import pulumi
import pulumi_kubernetes as k8s
import os
from pulumi import automation as auto
import uuid

def create_pod_name(service_name, stack_name):
    """Generate a unique pod name based on service and stack"""
    return f"{service_name}-{stack_name}-{str(uuid.uuid4())[:8]}"

def pulumi_program():
    stack = pulumi.get_stack()

    
    image_3d0f9723_3233_4392_bb34_df909ccb89bb_name = create_pod_name('image-3d0f9723-3233-4392-bb34-df909ccb89bb', stack)

    image_3d0f9723_3233_4392_bb34_df909ccb89bb = k8s.core.v1.Pod(image_3d0f9723_3233_4392_bb34_df909ccb89bb_name,
        metadata=k8s.meta.v1.ObjectMetaArgs(
            name=image_3d0f9723_3233_4392_bb34_df909ccb89bb_name,
            labels={
                
                **{'type': 'image-type'},
                
                'stack': stack,
                'original_service': 'image-3d0f9723-3233-4392-bb34-df909ccb89bb'
            }
        ),
        spec=k8s.core.v1.PodSpecArgs(
            containers=[
                k8s.core.v1.ContainerArgs(
                    name='giovaz94-tea-store-general',
                    image='giovaz94/tea-store-general',
                    resources=k8s.core.v1.ResourceRequirementsArgs(
                        requests={
                            'cpu': '10m',
                            'memory': '10M'
                        }
                    ),
                    
                    env=[
                        
                        k8s.core.v1.EnvVarArgs(
                            name='MCL',
                            
                            value='600'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='SERVICE_NAME',
                            
                            value='image'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='MAX_SIZE',
                            
                            value='1000'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='PORT',
                            
                            value='80'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='OUTPUT_SERVICES',
                            
                            value='{}'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='MAX_CONNECTIONS',
                            
                            value='70'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='PIPELINE_COUNT',
                            
                            value='1'
                            
                        ),
                        
                    ],
                    
                )
            ],
            node_name='giovserver'
        ),
        
    )
    
        
    
    image_1e137021_76ef_40d6_9806_c7e99c50cce9_name = create_pod_name('image-1e137021-76ef-40d6-9806-c7e99c50cce9', stack)

    image_1e137021_76ef_40d6_9806_c7e99c50cce9 = k8s.core.v1.Pod(image_1e137021_76ef_40d6_9806_c7e99c50cce9_name,
        metadata=k8s.meta.v1.ObjectMetaArgs(
            name=image_1e137021_76ef_40d6_9806_c7e99c50cce9_name,
            labels={
                
                **{'type': 'image-type'},
                
                'stack': stack,
                'original_service': 'image-1e137021-76ef-40d6-9806-c7e99c50cce9'
            }
        ),
        spec=k8s.core.v1.PodSpecArgs(
            containers=[
                k8s.core.v1.ContainerArgs(
                    name='giovaz94-tea-store-general',
                    image='giovaz94/tea-store-general',
                    resources=k8s.core.v1.ResourceRequirementsArgs(
                        requests={
                            'cpu': '10m',
                            'memory': '10M'
                        }
                    ),
                    
                    env=[
                        
                        k8s.core.v1.EnvVarArgs(
                            name='MCL',
                            
                            value='600'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='SERVICE_NAME',
                            
                            value='image'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='MAX_SIZE',
                            
                            value='1000'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='PORT',
                            
                            value='80'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='OUTPUT_SERVICES',
                            
                            value='{}'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='MAX_CONNECTIONS',
                            
                            value='70'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='PIPELINE_COUNT',
                            
                            value='1'
                            
                        ),
                        
                    ],
                    
                )
            ],
            node_name='giovserver'
        ),
        
    )
    
        
    
    persistence_e290e42d_6d1f_45f7_ae22_ffda355c7012_name = create_pod_name('persistence-e290e42d-6d1f-45f7-ae22-ffda355c7012', stack)

    persistence_e290e42d_6d1f_45f7_ae22_ffda355c7012 = k8s.core.v1.Pod(persistence_e290e42d_6d1f_45f7_ae22_ffda355c7012_name,
        metadata=k8s.meta.v1.ObjectMetaArgs(
            name=persistence_e290e42d_6d1f_45f7_ae22_ffda355c7012_name,
            labels={
                
                **{'type': 'persistence-type'},
                
                'stack': stack,
                'original_service': 'persistence-e290e42d-6d1f-45f7-ae22-ffda355c7012'
            }
        ),
        spec=k8s.core.v1.PodSpecArgs(
            containers=[
                k8s.core.v1.ContainerArgs(
                    name='giovaz94-tea-store-general',
                    image='giovaz94/tea-store-general',
                    resources=k8s.core.v1.ResourceRequirementsArgs(
                        requests={
                            'cpu': '10m',
                            'memory': '10M'
                        }
                    ),
                    
                    env=[
                        
                        k8s.core.v1.EnvVarArgs(
                            name='MCL',
                            
                            value='905'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='SERVICE_NAME',
                            
                            value='persistence'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='PORT',
                            
                            value='80'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='MAX_SIZE',
                            
                            value='1000'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='OUTPUT_SERVICES',
                            
                            value='{}'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='MAX_CONNECTIONS',
                            
                            value='70'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='PIPELINE_COUNT',
                            
                            value='1'
                            
                        ),
                        
                    ],
                    
                )
            ],
            node_name='giovserver'
        ),
        
    )
    
        
    
    webui_660783fa_4f73_44f1_867c_9bc422be1e78_name = create_pod_name('webui-660783fa-4f73-44f1-867c-9bc422be1e78', stack)

    webui_660783fa_4f73_44f1_867c_9bc422be1e78 = k8s.core.v1.Pod(webui_660783fa_4f73_44f1_867c_9bc422be1e78_name,
        metadata=k8s.meta.v1.ObjectMetaArgs(
            name=webui_660783fa_4f73_44f1_867c_9bc422be1e78_name,
            labels={
                
                **{'type': 'webui-type'},
                
                'stack': stack,
                'original_service': 'webui-660783fa-4f73-44f1-867c-9bc422be1e78'
            }
        ),
        spec=k8s.core.v1.PodSpecArgs(
            containers=[
                k8s.core.v1.ContainerArgs(
                    name='giovaz94-tea-store-general',
                    image='giovaz94/tea-store-general',
                    resources=k8s.core.v1.ResourceRequirementsArgs(
                        requests={
                            'cpu': '10m',
                            'memory': '10M'
                        }
                    ),
                    
                    env=[
                        
                        k8s.core.v1.EnvVarArgs(
                            name='MCL',
                            
                            value='150'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='SERVICE_NAME',
                            
                            value='webUI'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='PORT',
                            
                            value='80'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='MAX_SIZE',
                            
                            value='1000'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='OUTPUT_SERVICES',
                            
                            value='{"http://persistence-service/request":"1", "http://recommender-service/request":"1", "http://image-service/request":"2"}'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='MAX_CONNECTIONS',
                            
                            value='70'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='PIPELINE_COUNT',
                            
                            value='1'
                            
                        ),
                        
                    ],
                    
                )
            ],
            node_name='giovserver'
        ),
        
    )
    
        
    
    auth_33c5783d_6439_428d_96eb_f7ebcc2ccd2b_name = create_pod_name('auth-33c5783d-6439-428d-96eb-f7ebcc2ccd2b', stack)

    auth_33c5783d_6439_428d_96eb_f7ebcc2ccd2b = k8s.core.v1.Pod(auth_33c5783d_6439_428d_96eb_f7ebcc2ccd2b_name,
        metadata=k8s.meta.v1.ObjectMetaArgs(
            name=auth_33c5783d_6439_428d_96eb_f7ebcc2ccd2b_name,
            labels={
                
                **{'type': 'auth-type'},
                
                'stack': stack,
                'original_service': 'auth-33c5783d-6439-428d-96eb-f7ebcc2ccd2b'
            }
        ),
        spec=k8s.core.v1.PodSpecArgs(
            containers=[
                k8s.core.v1.ContainerArgs(
                    name='giovaz94-tea-store-general',
                    image='giovaz94/tea-store-general',
                    resources=k8s.core.v1.ResourceRequirementsArgs(
                        requests={
                            'cpu': '10m',
                            'memory': '10M'
                        }
                    ),
                    
                    env=[
                        
                        k8s.core.v1.EnvVarArgs(
                            name='MCL',
                            
                            value='190'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='SERVICE_NAME',
                            
                            value='auth'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='PORT',
                            
                            value='80'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='MAX_SIZE',
                            
                            value='1000'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='OUTPUT_SERVICES',
                            
                            value='{"http://persistence-service/request":"1"}'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='MAX_CONNECTIONS',
                            
                            value='70'
                            
                        ),
                        
                        k8s.core.v1.EnvVarArgs(
                            name='PIPELINE_COUNT',
                            
                            value='1'
                            
                        ),
                        
                    ],
                    
                )
            ],
            node_name='giovserver'
        ),
        
    )
    
        
    

    # Export all resource names
    
        
    pulumi.export('image-3d0f9723-3233-4392-bb34-df909ccb89bb_name', image_3d0f9723_3233_4392_bb34_df909ccb89bb.metadata['name'])
        
    pulumi.export('image-1e137021-76ef-40d6-9806-c7e99c50cce9_name', image_1e137021_76ef_40d6_9806_c7e99c50cce9.metadata['name'])
        
    pulumi.export('persistence-e290e42d-6d1f-45f7-ae22-ffda355c7012_name', persistence_e290e42d_6d1f_45f7_ae22_ffda355c7012.metadata['name'])
        
    pulumi.export('webui-660783fa-4f73-44f1-867c-9bc422be1e78_name', webui_660783fa_4f73_44f1_867c_9bc422be1e78.metadata['name'])
        
    pulumi.export('auth-33c5783d-6439-428d-96eb-f7ebcc2ccd2b_name', auth_33c5783d_6439_428d_96eb_f7ebcc2ccd2b.metadata['name'])
        
    

def deploy_orchestration(stack_name):
    stack = auto.create_or_select_stack(
        stack_name=stack_name,
        project_name='pulumi-k8s-increase-4f7a1aff-7504-4b86-bce1-0248d152de7c',
        program=pulumi_program
    )

    print(f'Successfully initialized stack: {stack_name}')

    kubeconfig_path = os.getenv('KUBECONFIG', '~/.kube/config')
    print(f"Using kubeconfig: {kubeconfig_path}")

    print('Refreshing stack...')
    stack.refresh(on_output=print)

    print('Previewing changes...')
    stack.preview(on_output=print)

    print('Deploying changes...')
    up_res = stack.up(on_output=print)

    print(f"\nResources created in stack '{stack_name}':")
    
        
    print(f"Pod image-3d0f9723-3233-4392-bb34-df909ccb89bb Name: {up_res.outputs['image-3d0f9723-3233-4392-bb34-df909ccb89bb_name'].value}")
        
    print(f"Pod image-1e137021-76ef-40d6-9806-c7e99c50cce9 Name: {up_res.outputs['image-1e137021-76ef-40d6-9806-c7e99c50cce9_name'].value}")
        
    print(f"Pod persistence-e290e42d-6d1f-45f7-ae22-ffda355c7012 Name: {up_res.outputs['persistence-e290e42d-6d1f-45f7-ae22-ffda355c7012_name'].value}")
        
    print(f"Pod webui-660783fa-4f73-44f1-867c-9bc422be1e78 Name: {up_res.outputs['webui-660783fa-4f73-44f1-867c-9bc422be1e78_name'].value}")
        
    print(f"Pod auth-33c5783d-6439-428d-96eb-f7ebcc2ccd2b Name: {up_res.outputs['auth-33c5783d-6439-428d-96eb-f7ebcc2ccd2b_name'].value}")
        
    

def destroy_pods(stack_name):
    stack = auto.create_or_select_stack(
        stack_name=stack_name,
        project_name='pulumi-k8s-increase-4f7a1aff-7504-4b86-bce1-0248d152de7c',
        program=lambda: None
    )

    print(f'Destroying resources in stack: {stack_name}...')
    stack.destroy(on_output=print)
    print('Resources successfully destroyed.')

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script.py stack_name [destroy]")
        sys.exit(1)

    stack_name = sys.argv[1]

    if len(sys.argv) > 2 and sys.argv[2] == 'destroy':
        destroy_pods(stack_name)
    else:
        deploy_orchestration(stack_name)
  