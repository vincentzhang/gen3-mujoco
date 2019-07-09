#!/usr/bin/env python3
"""
Playground: Run a basic simulation
"""
from mujoco_py import load_model_from_path, MjSim, MjViewer
import os

model = load_model_from_path("models/example.xml")
sim = MjSim(model)

viewer = MjViewer(sim)

t = 0

while True:
    sim.step()
    viewer.render()
    t += 1
    if t > 100 and os.getenv('TESTING') is not None:
        break
