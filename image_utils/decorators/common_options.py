import click
from functools import update_wrapper

def common_options(func):
    """
    Decorator to add common command-line options for image processing commands.

    This decorator adds '--input' and '--opaque' options to specify the input image path
    and whether to convert the output image to an opaque format.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function with the added command-line options.
    """
    @click.option('-i', '--input', type=click.Path(exists=True), help='Input image path')
    @click.option('--opaque', is_flag=True, help='Convert the output image to an opaque format (RGB)')
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return update_wrapper(wrapper, func)
