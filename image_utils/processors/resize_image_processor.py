from .image_processor import ImageProcessor
from PIL import Image
from typing import Tuple, Optional
import argparse

class ResizeImageProcessor(ImageProcessor):
    """
    A class for resizing an image.

    Inherits from ImageProcessor.
    """

    def __init__(self):
        """
        Initialize the ResizeImageProcessor with specific program name and description.
        """
        super().__init__(prog='resize', description='Resize an image.')

    def add_arguments(self, parser: argparse.ArgumentParser):
        """
        Add specific arguments for resizing the image.

        Args:
            parser (argparse.ArgumentParser): The argument parser.
        """
        parser.add_argument('size', type=str, help='Size in the format <width>x<height>, <width>x, or x<height>')

    def parse_size(self, size_str: str) -> Tuple[Optional[int], Optional[int]]:
        """
        Parse the size argument into width and height.

        Args:
            size_str (str): The size string in the format <width>x<height>, <width>x, or x<height>.

        Returns:
            Tuple[Optional[int], Optional[int]]: The width and height.

        Raises:
            ValueError: If the size string is not in the correct format.
        """
        if 'x' not in size_str:
            raise ValueError("Size must be in the format <width>x<height>, <width>x, or x<height>")
        width_str, height_str = size_str.split('x')
        width = int(width_str) if width_str else None
        height = int(height_str) if height_str else None
        return width, height

    def process(self) -> Image.Image:
        """
        Resize the input image.

        Returns:
            Image.Image: The resized image.
        """
        width, height = self.parse_size(self.args.size)
        img_width, img_height = self.input_image.size
        if width and not height:
            height = int((width / img_width) * img_height)
        elif height and not width:
            width = int((height / img_height) * img_width)
        return self.input_image.resize((width, height))
