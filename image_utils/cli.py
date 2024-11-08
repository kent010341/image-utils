from typing import Tuple
from .decorators import common_options, image_io_wrapper
from .operators import crop as _crop, resize as _resize, gray_scale as _gray_scale, expand as _expand, roll as _roll
import click

def parse_size(value: str) -> Tuple[int, int]:
    """Parse {w}x{h} format to (width, height)."""
    try:
        width, height = (int(x) if x else None for x in value.split('x'))

        if width is None and height is None:
            raise click.BadParameter("Both width and height cannot be empty (e.g., 100x200, 300x, x400).")

        return width, height
    except ValueError:
        raise click.BadParameter("Size must be in the format {w}x{h} (e.g., 100x200, 300x, x400).")

@click.group()
def cli():
    """A command-line tool for image processing."""
    pass

@cli.command()
@click.argument('size', callback=lambda ctx, param, value: parse_size(value))
@common_options
@image_io_wrapper
def resize(size, input, opaque):
    """Resize an image"""

    return _resize(*size)

@cli.command()
@click.option('--align', type=click.Choice(['top', 'bottom', 'left', 'right', 'center']), default='center', help='Align the cropped image in the square (default: center)')
@common_options
@image_io_wrapper
def crop(input, align, opaque):
    """Crop an image"""

    return _crop(align)

@cli.command()
@common_options
@image_io_wrapper
def gray_scale(input, opaque):
    """Change an image to gray scale"""

    return _gray_scale()

@cli.command()
@click.argument('size', callback=lambda ctx, param, value: parse_size(value))
@click.option(
    '--fillwith', 
    default='#00000000', 
    help='Fill color in HEX format (default: transparent).'
)
@click.option(
    '--align', 
    type=click.Choice(['c', 't', 'b', 'l', 'r', 'lt', 'rt', 'lb', 'rb']), 
    default='c', 
    help='Align the original image on the expanded canvas (default: c).'
)
@click.option(
    '--dx', 
    type=int, 
    default=0, 
    help='Horizontal shift (default: 0).'
)
@click.option(
    '--dy', 
    type=int, 
    default=0, 
    help='Vertical shift (default: 0).'
)
@click.option(
    '--fillwithpos', 
    type=(int, int), 
    default=None, 
    help='Sample the fill color from the given coordinates.'
)
@common_options
@image_io_wrapper
def expand(input, size, fillwith, align, dx, dy, fillwithpos, opaque):
    """Expand the canvas of an image"""

    w, h = size
    return _expand(
        width=w,
        height=h,
        fillwith=fillwith, 
        align=align, 
        dx=dx, 
        dy=dy, 
        fillwithpos=fillwithpos
    )

@cli.command()
@click.argument('shift', type=int)
@click.option(
    '-d', '--direction', 
    type=click.Choice(['l', 'r', 'u', 'b']), 
    default='r', 
    help="Direction of roll ('l' for left, 'r' for right, 'u' for up, 'b' for down). Default is 'r'."
)
@common_options
@image_io_wrapper
def roll(input, shift, direction, opaque):
    """Roll (shift) the image horizontally or vertically"""

    return _roll(shift=shift, direction=direction)

if __name__ == "__main__":
    cli()
