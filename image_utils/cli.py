from .decorators import common_options, image_io_wrapper
from .operators import crop as _crop, resize_with_pattern, gray_scale as _gray_scale, watermark as _watermark
import click

@click.group()
def cli():
    """A command-line tool for image processing."""
    pass

@cli.command()
@click.argument('size')
@common_options
@image_io_wrapper
def resize(size, input, opaque):
    """Resize an image"""

    return resize_with_pattern(size)

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
@click.option('--text', required=True, help='The watermark text to be added to the image')
@click.option('--color', default='FFFFFF', help='The color of the watermark text in hex (default: FFFFFF)')
@click.option('--opacity', default=30, type=int, help='The opacity level of the watermark text (default: 30)')
@click.option('--angle', default='0', help='The angle at which the watermark text is placed. Use "diagonal" for auto-calculated diagonal placement.')
@click.option('--font-size', default=None, type=int, help='The font size of the watermark text (default: auto)')
@common_options
@image_io_wrapper
def watermark(input, opaque, text, color, opacity, angle, font_size):
    """Add a watermark to an image"""
    return _watermark(text, color, opacity, angle, font_size)

if __name__ == "__main__":
    cli()
