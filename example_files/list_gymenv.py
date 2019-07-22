from gym import envs

# list all environments
print([env.id for env in envs.registry.all()])
#[env.id for env in envs.registry.all() if "Fetch" in env.id]
