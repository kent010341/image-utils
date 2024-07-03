from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import sys
from image_utils.operators.image_operator import ImageOperator
from typing import Type, Any

def handle_image_io(operator_cls: Type[ImageOperator], *op_args: Any, **op_kwargs: Any):
    """
    Decorator to handle image input/output and apply an image operator.

    This decorator handles loading the input image from a file path, stdin, or a file dialog,
    then applies the provided image operator to the image, and finally saves the processed
    image to stdout.

    Args:
        operator_cls (Type[ImageOperator]): A class that inherits from ImageOperator and processes an image.
        *op_args: Positional arguments to instantiate the operator.
        **op_kwargs: Keyword arguments to instantiate the operator.

    Returns:
        Callable: A decorator function for processing images.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            input_path = kwargs.get('input')
            
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
            
            # Create the operator instance and process the image
            operator_instance = operator_cls(*op_args, **op_kwargs)
            output_image = operator_instance(input_image)
            
            # Save the processed image to stdout
            output_image.save(sys.stdout.buffer, format=input_image.format)
        
        return wrapper
    return decorator
