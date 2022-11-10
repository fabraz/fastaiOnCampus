import os
import logging


def inject_env_variable(dir):
    env_vars = os.popen(f'cat {dir}')
    for var in env_vars:
        key, value = var.split('=', 1)
        os.environ[key.rstrip()] = value.rstrip()
    logging.info(f"Done injecting variables from {dir}")
    print(f"Done injecting variables from {dir}")
