from gym.envs.registration import register
import os

_particles = {
    "PredatorCapturePrey": "PredatorCapturePrey-v0",
    "PredatorCapturePreyGNN": "PredatorCapturePreyGNN-v0",
    "Warehouse": "Warehouse-v0",
    "Simple": "Simple-v0",
    "ArcticTransport": "ArcticTransport-v0",
    "MaterialTransport": "MaterialTransport-v0",
    "MaterialTransportGNN": "MaterialTransportGNN-v0",
    "HeterogeneousSensorNetwork": "HeterogeneousSensorNetwork-v0"
}

for scenario_name, gymkey in _particles.items():
    # 把所有scenarios的名称都注册了
    module_dir = os.path.join(os.path.dirname(__file__), 'scenarios/'+scenario_name)
    config_path = os.path.join(module_dir, 'config.yaml')

    # Registers multi-agent particle environments:
    register(
        gymkey,
        entry_point=f"robotarium_gym.wrapper:Wrapper",
        kwargs={'env_name': scenario_name,
                'config_path': config_path},
    )
    pass
pass