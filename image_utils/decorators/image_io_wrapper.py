from ..pipeline import pipe
from functools import wraps
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import sys

def image_io_wrapper(command_func):
    """
    Decorator to handle image input and output for CLI commands.

    This decorator fetches the input image from a specified path, standard input,
    or a file dialog, processes it using the decorated command function, and
    saves the output to standard output.

    Args:
        command_func (Callable): The command function to be decorated.

    Returns:
        Callable: The decorated function with image I/O handling.
    """
    @wraps(command_func)
    def wrapper(*args, **kwargs):
        # Get the input path and opaque flag from the keyword arguments
        input_path = kwargs.get('input')
        opaque = kwargs.get('opaque', False)
        # Fetch the input image based on the input path
        image = _fetch_image(input_path=input_path)
        # Execute the command function with the provided arguments
        pipeline = pipe(command_func(*args, **kwargs))
        # Process the image
        output_image = pipeline(image)
        # Convert the image to an opaque format if needed
        if opaque and output_image.mode in ('RGBA', 'LA'):
            output_image = output_image.convert('RGB')
        # Save the output to standard output
        output_image.save(sys.stdout.buffer, format=image.format)
    return wrapper

def _fetch_image(input_path: str) -> Image.Image:
    """
    Fetch the input image from the specified path, standard input, or a file dialog.

    Args:
        input_path (str): The path to the input image.

    Returns:
        Image.Image: The loaded image.
    """
    if input_path:
        # Load the image from the specified file path
        return Image.open(input_path)
    if not sys.stdin.isatty():
        # Load the image from standard input if provided
        return Image.open(sys.stdin.buffer)
    # Open a file dialog to select the image file
    Tk().withdraw()
    input_path = askopenfilename(title="Select an image to process")
    if not input_path:
        # Exit if no input file is provided
        print("No input file provided. Exiting.")
        sys.exit(1)
    return Image.open(input_path)
