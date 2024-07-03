from PIL import Image
from .image_operator import ImageOperator

class CropOperator(ImageOperator):
    """
    An image processing operator to crop an image to its bounding box and convert it to a square.

    Attributes:
        align (str): Alignment of the cropped image in the square. Options are 'top', 'bottom', 
                     'left', 'right', and 'center'. Default is 'center'.

    Methods:
        __call__(image: Image.Image) -> Image.Image:
            Crop the input image and return the processed image.
    """
    def __init__(self, align: str = 'center'):
        """
        Initialize the CropOperator with the specified alignment.

        Args:
            align (str): Alignment of the cropped image in the square. Default is 'center'.
        """
        self.align = align

    def __call__(self, image: Image.Image) -> Image.Image:
        """
        Crop the input image to its bounding box and convert it to a square.

        Args:
            image (Image.Image): The input image to be processed.

        Returns:
            Image.Image: The cropped and squared image.
        """
        bbox = image.getbbox()
        if bbox:
            cropped_image = image.crop(bbox)
            cropped_width, cropped_height = cropped_image.size

            max_side = max(cropped_width, cropped_height)
            square_image = Image.new("RGBA", (max_side, max_side), (0, 0, 0, 0))

            if self.align == 'top':
                paste_x = (max_side - cropped_width) // 2
                paste_y = 0
            elif self.align == 'bottom':
                paste_x = (max_side - cropped_width) // 2
                paste_y = max_side - cropped_height
            elif self.align == 'left':
                paste_x = 0
                paste_y = (max_side - cropped_height) // 2
            elif self.align == 'right':
                paste_x = max_side - cropped_width
                paste_y = (max_side - cropped_height) // 2
            else:  # center
                paste_x = (max_side - cropped_width) // 2
                paste_y = (max_side - cropped_height) // 2
            
            square_image.paste(cropped_image, (paste_x, paste_y))
        else:
            square_image = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
        
        return square_image

    def __repr__(self) -> str:
        """
        Return a string representation of the CropOperator.

        Returns:
            str: A string representation of the CropOperator.
        """
        return f"CropOperator(align='{self.align}')"

def crop(align: str = 'center') -> CropOperator:
    """
    Create a CropOperator instance with the specified alignment.

    Args:
        align (str): Alignment of the cropped image in the square. Default is 'center'.

    Returns:
        CropOperator: An instance of CropOperator.
    """
    return CropOperator(align=align)
