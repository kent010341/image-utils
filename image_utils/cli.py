from . import pipe
from .decorators import common_options
from .operators import crop as _crop, resize_with_pattern
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import click
import sys

@click.group()
def cli():
    """A command-line tool for image processing."""
    pass

@cli.command()
@click.argument('size')
@common_options
def resize(size, input):
    """Resize an image"""

    image = fetch_image(input_path=input)
    pipeline = pipe(resize_with_pattern(size))

    pipeline.process(image).save(sys.stdout.buffer, format=image.format)

@cli.command()
@click.option('--align', type=click.Choice(['top', 'bottom', 'left', 'right', 'center']), default='center', help='Align the cropped image in the square (default: center)')
@common_options
def crop(input, align):
    """Crop an image"""

    image = fetch_image(input_path=input)
    pipeline = pipe(_crop(align))

    pipeline.process(image).save(sys.stdout.buffer, format=image.format)

def fetch_image(input_path: str) -> Image.Image:
    # Load the input image from the provided path, stdin, or a file dialog
    if input_path:
        input_image = Image.open(input_path)
    else:
        if not sys.stdin.isatty():
            input_image = Image.open(sys.stdin.buffer)
        else:
            Tk().withdraw()
            input_path = askopenfilename(title="Select an image to process")
            if not input_path:
                print("No input file provided. Exiting.")
                sys.exit(1)
            input_image = Image.open(input_path)
    
    return input_image

if __name__ == "__main__":
    cli()
