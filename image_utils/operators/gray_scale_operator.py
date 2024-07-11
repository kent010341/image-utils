from PIL import Image
from .image_operator import ImageOperator

class GrayScaleOperator(ImageOperator):
    """
    An image processing operator to convert an image to grayscale.

    Methods:
        __call__(image: Image.Image) -> Image.Image:
            Convert the input image to grayscale and return the processed image.
    """
    def __call__(self, image: Image.Image) -> Image.Image:
        """
        Convert the input image to grayscale.

        Args:
            image (Image.Image): The input image to be processed.

        Returns:
            Image.Image: The grayscale image.
        """
        return image.convert('L').convert('RGBA')

    def __repr__(self) -> str:
        """
        Return a string representation of the GrayScaleOperator.

        Returns:
            str: A string representation of the GrayScaleOperator.
        """
        return "GrayScaleOperator()"

def gray_scale() -> GrayScaleOperator:
    """
    Create a GrayScaleOperator instance.

    Returns:
        GrayScaleOperator: An instance of GrayScaleOperator.
    """
    return GrayScaleOperator()
