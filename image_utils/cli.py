from importlib.metadata import version, PackageNotFoundError
from typing import Tuple, Union
from .decorators import common_options, image_io_wrapper
from . import operators
import click

# Fetch installed image-utils-package
try:
    package_version = version("image-utils-package")
except PackageNotFoundError:
    # default
    package_version = "0.0.0"

def parse_size(value: str) -> Tuple[int, int]:
    """Parse {w}x{h} format to (width, height)."""
    try:
        width, height = (int(x) if x else None for x in value.split('x'))

        if width is None and height is None:
            raise click.BadParameter("Both width and height cannot be empty (e.g., 100x200, 300x, x400).")

        return width, height
    except ValueError:
        raise click.BadParameter("Size must be in the format {w}x{h} (e.g., 100x200, 300x, x400).")


def parse_boundary(value: str) -> Union[int, float]:
    """
    Parse the boundary value, which may be a pixel (int) or a proportion (str ending with 'x').

    Raises:
        ValueError: If a proportion exceeds 1.0.
    """
    if isinstance(value, str) and value.endswith('x'):
        proportion = float(value[:-1])
        if proportion > 1.0:
            raise ValueError(f"Proportion '{value}' exceeds maximum allowable limit of 1.0 (100%).")
        return proportion
    return int(value)

@click.group()
@click.version_option(package_version, '-v', '--version', message='%(version)s')
def cli():
    """A command-line tool for image processing."""
    pass

@cli.command()
@click.argument('size', callback=lambda ctx, param, value: parse_size(value))
@common_options
@image_io_wrapper
def resize(size, input, opaque):
    """Resize an image"""

    return operators.resize(*size)

@cli.command()
@click.option('-l', '--left', default="0", help='Left boundary for cropping. Use a number (pixels) or a proportion (e.g., 0.9x for 90%).')
@click.option('-t', '--top', default="0", help='Top boundary for cropping. Use a number (pixels) or a proportion (e.g., 0.9x for 90%).')
@click.option('-r', '--right', default="1.0x", help='Right boundary for cropping. Use a number (pixels) or a proportion (e.g., 1.0x for 100%).')
@click.option('-b', '--bottom', default="1.0x", help='Bottom boundary for cropping. Use a number (pixels) or a proportion (e.g., 1.0x for 100%).')
@common_options
@image_io_wrapper
def crop(input, left, top, right, bottom, opaque):
    """Crop an image to specified boundaries."""
    
    try:
        left = parse_boundary(left)
        top = parse_boundary(top)
        right = parse_boundary(right)
        bottom = parse_boundary(bottom)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        return

    return operators.crop(left=left, top=top, right=right, bottom=bottom)


@cli.command()
@common_options
@image_io_wrapper
def gray_scale(input, opaque):
    """Change an image to gray scale"""

    return operators.gray_scale()

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
    return operators.expand(
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

    return operators.roll(shift=shift, direction=direction)

@cli.command()
@common_options
@image_io_wrapper
def trim(input, opaque):
    """Trim transparent borders from an image"""
    
    return operators.trim()

@cli.command()
@click.argument('direction', type=click.Choice(['h', 'v']))
@common_options
@image_io_wrapper
def flip(input, direction, opaque):
    """Flip the image horizontally or vertically"""

    return operators.flip(direction=direction)

@cli.command()
@click.argument('angle', type=float)
@click.option(
    '--fillwith', 
    default='#00000000', 
    help='Fill color in HEX format (default: transparent).'
)
@click.option(
    '--fillwithpos', 
    type=(int, int), 
    default=None, 
    help='Sample the fill color from the given coordinates.'
)
@common_options
@image_io_wrapper
def rotate(input, angle, fillwith, fillwithpos, opaque):
    """Rotate the image by a specified angle with expanded canvas"""

    return operators.rotate(
        angle=angle,
        fillwith=fillwith, 
        fillwithpos=fillwithpos
    )

if __name__ == "__main__":
    cli()
