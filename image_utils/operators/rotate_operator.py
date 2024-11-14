from PIL import Image
import math
from typing import Optional, Tuple
from .image_operator import ImageOperator

class RotateOperator(ImageOperator):
    """
    An image processing operator to rotate the image with canvas expansion and fill.

    Attributes:
        angle (float): Angle to rotate the image, in degrees.
        fillwith (str): Fill color in HEX format (default: transparent).
        fillwithpos (Optional[Tuple[int, int]]): Sample the fill color from the original image.

    Methods:
        __call__(image: Image.Image) -> Image.Image:
            Rotate the image and expand the canvas as needed, returning the processed image.
    """

    def __init__(self, 
                 angle: float, 
                 fillwith: str = "#00000000", 
                 fillwithpos: Optional[Tuple[int, int]] = None):
        self.angle = angle
        self.fillwith = fillwith
        self.fillwithpos = fillwithpos

    def __call__(self, image: Image.Image) -> Image.Image:
        """Rotate the image with expanded canvas."""
        original_width, original_height = image.size

        # Calculate expanded canvas size to fit the rotated image
        angle_rad = math.radians(self.angle)
        expanded_width = int(abs(original_width * math.cos(angle_rad)) + abs(original_height * math.sin(angle_rad)))
        expanded_height = int(abs(original_height * math.cos(angle_rad)) + abs(original_width * math.sin(angle_rad)))

        # Determine the fill color
        if self.fillwithpos:
            pos = self._adjust_position(self.fillwithpos, original_width, original_height)
            fill_color = image.getpixel(pos)
        else:
            fill_color = self._hex_to_rgba(self.fillwith)

        # Create the expanded canvas and paste the rotated image
        expanded_image = Image.new("RGBA", (expanded_width, expanded_height), fill_color)
        rotated_image = image.rotate(self.angle, expand=True)

        # Center the rotated image on the expanded canvas
        paste_x = (expanded_width - rotated_image.width) // 2
        paste_y = (expanded_height - rotated_image.height) // 2

        expanded_image.paste(rotated_image, (paste_x, paste_y), rotated_image)
        return expanded_image

    def _adjust_position(self, pos: Tuple[int, int], width: int, height: int) -> Tuple[int, int]:
        """Adjust position for negative indexing."""
        x, y = pos
        x = x if x >= 0 else width + x
        y = y if y >= 0 else height + y
        return max(0, min(x, width - 1)), max(0, min(y, height - 1))

    def _hex_to_rgba(self, hex_color: str) -> Tuple[int, int, int, int]:
        """Convert a HEX color string to an RGBA tuple."""
        hex_color = hex_color.lstrip('#')
        if len(hex_color) == 6:
            hex_color += 'FF'
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4, 6))

def rotate(angle: float,
           fillwith: str = "#00000000", 
           fillwithpos: Optional[Tuple[int, int]] = None) -> RotateOperator:
    """Create a RotateOperator instance with the specified settings."""
    return RotateOperator(angle, fillwith, fillwithpos)
