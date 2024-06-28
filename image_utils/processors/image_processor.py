from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from typing import Optional
import argparse
import sys

class ImageProcessor:
    """
    A base class for image processing tasks.

    Attributes:
        prog (str): The program name.
        description (str): The description of the program.
        input_image (Optional[Image.Image]): The input image.
        format (Optional[str]): The format of the input image.
    """

    def __init__(self, prog: str, description: str):
        """
        Initialize the ImageProcessor with program name and description.

        Args:
            prog (str): The program name.
            description (str): The description of the program.
        """
        self.prog = prog
        self.description = description
        self.input_image: Optional[Image.Image] = None
        self.format: Optional[str] = None

    def create_parser(self) -> argparse.ArgumentParser:
        """
        Create the argument parser with common arguments.

        Returns:
            argparse.ArgumentParser: The argument parser.
        """
        parser = argparse.ArgumentParser(prog=self.prog, description=self.description)
        parser.add_argument('-i', '--input', type=str, help='Input image path')
        self.add_arguments(parser)
        return parser

    def add_arguments(self, parser: argparse.ArgumentParser):
        """
        Add specific arguments for the image processing task.

        Args:
            parser (argparse.ArgumentParser): The argument parser.
        """
        pass

    def parse_arguments(self, parser: argparse.ArgumentParser):
        """
        Parse the arguments from the command line.

        Args:
            parser (argparse.ArgumentParser): The argument parser.
        """
        self.args = parser.parse_args()

    def load_image(self):
        """
        Load the input image from the specified path or standard input.
        """
        if not sys.stdin.isatty():
            self.input_image = Image.open(sys.stdin.buffer)
            self.format = self.input_image.format
        elif self.args.input:
            self.input_image = Image.open(self.args.input)
            self.format = self.input_image.format
        else:
            Tk().withdraw()  # Hide the root window
            input_path = askopenfilename(title="Select an image to process")
            if not input_path:
                print("No input file provided. Exiting.")
                sys.exit(1)
            self.input_image = Image.open(input_path)
            self.format = self.input_image.format

    def save_image(self, output_image: Image.Image):
        """
        Save the output image to standard output.

        Args:
            output_image (Image.Image): The processed image.
        """
        output_image.save(sys.stdout.buffer, format=self.format)

    def process(self) -> Image.Image:
        """
        Process the input image. This method should be overridden by subclasses.

        Returns:
            Image.Image: The processed image.

        Raises:
            NotImplementedError: If the method is not overridden by a subclass.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def run(self):
        """
        Run the image processing task.
        """
        parser = self.create_parser()
        self.parse_arguments(parser)
        self.load_image()
        output_image = self.process()
        self.save_image(output_image)
