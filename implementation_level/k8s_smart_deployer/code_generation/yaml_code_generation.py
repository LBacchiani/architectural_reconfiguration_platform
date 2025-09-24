import os
import uuid
import yaml
from code_generation.utilities import to_dns_name


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def enumerate_service_groups(input_list):
    seen = set()
    result = []

    for host, service in input_list:
        if service not in seen:
            # Only add the first occurrence of each service
            result.append((host, 0, service))  # 0 as placeholder for index
            seen.add(service)

    return result



def add_pod_definitions(order, components, instances, optimal):
    component_mapping = {comp['type']: comp for comp in components}
    replicas_mapping = {inst["type"]: inst["replicas"] for inst in instances}
    pod_definitions = []
    name_to_variable = {}
    indexed_services = enumerate_service_groups(order)

    service_variable_map = {}
    for node_name, service_idx, service_name in indexed_services:
        variable_name = f"{service_name}-{to_dns_name(str(uuid.uuid4()))}".replace("-type", "")
        if service_name not in name_to_variable:
            name_to_variable[service_name] = []
        name_to_variable[service_name].append(variable_name)
        service_variable_map[(node_name, service_idx, service_name)] = variable_name

    for node_name, service_idx, service_name in indexed_services:
        variable_name = name_to_variable[service_name][service_idx]
        component = component_mapping.get(service_name)
        if not component:
            continue

        kind = component.get("kind")
        mapped_dependencies = {}

        ports_required = component.get('ports', {}).get('strong', [])
        for entry in ports_required:
            dep_name = entry.get("id")
            dep_type = entry.get("type")
            dep_count = entry.get("value", 1)
            dep_config = entry.get("config", {})
            if dep_name:
                mapped_dependencies[dep_name] = [dep_type, dep_count, dep_config]

        if 'metadata' in component and 'labels' in component['metadata']:
            component['metadata']['labels']['type'] = component['type']
        else:
            component['metadata'] = {'labels': {'type': component['type']}}

        depends_on = []
        if kind == 'Pod':
            containers = component['spec']['containers']
            for container in containers:
                env_list = container.get("env", [])
                for dep_name, dep_info in mapped_dependencies.items():
                    dep_type = dep_info[0]
                    dep_count = dep_info[1]
                    dep_config = dep_info[2]

                    container_names = [c['name'] for c in dep_config.get('containers', []) if 'name' in c]
                    if container['name'] in container_names:
                        if dep_type in name_to_variable:
                            value = name_to_variable[dep_type][0]
                            env_list.append({"name": dep_name, "value": value})
                            depends_on.extend(f"${{{name_to_variable[dep_type][i]}}}" for i in range(dep_count))
                        else:
                            env_list.append({"name": dep_name, "type": dep_type})

            replicas = replicas_mapping.get(component['type'], 1)
            props = create_deployment_definition(
                variable_name,
                component,
                node_name if optimal else None,
                replicas
            )

        elif kind == 'Service':
            props = create_service_definition(variable_name, component)
            for dep_name, dep_info in mapped_dependencies.items():
                count = dep_info[0]
                if dep_name in name_to_variable:
                    depends_on.extend(f"${{{name_to_variable[dep_name][i]}}}" for i in range(count))

        pod_definitions.append({
            'name': variable_name,
            'type': 'kubernetes:apps/v1:Deployment' if kind == 'Pod' else 'kubernetes:core/v1:Service',
            'properties': props,
            'options': {"dependsOn": depends_on} if depends_on else {"customTimeouts": {"create": "50ms", "update": "50ms", "delete": "50ms"}}
        })

    return pod_definitions


def create_deployment_definition(name, component, node_name=None, replicas=1):
    spec = {
        'replicas': replicas,
        'selector': {
            'matchLabels': {
                **component['metadata'].get('labels', {})
            }
        },
        'template': {
            'metadata': {
                'labels': {
                    **component['metadata'].get('labels', {})
                }
            },
            'spec': {
                'containers': component['spec']['containers']
            }
        }
    }

    if node_name is not None:   
        spec['template']['spec']['nodeSelector'] = {
            'kubernetes.io/hostname': node_name
        }

    return {
        'apiVersion': 'apps/v1',
        'kind': 'Deployment',
        'metadata': {
            'name': name,
            'labels': component['metadata'].get('labels', {})
        },
        'spec': spec
    }


def create_service_definition(name, component):
    return {
        'apiVersion': 'v1',
        'kind': 'Service',
        'metadata': {
            'name': name,
            'labels': component['metadata'].get('labels', {})
        },
        'spec': component['spec']
    }


def no_dash_representer(dumper, value):
    return dumper.represent_mapping('tag:yaml.org,2002:map', value.items(), flow_style=False)


def generate_yaml_definition(orchestration_name, order, components, folder_name, instances, optimal):
    os.makedirs(folder_name, exist_ok=True)
    yaml.add_representer(dict, no_dash_representer)

    pulumi_yaml = {
        'name': orchestration_name,
        'runtime': 'yaml',
        'resources': { pod['name']: pod for pod in add_pod_definitions(order, components, instances, optimal) }
    }
    with open(f"{folder_name}/orchestration.yaml", "w") as file:
        yaml.dump(pulumi_yaml, file, default_flow_style=False, Dumper=NoAliasDumper, sort_keys=False)
