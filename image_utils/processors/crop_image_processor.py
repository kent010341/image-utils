from .image_processor import ImageProcessor
from PIL import Image
from typing import Optional

class CropImageProcessor(ImageProcessor):
    """
    A class for cropping an image to its bounding box and converting it to a square.

    Inherits from ImageProcessor.
    """

    def __init__(self, input_path: Optional[str] = None, align: str = 'center'):
        """
        Initialize the CropImageProcessor with input path and alignment.

        Args:
            input_path (Optional[str]): The input image path.
            align (str): The alignment for cropping.
        """
        super().__init__(input_path)
        self.align = align

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
