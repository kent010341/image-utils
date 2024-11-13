from PIL import Image
from typing import Union
from .image_operator import ImageOperator

class CropOperator(ImageOperator):
    """
    An image processing operator to crop an image to a specified rectangular area with optional boundaries.

    Attributes:
        left (Union[int, float]): The left boundary for cropping. 
                                  If float, interpreted as a percentage of image width (0.0 to 1.0).
                                  Default is 0 (left edge).
        top (Union[int, float]): The top boundary for cropping.
                                 If float, interpreted as a percentage of image height (0.0 to 1.0).
                                 Default is 0 (top edge).
        right (Union[int, float]): The right boundary for cropping.
                                   If float, interpreted as a percentage of image width (0.0 to 1.0).
                                   Default is image width (right edge).
        bottom (Union[int, float]): The bottom boundary for cropping.
                                    If float, interpreted as a percentage of image height (0.0 to 1.0).
                                    Default is image height (bottom edge).

    Methods:
        __call__(image: Image.Image) -> Image.Image:
            Crop the input image to the specified boundaries and return the processed image.
    """
    def __init__(self, left: Union[int, float] = 0, top: Union[int, float] = 0,
                 right: Union[int, float] = 1.0, bottom: Union[int, float] = 1.0):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def __call__(self, image: Image.Image) -> Image.Image:
        """
        Crop the input image to the specified boundaries.

        Args:
            image (Image.Image): The input image to be processed.

        Returns:
            Image.Image: The cropped image.
        """
        width, height = image.size

        # Convert float boundaries to pixel values if necessary
        left = int(self.left * width) if isinstance(self.left, float) else self.left
        top = int(self.top * height) if isinstance(self.top, float) else self.top
        right = int(self.right * width) if isinstance(self.right, float) else self.right
        bottom = int(self.bottom * height) if isinstance(self.bottom, float) else self.bottom

        # Ensure boundaries are within image dimensions
        left = max(0, min(left, width))
        top = max(0, min(top, height))
        right = max(left, min(right, width))
        bottom = max(top, min(bottom, height))

        # Crop to the specified rectangle
        cropped_image = image.crop((left, top, right, bottom))
        return cropped_image

    def __repr__(self) -> str:
        """
        Return a string representation of the CropOperator.

        Returns:
            str: A string representation of the CropOperator.
        """
        return (f"CropOperator(left={self.left}, top={self.top}, "
                f"right={self.right}, bottom={self.bottom})")

def crop(left: Union[int, float] = 0, top: Union[int, float] = 0, 
         right: Union[int, float] = 1.0, bottom: Union[int, float] = 1.0) -> CropOperator:
    """
    Create a CropOperator instance with the specified boundaries.

    Args:
        left (Union[int, float]): The left boundary for cropping. Default is 0.
        top (Union[int, float]): The top boundary for cropping. Default is 0.
        right (Union[int, float]): The right boundary for cropping. Default is 1.0.
        bottom (Union[int, float]): The bottom boundary for cropping. Default is 1.0.

    Returns:
        CropOperator: An instance of CropOperator.
    """
    return CropOperator(left=left, top=top, right=right, bottom=bottom)
