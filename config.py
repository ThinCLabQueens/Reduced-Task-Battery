import yaml

default_config = {
    "randomize_task": True,
    "num_task_in_subset": 3,
}

with open("config.yaml", "w") as f:
    yaml.dump(default_config, f)
