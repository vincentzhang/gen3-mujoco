#!/usr/bin/env python
"""
Run before using this file:
    export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so:/usr/lib/nvidia-384/libGL.so
"""
import os
import gym
from gym import spaces, envs
import argparse
import numpy as np
import itertools
import time
from builtins import input


class RandomAgent(object):
    """The world's simplest agent!"""
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation, reward, done):
        # if isinstance(self.action_space, spaces.Box):
            # print("action space is a Box")
        return self.action_space.sample()


class NoopAgent(object):
    """The world's simplest agent!"""
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation, reward, done):
        if isinstance(self.action_space, spaces.Box):
            action = np.zeros(self.action_space.shape)
        elif isinstance(self.action_space, spaces.Discrete):
            action = 0
        else:
            raise NotImplementedError("noop not implemented for class {}".format(type(self.action_space)))
        return action

class HumanAgent(object):
    """The world's simplest agent!"""
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation, reward, done):
        raise NotImplementedError("HumanAgent not implemented for class {}".format(type(self.action_space)))
        # action = input("type action from {0,..., %i} and press enter: " % (self.action_space.shape[0]))
        # try:
        #     action = int(action)
        # except ValueError:
        #     print("WARNING: ignoring illegal action '{}'.".format(action))
        #     action = 0

        # if action >= self.action_space.shape[0]:
        #     print("WARNING: ignoring illegal action {}.".format(action))
        #     action = 0
        # return self.action_space.sample()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("env", type=str, help="name of the environment. Options: Gen3-v0")
    parser.add_argument("--mode", choices=["noop", "random", "human"], default="random", help="mode of the agent")
    parser.add_argument("--max_steps", type=int, default=0, help="maximum episode length")
    parser.add_argument("--fps",type=float)
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--ignore_done", action="store_true")
    args = parser.parse_args()

    env = envs.make(args.env)
    action_space = env.action_space
    mode = args.mode
    fps = args.fps or env.metadata.get('video.frames_per_second') or 100
    if args.max_steps == 0: 
        args.max_steps = env.spec.tags['wrapper_config.TimeLimit.max_episode_steps']
        print("max_steps = ", args.max_steps)

    print("Press ESC to quit")
    reward = 0
    done = False
    if mode == "random":
        agent = RandomAgent(action_space)
    elif mode == "noop":
        agent = NoopAgent(action_space)
    elif mode == "human":
        agent = HumanAgent(action_space)

    while True:
        obs = env.reset()
        env.render(mode='human')
        print("Starting a new trajectory")
        for t in range(args.max_steps) if args.max_steps else itertools.count():
            print("\nSTEP #", t)
            done = False
            action = agent.act(obs, reward, done)
            # print(action)
            time.sleep(1.0 / fps)
            obs, reward, done, info = env.step(action)
            print("observation: \n\tobservation:\t", obs['observation'], "\n\tachieved_goal:\t", obs['achieved_goal'], "\n\tdesired_goal:\t", obs['desired_goal'])
            print("reward:", reward)
            print("done:", done)
            print("info:\tis_success:", info['is_success'])
            env.render() # default mode is human
            if done and not args.ignore_done:
                break
        print("Done after {} steps".format(t + 1))
        if args.once or os.getenv('TESTING') is not None:
            break
