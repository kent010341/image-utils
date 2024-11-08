from PIL import Image
from .image_operator import ImageOperator
from typing import Optional, Tuple

class ResizeOperator(ImageOperator):
    """
    An image operator that resizes the image to the specified width and height.
    If only one dimension is provided, the other is scaled proportionally.
    """

    def __init__(self, width: Optional[int] = None, height: Optional[int] = None):
        if width is None and height is None:
            raise ValueError("At least one of width or height must be specified.")

        self.width = width
        self.height = height

    def __call__(self, image: Image.Image) -> Image.Image:
        """
        Resizes the given image to the specified dimensions.
        
        Parameters:
        image (Image.Image): The image to resize.
        
        Returns:
        Image.Image: The resized image.
        """
        img_width, img_height = image.size
        if self.width and not self.height:
            self.height = int((self.width / img_width) * img_height)
        elif self.height and not self.width:
            self.width = int((self.height / img_height) * img_width)
        return image.resize((self.width, self.height))

    def __repr__(self) -> str:
        """
        Return a string representation of the ResizeOperator.

        Returns:
            str: A string representation of the ResizeOperator.
        """
        return f"ResizeOperator(width='{self.width}, height='{self.height}')"

def resize(width: Optional[int] = None, height: Optional[int] = None) -> ResizeOperator:
    """
    Creates a ResizeOperator with the specified width and height.
    
    Parameters:
    width (Optional[int]): The width to resize to. Can be None.
    height (Optional[int]): The height to resize to. Can be None.
    
    Returns:
    ResizeOperator: The ResizeOperator initialized with the specified dimensions.
    """
    return ResizeOperator(width, height)
