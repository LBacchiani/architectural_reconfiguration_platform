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

    
        
    
    image_2c06260e_9112_41aa_b5d8_14f2329e7530_name = create_pod_name('image-2c06260e-9112-41aa-b5d8-14f2329e7530', stack)

    image_2c06260e_9112_41aa_b5d8_14f2329e7530 = k8s.core.v1.Pod(image_2c06260e_9112_41aa_b5d8_14f2329e7530_name,
        metadata=k8s.meta.v1.ObjectMetaArgs(
            name=image_2c06260e_9112_41aa_b5d8_14f2329e7530_name,
            labels={
                
                **{'type': 'image-type'},
                
                'stack': stack,
                'original_service': 'image-2c06260e-9112-41aa-b5d8-14f2329e7530'
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
    
        
    
    image_b15f0d6a_64f9_4158_901a_3b90b0976271_name = create_pod_name('image-b15f0d6a-64f9-4158-901a-3b90b0976271', stack)

    image_b15f0d6a_64f9_4158_901a_3b90b0976271 = k8s.core.v1.Pod(image_b15f0d6a_64f9_4158_901a_3b90b0976271_name,
        metadata=k8s.meta.v1.ObjectMetaArgs(
            name=image_b15f0d6a_64f9_4158_901a_3b90b0976271_name,
            labels={
                
                **{'type': 'image-type'},
                
                'stack': stack,
                'original_service': 'image-b15f0d6a-64f9-4158-901a-3b90b0976271'
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
    
        
    
    persistence_44cca5ca_32f2_4a14_8087_d7c304c9eee1_name = create_pod_name('persistence-44cca5ca-32f2-4a14-8087-d7c304c9eee1', stack)

    persistence_44cca5ca_32f2_4a14_8087_d7c304c9eee1 = k8s.core.v1.Pod(persistence_44cca5ca_32f2_4a14_8087_d7c304c9eee1_name,
        metadata=k8s.meta.v1.ObjectMetaArgs(
            name=persistence_44cca5ca_32f2_4a14_8087_d7c304c9eee1_name,
            labels={
                
                **{'type': 'persistence-type'},
                
                'stack': stack,
                'original_service': 'persistence-44cca5ca-32f2-4a14-8087-d7c304c9eee1'
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
    
        
    
    webui_a01b49c8_2a2c_4c8d_927f_01d97841687e_name = create_pod_name('webui-a01b49c8-2a2c-4c8d-927f-01d97841687e', stack)

    webui_a01b49c8_2a2c_4c8d_927f_01d97841687e = k8s.core.v1.Pod(webui_a01b49c8_2a2c_4c8d_927f_01d97841687e_name,
        metadata=k8s.meta.v1.ObjectMetaArgs(
            name=webui_a01b49c8_2a2c_4c8d_927f_01d97841687e_name,
            labels={
                
                **{'type': 'webui-type'},
                
                'stack': stack,
                'original_service': 'webui-a01b49c8-2a2c-4c8d-927f-01d97841687e'
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
    
        
    
    webui_8668eca2_61de_486f_9734_ba22fede54c9_name = create_pod_name('webui-8668eca2-61de-486f-9734-ba22fede54c9', stack)

    webui_8668eca2_61de_486f_9734_ba22fede54c9 = k8s.core.v1.Pod(webui_8668eca2_61de_486f_9734_ba22fede54c9_name,
        metadata=k8s.meta.v1.ObjectMetaArgs(
            name=webui_8668eca2_61de_486f_9734_ba22fede54c9_name,
            labels={
                
                **{'type': 'webui-type'},
                
                'stack': stack,
                'original_service': 'webui-8668eca2-61de-486f-9734-ba22fede54c9'
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
    
        
    
    auth_7465b705_e72d_4960_a212_35d3cef69be6_name = create_pod_name('auth-7465b705-e72d-4960-a212-35d3cef69be6', stack)

    auth_7465b705_e72d_4960_a212_35d3cef69be6 = k8s.core.v1.Pod(auth_7465b705_e72d_4960_a212_35d3cef69be6_name,
        metadata=k8s.meta.v1.ObjectMetaArgs(
            name=auth_7465b705_e72d_4960_a212_35d3cef69be6_name,
            labels={
                
                **{'type': 'auth-type'},
                
                'stack': stack,
                'original_service': 'auth-7465b705-e72d-4960-a212-35d3cef69be6'
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
    
        
    pulumi.export('image-2c06260e-9112-41aa-b5d8-14f2329e7530_name', image_2c06260e_9112_41aa_b5d8_14f2329e7530.metadata['name'])
        
    pulumi.export('image-b15f0d6a-64f9-4158-901a-3b90b0976271_name', image_b15f0d6a_64f9_4158_901a_3b90b0976271.metadata['name'])
        
    pulumi.export('persistence-44cca5ca-32f2-4a14-8087-d7c304c9eee1_name', persistence_44cca5ca_32f2_4a14_8087_d7c304c9eee1.metadata['name'])
        
    pulumi.export('webui-a01b49c8-2a2c-4c8d-927f-01d97841687e_name', webui_a01b49c8_2a2c_4c8d_927f_01d97841687e.metadata['name'])
        
    pulumi.export('webui-8668eca2-61de-486f-9734-ba22fede54c9_name', webui_8668eca2_61de_486f_9734_ba22fede54c9.metadata['name'])
        
    pulumi.export('auth-7465b705-e72d-4960-a212-35d3cef69be6_name', auth_7465b705_e72d_4960_a212_35d3cef69be6.metadata['name'])
        
    

def deploy_orchestration(stack_name):
    stack = auto.create_or_select_stack(
        stack_name=stack_name,
        project_name='pulumi-k8s-increase-6f2868f0-d5f9-4756-b47f-4684ca975d85',
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
    
        
    print(f"Pod image-2c06260e-9112-41aa-b5d8-14f2329e7530 Name: {up_res.outputs['image-2c06260e-9112-41aa-b5d8-14f2329e7530_name'].value}")
        
    print(f"Pod image-b15f0d6a-64f9-4158-901a-3b90b0976271 Name: {up_res.outputs['image-b15f0d6a-64f9-4158-901a-3b90b0976271_name'].value}")
        
    print(f"Pod persistence-44cca5ca-32f2-4a14-8087-d7c304c9eee1 Name: {up_res.outputs['persistence-44cca5ca-32f2-4a14-8087-d7c304c9eee1_name'].value}")
        
    print(f"Pod webui-a01b49c8-2a2c-4c8d-927f-01d97841687e Name: {up_res.outputs['webui-a01b49c8-2a2c-4c8d-927f-01d97841687e_name'].value}")
        
    print(f"Pod webui-8668eca2-61de-486f-9734-ba22fede54c9 Name: {up_res.outputs['webui-8668eca2-61de-486f-9734-ba22fede54c9_name'].value}")
        
    print(f"Pod auth-7465b705-e72d-4960-a212-35d3cef69be6 Name: {up_res.outputs['auth-7465b705-e72d-4960-a212-35d3cef69be6_name'].value}")
        
    

def destroy_pods(stack_name):
    stack = auto.create_or_select_stack(
        stack_name=stack_name,
        project_name='pulumi-k8s-increase-6f2868f0-d5f9-4756-b47f-4684ca975d85',
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
  