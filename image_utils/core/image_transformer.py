from typing import Protocol
from PIL import Image

class ImageTransformer(Protocol):
    """
    A generic interface for objects or functions that transform an image.

    Any object implementing this interface should accept a PIL Image and return a transformed Image.
    This protocol enables interoperability between standalone functions, operator classes,
    and composed pipelines.
    """
    def __call__(self, image: Image.Image) -> Image.Image:
        """
        Transform the given image and return the result.

        Args:
            image (Image.Image): The input image.

        Returns:
            Image.Image: The transformed image.
        """
        ...
