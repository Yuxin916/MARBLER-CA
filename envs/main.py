import argparse

from demoPCPAgents import *
from pcpAgents import *

def create_parser():
    parser = argparse.ArgumentParser(description='PCPAgents tester')
    # predator arguments
    parser.add_argument('-predator', type=int, default=2)
    parser.add_argument('-predator_radius', type=float, default = .9)
    parser.add_argument('-predator_reward', type=float, default = -0.05)
    # capture arguments
    parser.add_argument('-capture', type=int, default=2)
    parser.add_argument('-capture_radius', type=float, default = .5)
    parser.add_argument('-capture_reward', type=float, default = -0.05)
    # environment
    parser.add_argument('-show_figure', type=bool, default=True)
    parser.add_argument('-real_time', type=bool, default= False)
    parser.add_argument('-max_episode_steps', type=int, default = 1000)

    return parser

if __name__ == "__main__":
    warnings.filterwarnings(action='ignore', category=DeprecationWarning)

    args = create_parser().parse_args()

    predatorPolicy = DemoPredatorAgent()
    capturePolicy = DemoCaptureAgent()
    policies = []
    for i in range(args.predator):
        policies.append(predatorPolicy)
    for i in range(args.capture):
        policies.append(capturePolicy)
    agents = PCPAgents(args, policies)
    agents.run_episode()