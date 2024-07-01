from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from typing import Optional
import sys

class ImageProcessor:
    """
    A base class for image processing tasks.

    Attributes:
        input_path (Optional[str]): The input image path.
        input_image (Optional[Image.Image]): The input image.
        format (Optional[str]): The format of the input image.
    """

    def __init__(self, input_path: Optional[str] = None):
        """
        Initialize the ImageProcessor.

        Args:
            input_path (Optional[str]): The input image path.
        """
        self.input_path = input_path
        self.input_image: Optional[Image.Image] = None
        self.format: Optional[str] = None

    def load_image(self):
        """
        Load the input image from the specified path or standard input.
        """
        if not sys.stdin.isatty():
            self.input_image = Image.open(sys.stdin.buffer)
            self.format = self.input_image.format
        elif self.input_path:
            self.input_image = Image.open(self.input_path)
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
        self.load_image()
        output_image = self.process()
        self.save_image(output_image)
