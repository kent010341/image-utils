from .image_processor import ImageProcessor
from PIL import Image
import argparse

class CropImageProcessor(ImageProcessor):
    """
    A class for cropping an image to its bounding box and converting it to a square.

    Inherits from ImageProcessor.
    """

    def __init__(self):
        """
        Initialize the CropImageProcessor with specific program name and description.
        """
        super().__init__(prog='crop', description='Automatically crop an image to its bounding box and convert it to a square.')

    def add_arguments(self, parser: argparse.ArgumentParser):
        """
        Add specific arguments for cropping the image.

        Args:
            parser (argparse.ArgumentParser): The argument parser.
        """
        parser.add_argument('--align', '-a', type=str, choices=['top', 'bottom', 'left', 'right', 'center'], default='center', help='Align the cropped image in the square (default: center)')

    def process(self) -> Image.Image:
        """
        Crop the input image to its bounding box and convert it to a square.

        Returns:
            Image.Image: The cropped and squared image.
        """
        bbox = self.input_image.getbbox()
        if bbox:
            cropped_image = self.input_image.crop(bbox)
            cropped_width, cropped_height = cropped_image.size

            # Determine the size of the square
            max_side = max(cropped_width, cropped_height)
            
            # Create a new square image with a transparent background
            square_image = Image.new("RGBA", (max_side, max_side), (0, 0, 0, 0))
            
            # Calculate position to paste the cropped image based on alignment
            if self.args.align == 'top':
                paste_x = (max_side - cropped_width) // 2
                paste_y = 0
            elif self.args.align == 'bottom':
                paste_x = (max_side - cropped_width) // 2
                paste_y = max_side - cropped_height
            elif self.args.align == 'left':
                paste_x = 0
                paste_y = (max_side - cropped_height) // 2
            elif self.args.align == 'right':
                paste_x = max_side - cropped_width
                paste_y = (max_side - cropped_height) // 2
            else:  # center
                paste_x = (max_side - cropped_width) // 2
                paste_y = (max_side - cropped_height) // 2
            
            square_image.paste(cropped_image, (paste_x, paste_y))
        else:
            # If the image is completely transparent, create a 1x1 transparent square
            square_image = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
        
        return square_image
