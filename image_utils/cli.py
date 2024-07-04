from .decorators import common_options, image_io_wrapper
from .operators import crop as _crop, resize_with_pattern
import click

@click.group()
def cli():
    """A command-line tool for image processing."""
    pass

@cli.command()
@click.argument('size')
@common_options
@image_io_wrapper
def resize(size, input):
    """Resize an image"""

    return resize_with_pattern(size)

@cli.command()
@click.option('--align', type=click.Choice(['top', 'bottom', 'left', 'right', 'center']), default='center', help='Align the cropped image in the square (default: center)')
@common_options
@image_io_wrapper
def crop(input, align):
    """Crop an image"""

    return _crop(align)

if __name__ == "__main__":
    cli()
