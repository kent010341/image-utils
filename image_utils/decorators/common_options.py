import click
from functools import update_wrapper

def common_options(func):
    """
    Decorator to add common command-line options for image processing commands.

    This decorator adds an '--input' option to specify the input image path.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function with the added command-line options.
    """
    @click.option('-i', '--input', type=click.Path(exists=True), help='Input image path')
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return update_wrapper(wrapper, func)
