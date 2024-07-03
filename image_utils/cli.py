import click
from image_utils.decorators import common_options, handle_image_io
from image_utils.operators import crop, resize_with_pattern

@click.group()
def cli():
    """A command-line tool for image processing."""
    pass

@cli.command()
@click.argument('size')
@common_options
@handle_image_io(resize_with_pattern, 'size')
def resize_image(size, input):
    """Resize an image"""
    pass

@cli.command()
@click.option('--align', type=click.Choice(['top', 'bottom', 'left', 'right', 'center']), default='center', help='Align the cropped image in the square (default: center)')
@common_options
@handle_image_io(crop, 'align')
def crop_image(input, align):
    """Crop an image"""
    pass

if __name__ == "__main__":
    cli()
