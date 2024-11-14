from PIL import Image
from .image_operator import ImageOperator

class FlipOperator(ImageOperator):
    """
    An image processing operator to flip the image in a specified direction.

    Attributes:
        direction (str): Direction to flip the image ('h' for horizontal, 'v' for vertical).

    Methods:
        __call__(image: Image.Image) -> Image.Image:
            Flip the image and return the processed image.
    """

    def __init__(self, direction: str):
        self.direction = direction.lower()
        if self.direction not in ('h', 'v'):
            raise ValueError("Direction must be 'h' for horizontal or 'v' for vertical.")

    def __call__(self, image: Image.Image) -> Image.Image:
        """Flip the image in the specified direction."""
        if self.direction == 'h':
            return image.transpose(Image.FLIP_LEFT_RIGHT)
        elif self.direction == 'v':
            return image.transpose(Image.FLIP_TOP_BOTTOM)

    def __repr__(self) -> str:
        """Return a string representation of the FlipOperator."""
        return f"FlipOperator(direction='{self.direction}')"

def flip(direction: str) -> FlipOperator:
    """
    Create a FlipOperator with the specified direction.

    Parameters:
    direction (str): Direction to flip the image ('h' for horizontal, 'v' for vertical).

    Returns:
    FlipOperator: An instance of FlipOperator.
    """
    return FlipOperator(direction)
