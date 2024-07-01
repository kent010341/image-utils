import click
from functools import update_wrapper

def common_options(func):
    @click.option('-i', '--input', type=click.Path(exists=True), help='Input image path')
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return update_wrapper(wrapper, func)
