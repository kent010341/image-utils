from PIL import Image
from typing import Callable
from ..core.image_transformer import ImageTransformer
from .image_operator import ImageOperator

class ConcatMapOperator(ImageOperator):
    """
    An image operator that dynamically applies a transformer based on the input image.

    It mimics the behavior of RxJS's concatMap: for each image, it evaluates a mapping function
    that returns an ImageTransformer, which is then applied to the image.

    Example:
        concat_map(lambda img: resize(width=256) if img.width > img.height else resize(height=256))
    """

    def __init__(self, fn: Callable[[Image.Image], ImageTransformer]):
        """
        Initialize with a mapping function.

        Args:
            fn (Callable): A function that takes an image and returns an ImageTransformer.
        """
        self.fn = fn

    def __call__(self, image: Image.Image) -> Image.Image:
        """
        Apply the transformer generated by the mapping function to the image.

        Args:
            image (Image.Image): The image to be transformed.

        Returns:
            Image.Image: The result of applying the dynamically selected transformer.
        """
        transformer = self.fn(image)
        return transformer(image)

    def __repr__(self) -> str:
        """
        Return a string representation of the operator.

        Returns:
            str: A simple descriptor.
        """
        return "ConcatMapOperator(<dynamic>)"

def concat_map(fn: Callable[[Image.Image], ImageTransformer]) -> ConcatMapOperator:
    """
    Factory function for creating a ConcatMapOperator.

    Args:
        fn (Callable): A function that returns an ImageTransformer based on input image.

    Returns:
        ConcatMapOperator: The constructed operator.
    """
    return ConcatMapOperator(fn)
