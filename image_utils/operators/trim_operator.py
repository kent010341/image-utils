from PIL import Image
from .image_operator import ImageOperator
from .crop_operator import crop

class TrimOperator(ImageOperator):
    """
    An image processing operator to trim an image to its bounding box, removing any transparent borders.

    Methods:
        __call__(image: Image.Image) -> Image.Image:
            Trim the input image to its bounding box and return the processed image.
    """
    def __call__(self, image: Image.Image) -> Image.Image:
        """
        Trim the input image to its bounding box.

        Args:
            image (Image.Image): The input image to be processed.

        Returns:
            Image.Image: The trimmed image.
        """
        bbox = image.getbbox()
        if bbox:
            left, top, right, bottom = bbox
            operator = crop(left, top, right, bottom)
            return operator(image)
        else:
            # Return a minimal 1x1 image if bounding box is not found (e.g., fully transparent image)
            return Image.new("RGBA", (1, 1), (0, 0, 0, 0))

    def __repr__(self) -> str:
        """
        Return a string representation of the TrimOperator.

        Returns:
            str: A string representation of the TrimOperator.
        """
        return "TrimOperator()"

def trim() -> TrimOperator:
    """
    Create a TrimOperator instance.

    Returns:
        TrimOperator: An instance of TrimOperator.
    """
    return TrimOperator()
