# gen3-mujoco
Mujoco model of the Kinova Gen3 robot

## Update:
There're some issues with the implementations here. Please use the [mujoco_menagerie](https://github.com/google-deepmind/mujoco_menagerie/tree/main/kinova_gen3) repo. 

## To checkout the repo with the gym submodule:
```
    git clone --recursive git@github.com:vincentzhang/gen3-mujoco.git
    cd gym
    pip3 install -e '.[all]'
```

## If you have already cloned the repo and only want to add the submodule, then do:
```
    git submodule update --init --recursive
    cd gym
    pip3 install -e '.[all]'
```

## Examples:
```
    # Display the environment in mujoco
    python gen3.py
    # Run random agent through openai gym
    LD_PRELOAD="" python realtime_sim.py
```
