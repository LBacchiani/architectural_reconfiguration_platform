import pulumi
import pulumi_kubernetes as k8s
import os
from pulumi import automation as auto
import uuid

def create_pod_name(service_name, stack_name):
    """Generate a unique pod name based on service and stack"""
    return f'{service_name}-{stack_name}-{str(uuid.uuid4())[:8]}'

def pulumi_program():
    stack = pulumi.get_stack()
    image_076df714_c307_4bd2_8b8f_0a1bf69f1d1e_name = create_pod_name('image-076df714-c307-4bd2-8b8f-0a1bf69f1d1e', stack)
    image_076df714_c307_4bd2_8b8f_0a1bf69f1d1e = k8s.core.v1.Pod(image_076df714_c307_4bd2_8b8f_0a1bf69f1d1e_name, metadata=k8s.meta.v1.ObjectMetaArgs(name=image_076df714_c307_4bd2_8b8f_0a1bf69f1d1e_name, labels={**{'type': 'image-type'}, 'stack': stack, 'original_service': 'image-076df714-c307-4bd2-8b8f-0a1bf69f1d1e'}), spec=k8s.core.v1.PodSpecArgs(containers=[k8s.core.v1.ContainerArgs(name='giovaz94-tea-store-general', image='giovaz94/tea-store-general', resources=k8s.core.v1.ResourceRequirementsArgs(requests={'cpu': '10m', 'memory': '10M'}), env=[k8s.core.v1.EnvVarArgs(name='MCL', value='190'), k8s.core.v1.EnvVarArgs(name='SERVICE_NAME', value='image'), k8s.core.v1.EnvVarArgs(name='PORT', value='8002'), k8s.core.v1.EnvVarArgs(name='OUTPUT_SERVICES', value='{"http://persistence-service:8003/request":"1"}')])], node_name='giovserver'))
    image_6a6e05ea_35e9_4791_9e88_31a9a6022e6b_name = create_pod_name('image-6a6e05ea-35e9-4791-9e88-31a9a6022e6b', stack)
    image_6a6e05ea_35e9_4791_9e88_31a9a6022e6b = k8s.core.v1.Pod(image_6a6e05ea_35e9_4791_9e88_31a9a6022e6b_name, metadata=k8s.meta.v1.ObjectMetaArgs(name=image_6a6e05ea_35e9_4791_9e88_31a9a6022e6b_name, labels={**{'type': 'image-type'}, 'stack': stack, 'original_service': 'image-6a6e05ea-35e9-4791-9e88-31a9a6022e6b'}), spec=k8s.core.v1.PodSpecArgs(containers=[k8s.core.v1.ContainerArgs(name='giovaz94-tea-store-general', image='giovaz94/tea-store-general', resources=k8s.core.v1.ResourceRequirementsArgs(requests={'cpu': '10m', 'memory': '10M'}), env=[k8s.core.v1.EnvVarArgs(name='MCL', value='190'), k8s.core.v1.EnvVarArgs(name='SERVICE_NAME', value='image'), k8s.core.v1.EnvVarArgs(name='PORT', value='8002'), k8s.core.v1.EnvVarArgs(name='OUTPUT_SERVICES', value='{"http://persistence-service:8003/request":"1"}')])], node_name='giovserver'))
    persistence_8b96c406_d374_4c1e_9913_b7e28a2cb6b8_name = create_pod_name('persistence-8b96c406-d374-4c1e-9913-b7e28a2cb6b8', stack)
    persistence_8b96c406_d374_4c1e_9913_b7e28a2cb6b8 = k8s.core.v1.Pod(persistence_8b96c406_d374_4c1e_9913_b7e28a2cb6b8_name, metadata=k8s.meta.v1.ObjectMetaArgs(name=persistence_8b96c406_d374_4c1e_9913_b7e28a2cb6b8_name, labels={**{'type': 'persistence-type'}, 'stack': stack, 'original_service': 'persistence-8b96c406-d374-4c1e-9913-b7e28a2cb6b8'}), spec=k8s.core.v1.PodSpecArgs(containers=[k8s.core.v1.ContainerArgs(name='giovaz94-tea-store-general', image='giovaz94/tea-store-general', resources=k8s.core.v1.ResourceRequirementsArgs(requests={'cpu': '10m', 'memory': '10M'}), env=[k8s.core.v1.EnvVarArgs(name='MCL', value='190'), k8s.core.v1.EnvVarArgs(name='SERVICE_NAME', value='persistence'), k8s.core.v1.EnvVarArgs(name='PORT', value='8003')])], node_name='giovserver'))
    webui_8de9d113_2481_4a57_a1cc_adb9822be4f4_name = create_pod_name('webui-8de9d113-2481-4a57-a1cc-adb9822be4f4', stack)
    webui_8de9d113_2481_4a57_a1cc_adb9822be4f4 = k8s.core.v1.Pod(webui_8de9d113_2481_4a57_a1cc_adb9822be4f4_name, metadata=k8s.meta.v1.ObjectMetaArgs(name=webui_8de9d113_2481_4a57_a1cc_adb9822be4f4_name, labels={**{'type': 'webui-type'}, 'stack': stack, 'original_service': 'webui-8de9d113-2481-4a57-a1cc-adb9822be4f4'}), spec=k8s.core.v1.PodSpecArgs(containers=[k8s.core.v1.ContainerArgs(name='giovaz94-tea-store-general', image='giovaz94/tea-store-general', resources=k8s.core.v1.ResourceRequirementsArgs(requests={'cpu': '10m', 'memory': '10M'}), env=[k8s.core.v1.EnvVarArgs(name='MCL', value='150'), k8s.core.v1.EnvVarArgs(name='SERVICE_NAME', value='webUI'), k8s.core.v1.EnvVarArgs(name='PORT_IMAGE_SERVICE', value='image-service'), k8s.core.v1.EnvVarArgs(name='PORT_PERSISTENCE_SERVICE', value='persistence-service'), k8s.core.v1.EnvVarArgs(name='PORT_AUTH_SERVICE', value='auth-service'), k8s.core.v1.EnvVarArgs(name='PORT_RECOMMENDER_SERVICE', value='recommender-service'), k8s.core.v1.EnvVarArgs(name='PORT', value='8001'), k8s.core.v1.EnvVarArgs(name='OUTPUT_SERVICES', value='{"http://recommender-service:8005/request":"1","http://image-service:8004/request":"2","http://persistence-service:8003/request":"1","http://auth-service:8002/request":"1"}')])], node_name='giovserver'))
    auth_6734c947_70f9_4ff1_aeb4_43df3508b444_name = create_pod_name('auth-6734c947-70f9-4ff1-aeb4-43df3508b444', stack)
    auth_6734c947_70f9_4ff1_aeb4_43df3508b444 = k8s.core.v1.Pod(auth_6734c947_70f9_4ff1_aeb4_43df3508b444_name, metadata=k8s.meta.v1.ObjectMetaArgs(name=auth_6734c947_70f9_4ff1_aeb4_43df3508b444_name, labels={**{'type': 'auth-type'}, 'stack': stack, 'original_service': 'auth-6734c947-70f9-4ff1-aeb4-43df3508b444'}), spec=k8s.core.v1.PodSpecArgs(containers=[k8s.core.v1.ContainerArgs(name='giovaz94-tea-store-general', image='giovaz94/tea-store-general', resources=k8s.core.v1.ResourceRequirementsArgs(requests={'cpu': '10m', 'memory': '10M'}), env=[k8s.core.v1.EnvVarArgs(name='MCL', value='190'), k8s.core.v1.EnvVarArgs(name='SERVICE_NAME', value='auth'), k8s.core.v1.EnvVarArgs(name='PORT', value='8002'), k8s.core.v1.EnvVarArgs(name='PORT_PERSISTENCE_SERVICE', value='persistence-service'), k8s.core.v1.EnvVarArgs(name='OUTPUT_SERVICES', value='{"http://persistence-service:8003/request":"1"}')])], node_name='giovserver'))
    pulumi.export('image-076df714-c307-4bd2-8b8f-0a1bf69f1d1e_name', image_076df714_c307_4bd2_8b8f_0a1bf69f1d1e.metadata['name'])
    pulumi.export('image-6a6e05ea-35e9-4791-9e88-31a9a6022e6b_name', image_6a6e05ea_35e9_4791_9e88_31a9a6022e6b.metadata['name'])
    pulumi.export('persistence-8b96c406-d374-4c1e-9913-b7e28a2cb6b8_name', persistence_8b96c406_d374_4c1e_9913_b7e28a2cb6b8.metadata['name'])
    pulumi.export('webui-8de9d113-2481-4a57-a1cc-adb9822be4f4_name', webui_8de9d113_2481_4a57_a1cc_adb9822be4f4.metadata['name'])
    pulumi.export('auth-6734c947-70f9-4ff1-aeb4-43df3508b444_name', auth_6734c947_70f9_4ff1_aeb4_43df3508b444.metadata['name'])

def deploy_orchestration(stack_name):
    stack = auto.create_or_select_stack(stack_name=stack_name, project_name='pulumi-k8s-increase-a1f48ec5-60c3-4ab5-adb4-ab61aa4a1cd5', program=pulumi_program)
    print(f'Successfully initialized stack: {stack_name}')
    kubeconfig_path = os.getenv('KUBECONFIG', '~/.kube/config')
    print(f'Using kubeconfig: {kubeconfig_path}')
    print('Refreshing stack...')
    stack.refresh(on_output=print)
    print('Previewing changes...')
    stack.preview(on_output=print)
    print('Deploying changes...')
    up_res = stack.up(on_output=print)
    print(f"\nResources created in stack '{stack_name}':")
    print(f"Pod image-076df714-c307-4bd2-8b8f-0a1bf69f1d1e Name: {up_res.outputs['image-076df714-c307-4bd2-8b8f-0a1bf69f1d1e_name'].value}")
    print(f"Pod image-6a6e05ea-35e9-4791-9e88-31a9a6022e6b Name: {up_res.outputs['image-6a6e05ea-35e9-4791-9e88-31a9a6022e6b_name'].value}")
    print(f"Pod persistence-8b96c406-d374-4c1e-9913-b7e28a2cb6b8 Name: {up_res.outputs['persistence-8b96c406-d374-4c1e-9913-b7e28a2cb6b8_name'].value}")
    print(f"Pod webui-8de9d113-2481-4a57-a1cc-adb9822be4f4 Name: {up_res.outputs['webui-8de9d113-2481-4a57-a1cc-adb9822be4f4_name'].value}")
    print(f"Pod auth-6734c947-70f9-4ff1-aeb4-43df3508b444 Name: {up_res.outputs['auth-6734c947-70f9-4ff1-aeb4-43df3508b444_name'].value}")

def destroy_pods(stack_name):
    stack = auto.create_or_select_stack(stack_name=stack_name, project_name='pulumi-k8s-increase-a1f48ec5-60c3-4ab5-adb4-ab61aa4a1cd5', program=lambda: None)
    print(f'Destroying resources in stack: {stack_name}...')
    stack.destroy(on_output=print)
    print('Resources successfully destroyed.')
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python script.py stack_name [destroy]')
        sys.exit(1)
    stack_name = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == 'destroy':
        destroy_pods(stack_name)
    else:
        deploy_orchestration(stack_name)