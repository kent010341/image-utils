import click
from .processors.resize_image_processor import ResizeImageProcessor
from .processors.crop_image_processor import CropImageProcessor
from .decorators import common_options

@click.group()
def cli():
    """A command-line tool for image processing."""
    pass

@cli.command()
@click.argument('size')
@common_options
def resize(size, input):
    """Resize an image"""
    processor = ResizeImageProcessor(size=size, input_path=input)
    processor.run()

@cli.command()
@click.option('--align', '-a', type=click.Choice(['top', 'bottom', 'left', 'right', 'center']), default='center', help='Align the cropped image in the square (default: center)')
@common_options
def crop(input, align):
    """Crop an image"""
    processor = CropImageProcessor(input_path=input, align=align)
    processor.run()

if __name__ == "__main__":
    cli()
