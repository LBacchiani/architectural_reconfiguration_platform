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
    message_analyzer_0405631c_044f_4952_b3df_984f253cd473_name = create_pod_name('message-analyzer-0405631c-044f-4952-b3df-984f253cd473', stack)
    message_analyzer_0405631c_044f_4952_b3df_984f253cd473 = k8s.core.v1.Pod(message_analyzer_0405631c_044f_4952_b3df_984f253cd473_name, metadata=k8s.meta.v1.ObjectMetaArgs(name=message_analyzer_0405631c_044f_4952_b3df_984f253cd473_name, labels={**{'type': 'message-analyzer-type'}, 'stack': stack, 'original_service': 'message-analyzer-0405631c-044f-4952-b3df-984f253cd473'}), spec=k8s.core.v1.PodSpecArgs(containers=[k8s.core.v1.ContainerArgs(name='giovaz94-mail-pipeline-general', image='giovaz94/mail-pipeline-general', resources=k8s.core.v1.ResourceRequirementsArgs(requests={'cpu': '10m', 'memory': '10M'}), env=[k8s.core.v1.EnvVarArgs(name='MCL', value='300'), k8s.core.v1.EnvVarArgs(name='REDIS_HOST', value='redis-service'), k8s.core.v1.EnvVarArgs(name='SERVICE_NAME', value='message-analyzer'), k8s.core.v1.EnvVarArgs(name='PORT', value='80'), k8s.core.v1.EnvVarArgs(name='MAX_SIZE', value='800'), k8s.core.v1.EnvVarArgs(name='MAX_CONNECTIONS', value='70'), k8s.core.v1.EnvVarArgs(name='PIPELINE_COUNT', value='1')])], node_name='giovserver'))
    message_analyzer_297ea803_628b_4fd7_9816_61e4a6d27934_name = create_pod_name('message-analyzer-297ea803-628b-4fd7-9816-61e4a6d27934', stack)
    message_analyzer_297ea803_628b_4fd7_9816_61e4a6d27934 = k8s.core.v1.Pod(message_analyzer_297ea803_628b_4fd7_9816_61e4a6d27934_name, metadata=k8s.meta.v1.ObjectMetaArgs(name=message_analyzer_297ea803_628b_4fd7_9816_61e4a6d27934_name, labels={**{'type': 'message-analyzer-type'}, 'stack': stack, 'original_service': 'message-analyzer-297ea803-628b-4fd7-9816-61e4a6d27934'}), spec=k8s.core.v1.PodSpecArgs(containers=[k8s.core.v1.ContainerArgs(name='giovaz94-mail-pipeline-general', image='giovaz94/mail-pipeline-general', resources=k8s.core.v1.ResourceRequirementsArgs(requests={'cpu': '10m', 'memory': '10M'}), env=[k8s.core.v1.EnvVarArgs(name='MCL', value='300'), k8s.core.v1.EnvVarArgs(name='REDIS_HOST', value='redis-service'), k8s.core.v1.EnvVarArgs(name='SERVICE_NAME', value='message-analyzer'), k8s.core.v1.EnvVarArgs(name='PORT', value='80'), k8s.core.v1.EnvVarArgs(name='MAX_SIZE', value='800'), k8s.core.v1.EnvVarArgs(name='MAX_CONNECTIONS', value='70'), k8s.core.v1.EnvVarArgs(name='PIPELINE_COUNT', value='1')])], node_name='giovserver'))
    message_analyzer_service_25772f46_3d92_455c_89e8_2dbbca2c4d50 = k8s.core.v1.Service('message-analyzer-service-25772f46-3d92-455c-89e8-2dbbca2c4d50', metadata=k8s.meta.v1.ObjectMetaArgs(name='message-analyzer-service-25772f46-3d92-455c-89e8-2dbbca2c4d50', labels={**{'type': 'message-analyzer-service-type'}, 'stack': stack, 'original_service': 'message-analyzer-service-25772f46-3d92-455c-89e8-2dbbca2c4d50'}), spec=k8s.core.v1.ServiceSpecArgs(selector={'type': 'message-analyzer-type'}, ports=[k8s.core.v1.ServicePortArgs(port=80, target_port=80)]), opts=pulumi.ResourceOptions(depends_on=[message_analyzer_0405631c_044f_4952_b3df_984f253cd473]))
    image_analyzer_3996cf3f_82f2_4566_a43c_9c10d09412df_name = create_pod_name('image-analyzer-3996cf3f-82f2-4566-a43c-9c10d09412df', stack)
    image_analyzer_3996cf3f_82f2_4566_a43c_9c10d09412df = k8s.core.v1.Pod(image_analyzer_3996cf3f_82f2_4566_a43c_9c10d09412df_name, metadata=k8s.meta.v1.ObjectMetaArgs(name=image_analyzer_3996cf3f_82f2_4566_a43c_9c10d09412df_name, labels={**{'type': 'image-analyzer-type'}, 'stack': stack, 'original_service': 'image-analyzer-3996cf3f-82f2-4566-a43c-9c10d09412df'}), spec=k8s.core.v1.PodSpecArgs(containers=[k8s.core.v1.ContainerArgs(name='giovaz94-mail-pipeline-general', image='giovaz94/mail-pipeline-general', resources=k8s.core.v1.ResourceRequirementsArgs(requests={'cpu': '10m', 'memory': '10M'}), env=[k8s.core.v1.EnvVarArgs(name='MCL', value='231'), k8s.core.v1.EnvVarArgs(name='REDIS_HOST', value='redis-service'), k8s.core.v1.EnvVarArgs(name='SERVICE_NAME', value='image-analyzer'), k8s.core.v1.EnvVarArgs(name='PORT', value='80'), k8s.core.v1.EnvVarArgs(name='MAX_SIZE', value='800'), k8s.core.v1.EnvVarArgs(name='MAX_CONNECTIONS', value='70'), k8s.core.v1.EnvVarArgs(name='PIPELINE_COUNT', value='1')])], node_name='giovserver'), opts=pulumi.ResourceOptions(depends_on=[message_analyzer_service_25772f46_3d92_455c_89e8_2dbbca2c4d50]))
    image_analyzer_service_9b712430_6262_4a49_9adf_e4e4fe183c1f = k8s.core.v1.Service('image-analyzer-service-9b712430-6262-4a49-9adf-e4e4fe183c1f', metadata=k8s.meta.v1.ObjectMetaArgs(name='image-analyzer-service-9b712430-6262-4a49-9adf-e4e4fe183c1f', labels={**{'type': 'image-analyzer-service-type'}, 'stack': stack, 'original_service': 'image-analyzer-service-9b712430-6262-4a49-9adf-e4e4fe183c1f'}), spec=k8s.core.v1.ServiceSpecArgs(selector={'type': 'image-analyzer-type'}, ports=[k8s.core.v1.ServicePortArgs(port=80, target_port=80)]), opts=pulumi.ResourceOptions(depends_on=[image_analyzer_3996cf3f_82f2_4566_a43c_9c10d09412df]))
    attachment_manager_0ea9f6df_bf16_4ae7_95a1_d49772777f6f_name = create_pod_name('attachment-manager-0ea9f6df-bf16-4ae7-95a1-d49772777f6f', stack)
    attachment_manager_0ea9f6df_bf16_4ae7_95a1_d49772777f6f = k8s.core.v1.Pod(attachment_manager_0ea9f6df_bf16_4ae7_95a1_d49772777f6f_name, metadata=k8s.meta.v1.ObjectMetaArgs(name=attachment_manager_0ea9f6df_bf16_4ae7_95a1_d49772777f6f_name, labels={**{'type': 'attachment-manager-type'}, 'stack': stack, 'original_service': 'attachment-manager-0ea9f6df-bf16-4ae7-95a1-d49772777f6f'}), spec=k8s.core.v1.PodSpecArgs(containers=[k8s.core.v1.ContainerArgs(name='giovaz94-mail-pipeline-general', image='giovaz94/mail-pipeline-general', resources=k8s.core.v1.ResourceRequirementsArgs(requests={'cpu': '10m', 'memory': '10M'}), env=[k8s.core.v1.EnvVarArgs(name='MCL', value='231'), k8s.core.v1.EnvVarArgs(name='REDIS_HOST', value='redis-service'), k8s.core.v1.EnvVarArgs(name='SERVICE_NAME', value='attachment-manager'), k8s.core.v1.EnvVarArgs(name='PORT', value='80'), k8s.core.v1.EnvVarArgs(name='MAX_SIZE', value='800'), k8s.core.v1.EnvVarArgs(name='MAX_CONNECTIONS', value='70'), k8s.core.v1.EnvVarArgs(name='PIPELINE_COUNT', value='1')])], node_name='giovserver'), opts=pulumi.ResourceOptions(depends_on=[image_analyzer_service_9b712430_6262_4a49_9adf_e4e4fe183c1f]))
    attachment_manager_service_dca6a5a4_b938_41b7_bf8f_409d54fcee8d = k8s.core.v1.Service('attachment-manager-service-dca6a5a4-b938-41b7-bf8f-409d54fcee8d', metadata=k8s.meta.v1.ObjectMetaArgs(name='attachment-manager-service-dca6a5a4-b938-41b7-bf8f-409d54fcee8d', labels={**{'type': 'attachment-manager-service-type'}, 'stack': stack, 'original_service': 'attachment-manager-service-dca6a5a4-b938-41b7-bf8f-409d54fcee8d'}), spec=k8s.core.v1.ServiceSpecArgs(selector={'type': 'attachment-manager-type'}, ports=[k8s.core.v1.ServicePortArgs(port=80, target_port=80)]), opts=pulumi.ResourceOptions(depends_on=[attachment_manager_0ea9f6df_bf16_4ae7_95a1_d49772777f6f]))
    virus_scanner_62e4011c_2bd0_468d_ba3c_9c7be7b9376b_name = create_pod_name('virus-scanner-62e4011c-2bd0-468d-ba3c-9c7be7b9376b', stack)
    virus_scanner_62e4011c_2bd0_468d_ba3c_9c7be7b9376b = k8s.core.v1.Pod(virus_scanner_62e4011c_2bd0_468d_ba3c_9c7be7b9376b_name, metadata=k8s.meta.v1.ObjectMetaArgs(name=virus_scanner_62e4011c_2bd0_468d_ba3c_9c7be7b9376b_name, labels={**{'type': 'virus-scanner-type'}, 'stack': stack, 'original_service': 'virus-scanner-62e4011c-2bd0-468d-ba3c-9c7be7b9376b'}), spec=k8s.core.v1.PodSpecArgs(containers=[k8s.core.v1.ContainerArgs(name='giovaz94-mail-pipeline-general', image='giovaz94/mail-pipeline-general', resources=k8s.core.v1.ResourceRequirementsArgs(requests={'cpu': '10m', 'memory': '10M'}), env=[k8s.core.v1.EnvVarArgs(name='MCL', value='120'), k8s.core.v1.EnvVarArgs(name='REDIS_HOST', value='redis-service'), k8s.core.v1.EnvVarArgs(name='SERVICE_NAME', value='virus-scanner'), k8s.core.v1.EnvVarArgs(name='PORT', value='80'), k8s.core.v1.EnvVarArgs(name='MAX_SIZE', value='800'), k8s.core.v1.EnvVarArgs(name='MAX_CONNECTIONS', value='70'), k8s.core.v1.EnvVarArgs(name='PIPELINE_COUNT', value='1')])], node_name='giovserver'), opts=pulumi.ResourceOptions(depends_on=[message_analyzer_service_25772f46_3d92_455c_89e8_2dbbca2c4d50, attachment_manager_service_dca6a5a4_b938_41b7_bf8f_409d54fcee8d]))
    virus_scanner_257be5e2_804e_41c1_bff4_4446f14e4ab9_name = create_pod_name('virus-scanner-257be5e2-804e-41c1-bff4-4446f14e4ab9', stack)
    virus_scanner_257be5e2_804e_41c1_bff4_4446f14e4ab9 = k8s.core.v1.Pod(virus_scanner_257be5e2_804e_41c1_bff4_4446f14e4ab9_name, metadata=k8s.meta.v1.ObjectMetaArgs(name=virus_scanner_257be5e2_804e_41c1_bff4_4446f14e4ab9_name, labels={**{'type': 'virus-scanner-type'}, 'stack': stack, 'original_service': 'virus-scanner-257be5e2-804e-41c1-bff4-4446f14e4ab9'}), spec=k8s.core.v1.PodSpecArgs(containers=[k8s.core.v1.ContainerArgs(name='giovaz94-mail-pipeline-general', image='giovaz94/mail-pipeline-general', resources=k8s.core.v1.ResourceRequirementsArgs(requests={'cpu': '10m', 'memory': '10M'}), env=[k8s.core.v1.EnvVarArgs(name='MCL', value='120'), k8s.core.v1.EnvVarArgs(name='REDIS_HOST', value='redis-service'), k8s.core.v1.EnvVarArgs(name='SERVICE_NAME', value='virus-scanner'), k8s.core.v1.EnvVarArgs(name='PORT', value='80'), k8s.core.v1.EnvVarArgs(name='MAX_SIZE', value='800'), k8s.core.v1.EnvVarArgs(name='MAX_CONNECTIONS', value='70'), k8s.core.v1.EnvVarArgs(name='PIPELINE_COUNT', value='1')])], node_name='giovserver'), opts=pulumi.ResourceOptions(depends_on=[message_analyzer_service_25772f46_3d92_455c_89e8_2dbbca2c4d50, attachment_manager_service_dca6a5a4_b938_41b7_bf8f_409d54fcee8d]))
    pulumi.export('message-analyzer-0405631c-044f-4952-b3df-984f253cd473_name', message_analyzer_0405631c_044f_4952_b3df_984f253cd473.metadata['name'])
    pulumi.export('message-analyzer-297ea803-628b-4fd7-9816-61e4a6d27934_name', message_analyzer_297ea803_628b_4fd7_9816_61e4a6d27934.metadata['name'])
    pulumi.export('message-analyzer-service-25772f46-3d92-455c-89e8-2dbbca2c4d50_name', message_analyzer_service_25772f46_3d92_455c_89e8_2dbbca2c4d50.metadata['name'])
    pulumi.export('image-analyzer-3996cf3f-82f2-4566-a43c-9c10d09412df_name', image_analyzer_3996cf3f_82f2_4566_a43c_9c10d09412df.metadata['name'])
    pulumi.export('image-analyzer-service-9b712430-6262-4a49-9adf-e4e4fe183c1f_name', image_analyzer_service_9b712430_6262_4a49_9adf_e4e4fe183c1f.metadata['name'])
    pulumi.export('attachment-manager-0ea9f6df-bf16-4ae7-95a1-d49772777f6f_name', attachment_manager_0ea9f6df_bf16_4ae7_95a1_d49772777f6f.metadata['name'])
    pulumi.export('attachment-manager-service-dca6a5a4-b938-41b7-bf8f-409d54fcee8d_name', attachment_manager_service_dca6a5a4_b938_41b7_bf8f_409d54fcee8d.metadata['name'])
    pulumi.export('virus-scanner-62e4011c-2bd0-468d-ba3c-9c7be7b9376b_name', virus_scanner_62e4011c_2bd0_468d_ba3c_9c7be7b9376b.metadata['name'])
    pulumi.export('virus-scanner-257be5e2-804e-41c1-bff4-4446f14e4ab9_name', virus_scanner_257be5e2_804e_41c1_bff4_4446f14e4ab9.metadata['name'])

def deploy_orchestration(stack_name):
    stack = auto.create_or_select_stack(stack_name=stack_name, project_name='pulumi-k8s-increase-068ebae5-359f-405c-82cb-fe8843d1fb51', program=pulumi_program)
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
    print(f"Pod message-analyzer-0405631c-044f-4952-b3df-984f253cd473 Name: {up_res.outputs['message-analyzer-0405631c-044f-4952-b3df-984f253cd473_name'].value}")
    print(f"Pod message-analyzer-297ea803-628b-4fd7-9816-61e4a6d27934 Name: {up_res.outputs['message-analyzer-297ea803-628b-4fd7-9816-61e4a6d27934_name'].value}")
    print(f"Service message-analyzer-service-25772f46-3d92-455c-89e8-2dbbca2c4d50 Name: {up_res.outputs['message-analyzer-service-25772f46-3d92-455c-89e8-2dbbca2c4d50_name'].value}")
    print(f"Pod image-analyzer-3996cf3f-82f2-4566-a43c-9c10d09412df Name: {up_res.outputs['image-analyzer-3996cf3f-82f2-4566-a43c-9c10d09412df_name'].value}")
    print(f"Service image-analyzer-service-9b712430-6262-4a49-9adf-e4e4fe183c1f Name: {up_res.outputs['image-analyzer-service-9b712430-6262-4a49-9adf-e4e4fe183c1f_name'].value}")
    print(f"Pod attachment-manager-0ea9f6df-bf16-4ae7-95a1-d49772777f6f Name: {up_res.outputs['attachment-manager-0ea9f6df-bf16-4ae7-95a1-d49772777f6f_name'].value}")
    print(f"Service attachment-manager-service-dca6a5a4-b938-41b7-bf8f-409d54fcee8d Name: {up_res.outputs['attachment-manager-service-dca6a5a4-b938-41b7-bf8f-409d54fcee8d_name'].value}")
    print(f"Pod virus-scanner-62e4011c-2bd0-468d-ba3c-9c7be7b9376b Name: {up_res.outputs['virus-scanner-62e4011c-2bd0-468d-ba3c-9c7be7b9376b_name'].value}")
    print(f"Pod virus-scanner-257be5e2-804e-41c1-bff4-4446f14e4ab9 Name: {up_res.outputs['virus-scanner-257be5e2-804e-41c1-bff4-4446f14e4ab9_name'].value}")

def destroy_pods(stack_name):
    stack = auto.create_or_select_stack(stack_name=stack_name, project_name='pulumi-k8s-increase-068ebae5-359f-405c-82cb-fe8843d1fb51', program=lambda: None)
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