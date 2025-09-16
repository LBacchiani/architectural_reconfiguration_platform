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
    image_21343c2d_cb63_4068_a679_34bf2171e9ac_name = create_pod_name('image-21343c2d-cb63-4068-a679-34bf2171e9ac', stack)
    image_21343c2d_cb63_4068_a679_34bf2171e9ac = k8s.core.v1.Pod(image_21343c2d_cb63_4068_a679_34bf2171e9ac_name, metadata=k8s.meta.v1.ObjectMetaArgs(name=image_21343c2d_cb63_4068_a679_34bf2171e9ac_name, labels={**{'type': 'image-type'}, 'stack': stack, 'original_service': 'image-21343c2d-cb63-4068-a679-34bf2171e9ac'}), spec=k8s.core.v1.PodSpecArgs(containers=[k8s.core.v1.ContainerArgs(name='giovaz94-tea-store-general', image='giovaz94/tea-store-general', resources=k8s.core.v1.ResourceRequirementsArgs(requests={'cpu': '10m', 'memory': '10M'}), env=[k8s.core.v1.EnvVarArgs(name='MCL', value='190'), k8s.core.v1.EnvVarArgs(name='SERVICE_NAME', value='image'), k8s.core.v1.EnvVarArgs(name='PORT', value='8002'), k8s.core.v1.EnvVarArgs(name='OUTPUT_SERVICES', value='{"http://persistence-service:8003/request":"1"}')])], node_name='giovserver'))
    image_7896fef8_6e7f_4749_bcd7_f49b9eb69ee3_name = create_pod_name('image-7896fef8-6e7f-4749-bcd7-f49b9eb69ee3', stack)
    image_7896fef8_6e7f_4749_bcd7_f49b9eb69ee3 = k8s.core.v1.Pod(image_7896fef8_6e7f_4749_bcd7_f49b9eb69ee3_name, metadata=k8s.meta.v1.ObjectMetaArgs(name=image_7896fef8_6e7f_4749_bcd7_f49b9eb69ee3_name, labels={**{'type': 'image-type'}, 'stack': stack, 'original_service': 'image-7896fef8-6e7f-4749-bcd7-f49b9eb69ee3'}), spec=k8s.core.v1.PodSpecArgs(containers=[k8s.core.v1.ContainerArgs(name='giovaz94-tea-store-general', image='giovaz94/tea-store-general', resources=k8s.core.v1.ResourceRequirementsArgs(requests={'cpu': '10m', 'memory': '10M'}), env=[k8s.core.v1.EnvVarArgs(name='MCL', value='190'), k8s.core.v1.EnvVarArgs(name='SERVICE_NAME', value='image'), k8s.core.v1.EnvVarArgs(name='PORT', value='8002'), k8s.core.v1.EnvVarArgs(name='OUTPUT_SERVICES', value='{"http://persistence-service:8003/request":"1"}')])], node_name='giovserver'))
    persistence_01b367da_3dd2_469e_9f64_99208cf1e456_name = create_pod_name('persistence-01b367da-3dd2-469e-9f64-99208cf1e456', stack)
    persistence_01b367da_3dd2_469e_9f64_99208cf1e456 = k8s.core.v1.Pod(persistence_01b367da_3dd2_469e_9f64_99208cf1e456_name, metadata=k8s.meta.v1.ObjectMetaArgs(name=persistence_01b367da_3dd2_469e_9f64_99208cf1e456_name, labels={**{'type': 'persistence-type'}, 'stack': stack, 'original_service': 'persistence-01b367da-3dd2-469e-9f64-99208cf1e456'}), spec=k8s.core.v1.PodSpecArgs(containers=[k8s.core.v1.ContainerArgs(name='giovaz94-tea-store-general', image='giovaz94/tea-store-general', resources=k8s.core.v1.ResourceRequirementsArgs(requests={'cpu': '10m', 'memory': '10M'}), env=[k8s.core.v1.EnvVarArgs(name='MCL', value='190'), k8s.core.v1.EnvVarArgs(name='SERVICE_NAME', value='persistence'), k8s.core.v1.EnvVarArgs(name='PORT', value='8003')])], node_name='giovserver'))
    webui_1a146abb_ed94_4747_8f14_e01a014e1fc2_name = create_pod_name('webui-1a146abb-ed94-4747-8f14-e01a014e1fc2', stack)
    webui_1a146abb_ed94_4747_8f14_e01a014e1fc2 = k8s.core.v1.Pod(webui_1a146abb_ed94_4747_8f14_e01a014e1fc2_name, metadata=k8s.meta.v1.ObjectMetaArgs(name=webui_1a146abb_ed94_4747_8f14_e01a014e1fc2_name, labels={**{'type': 'webui-type'}, 'stack': stack, 'original_service': 'webui-1a146abb-ed94-4747-8f14-e01a014e1fc2'}), spec=k8s.core.v1.PodSpecArgs(containers=[k8s.core.v1.ContainerArgs(name='giovaz94-tea-store-general', image='giovaz94/tea-store-general', resources=k8s.core.v1.ResourceRequirementsArgs(requests={'cpu': '10m', 'memory': '10M'}), env=[k8s.core.v1.EnvVarArgs(name='MCL', value='150'), k8s.core.v1.EnvVarArgs(name='SERVICE_NAME', value='webUI'), k8s.core.v1.EnvVarArgs(name='PORT_IMAGE_SERVICE', value='image-service'), k8s.core.v1.EnvVarArgs(name='PORT_PERSISTENCE_SERVICE', value='persistence-service'), k8s.core.v1.EnvVarArgs(name='PORT_AUTH_SERVICE', value='auth-service'), k8s.core.v1.EnvVarArgs(name='PORT_RECOMMENDER_SERVICE', value='recommender-service'), k8s.core.v1.EnvVarArgs(name='PORT', value='8001'), k8s.core.v1.EnvVarArgs(name='OUTPUT_SERVICES', value='{"http://recommender-service:8005/request":"1","http://image-service:8004/request":"2","http://persistence-service:8003/request":"1","http://auth-service:8002/request":"1"}')])], node_name='giovserver'))
    webui_76cb873f_d555_42fe_83fb_91ae6f0e5855_name = create_pod_name('webui-76cb873f-d555-42fe-83fb-91ae6f0e5855', stack)
    webui_76cb873f_d555_42fe_83fb_91ae6f0e5855 = k8s.core.v1.Pod(webui_76cb873f_d555_42fe_83fb_91ae6f0e5855_name, metadata=k8s.meta.v1.ObjectMetaArgs(name=webui_76cb873f_d555_42fe_83fb_91ae6f0e5855_name, labels={**{'type': 'webui-type'}, 'stack': stack, 'original_service': 'webui-76cb873f-d555-42fe-83fb-91ae6f0e5855'}), spec=k8s.core.v1.PodSpecArgs(containers=[k8s.core.v1.ContainerArgs(name='giovaz94-tea-store-general', image='giovaz94/tea-store-general', resources=k8s.core.v1.ResourceRequirementsArgs(requests={'cpu': '10m', 'memory': '10M'}), env=[k8s.core.v1.EnvVarArgs(name='MCL', value='150'), k8s.core.v1.EnvVarArgs(name='SERVICE_NAME', value='webUI'), k8s.core.v1.EnvVarArgs(name='PORT_IMAGE_SERVICE', value='image-service'), k8s.core.v1.EnvVarArgs(name='PORT_PERSISTENCE_SERVICE', value='persistence-service'), k8s.core.v1.EnvVarArgs(name='PORT_AUTH_SERVICE', value='auth-service'), k8s.core.v1.EnvVarArgs(name='PORT_RECOMMENDER_SERVICE', value='recommender-service'), k8s.core.v1.EnvVarArgs(name='PORT', value='8001'), k8s.core.v1.EnvVarArgs(name='OUTPUT_SERVICES', value='{"http://recommender-service:8005/request":"1","http://image-service:8004/request":"2","http://persistence-service:8003/request":"1","http://auth-service:8002/request":"1"}')])], node_name='giovserver'))
    auth_58cf6f86_8e8f_48c8_88dd_d819e670b4c1_name = create_pod_name('auth-58cf6f86-8e8f-48c8-88dd-d819e670b4c1', stack)
    auth_58cf6f86_8e8f_48c8_88dd_d819e670b4c1 = k8s.core.v1.Pod(auth_58cf6f86_8e8f_48c8_88dd_d819e670b4c1_name, metadata=k8s.meta.v1.ObjectMetaArgs(name=auth_58cf6f86_8e8f_48c8_88dd_d819e670b4c1_name, labels={**{'type': 'auth-type'}, 'stack': stack, 'original_service': 'auth-58cf6f86-8e8f-48c8-88dd-d819e670b4c1'}), spec=k8s.core.v1.PodSpecArgs(containers=[k8s.core.v1.ContainerArgs(name='giovaz94-tea-store-general', image='giovaz94/tea-store-general', resources=k8s.core.v1.ResourceRequirementsArgs(requests={'cpu': '10m', 'memory': '10M'}), env=[k8s.core.v1.EnvVarArgs(name='MCL', value='190'), k8s.core.v1.EnvVarArgs(name='SERVICE_NAME', value='auth'), k8s.core.v1.EnvVarArgs(name='PORT', value='8002'), k8s.core.v1.EnvVarArgs(name='PORT_PERSISTENCE_SERVICE', value='persistence-service'), k8s.core.v1.EnvVarArgs(name='OUTPUT_SERVICES', value='{"http://persistence-service:8003/request":"1"}')])], node_name='giovserver'))
    pulumi.export('image-21343c2d-cb63-4068-a679-34bf2171e9ac_name', image_21343c2d_cb63_4068_a679_34bf2171e9ac.metadata['name'])
    pulumi.export('image-7896fef8-6e7f-4749-bcd7-f49b9eb69ee3_name', image_7896fef8_6e7f_4749_bcd7_f49b9eb69ee3.metadata['name'])
    pulumi.export('persistence-01b367da-3dd2-469e-9f64-99208cf1e456_name', persistence_01b367da_3dd2_469e_9f64_99208cf1e456.metadata['name'])
    pulumi.export('webui-1a146abb-ed94-4747-8f14-e01a014e1fc2_name', webui_1a146abb_ed94_4747_8f14_e01a014e1fc2.metadata['name'])
    pulumi.export('webui-76cb873f-d555-42fe-83fb-91ae6f0e5855_name', webui_76cb873f_d555_42fe_83fb_91ae6f0e5855.metadata['name'])
    pulumi.export('auth-58cf6f86-8e8f-48c8-88dd-d819e670b4c1_name', auth_58cf6f86_8e8f_48c8_88dd_d819e670b4c1.metadata['name'])

def deploy_orchestration(stack_name):
    stack = auto.create_or_select_stack(stack_name=stack_name, project_name='pulumi-k8s-increase-21313e63-56eb-4fdd-99d6-37ab2947bf18', program=pulumi_program)
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
    print(f"Pod image-21343c2d-cb63-4068-a679-34bf2171e9ac Name: {up_res.outputs['image-21343c2d-cb63-4068-a679-34bf2171e9ac_name'].value}")
    print(f"Pod image-7896fef8-6e7f-4749-bcd7-f49b9eb69ee3 Name: {up_res.outputs['image-7896fef8-6e7f-4749-bcd7-f49b9eb69ee3_name'].value}")
    print(f"Pod persistence-01b367da-3dd2-469e-9f64-99208cf1e456 Name: {up_res.outputs['persistence-01b367da-3dd2-469e-9f64-99208cf1e456_name'].value}")
    print(f"Pod webui-1a146abb-ed94-4747-8f14-e01a014e1fc2 Name: {up_res.outputs['webui-1a146abb-ed94-4747-8f14-e01a014e1fc2_name'].value}")
    print(f"Pod webui-76cb873f-d555-42fe-83fb-91ae6f0e5855 Name: {up_res.outputs['webui-76cb873f-d555-42fe-83fb-91ae6f0e5855_name'].value}")
    print(f"Pod auth-58cf6f86-8e8f-48c8-88dd-d819e670b4c1 Name: {up_res.outputs['auth-58cf6f86-8e8f-48c8-88dd-d819e670b4c1_name'].value}")

def destroy_pods(stack_name):
    stack = auto.create_or_select_stack(stack_name=stack_name, project_name='pulumi-k8s-increase-21313e63-56eb-4fdd-99d6-37ab2947bf18', program=lambda: None)
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