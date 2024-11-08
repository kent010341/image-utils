from PIL import Image
from typing import Optional
from .image_operator import ImageOperator

class RollOperator(ImageOperator):
    """
    An image processing operator to roll the image in a specified direction.

    Attributes:
        shift (int): Number of pixels to shift.
        direction (str): Direction to roll the image ('l' for left, 'r' for right, 'u' for up, 'b' for bottom).

    Methods:
        __call__(image: Image.Image) -> Image.Image:
            Roll the image and return the processed image.
    """

    def __init__(self, shift: int, direction: str = 'r'):
        self.shift = shift
        self.direction = direction.lower()
        if self.direction not in ('l', 'r', 'u', 'b'):
            raise ValueError("Direction must be one of 'l', 'r', 'u', 'b'.")

    def __call__(self, image: Image.Image) -> Image.Image:
        """Roll the image in the specified direction by the given shift amount."""
        original_width, original_height = image.size
        rolled_image = Image.new("RGBA", (original_width, original_height))

        if self.direction == 'r':  # Roll right
            left_part = image.crop((0, 0, original_width - self.shift, original_height))
            right_part = image.crop((original_width - self.shift, 0, original_width, original_height))
            rolled_image.paste(right_part, (0, 0))
            rolled_image.paste(left_part, (self.shift, 0))
        
        elif self.direction == 'l':  # Roll left
            left_part = image.crop((0, 0, self.shift, original_height))
            right_part = image.crop((self.shift, 0, original_width, original_height))
            rolled_image.paste(right_part, (0, 0))
            rolled_image.paste(left_part, (original_width - self.shift, 0))
        
        elif self.direction == 'u':  # Roll up
            top_part = image.crop((0, 0, original_width, self.shift))
            bottom_part = image.crop((0, self.shift, original_width, original_height))
            rolled_image.paste(bottom_part, (0, 0))
            rolled_image.paste(top_part, (0, original_height - self.shift))
        
        elif self.direction == 'b':  # Roll down
            top_part = image.crop((0, 0, original_width, original_height - self.shift))
            bottom_part = image.crop((0, original_height - self.shift, original_width, original_height))
            rolled_image.paste(bottom_part, (0, 0))
            rolled_image.paste(top_part, (0, self.shift))

        return rolled_image

def roll(shift: int, direction: str = 'r') -> RollOperator:
    """Create a RollOperator instance with the specified shift and direction."""
    return RollOperator(shift, direction)
