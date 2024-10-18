from PIL import Image
from typing import Optional, Tuple, Union
from .image_operator import ImageOperator

class ExpandOperator(ImageOperator):
    """
    An image processing operator to expand the image canvas while keeping the original image intact.

    Attributes:
        width (Optional[int]): Target width of the expanded image. Default is None.
        height (Optional[int]): Target height of the expanded image. Default is None.
        fillwith (str): Fill color in HEX format (default: transparent).
        align (str): Alignment of the original image on the expanded canvas. Default is 'c'.
        dx (int): Horizontal shift (default: 0).
        dy (int): Vertical shift (default: 0).
        fillwithpos (Optional[Tuple[int, int]]): Sample the fill color from the original image.

    Methods:
        __call__(image: Image.Image) -> Image.Image:
            Expand the canvas and return the processed image.
    """

    def __init__(self, 
                 width: Optional[int] = None, 
                 height: Optional[int] = None,
                 fillwith: str = "#00000000", 
                 align: str = 'c', 
                 dx: int = 0, dy: int = 0, 
                 fillwithpos: Optional[Tuple[int, int]] = None):
        self.width = width
        self.height = height
        self.fillwith = fillwith
        self.align = align
        self.dx = dx
        self.dy = dy
        self.fillwithpos = fillwithpos

    def __call__(self, image: Image.Image) -> Image.Image:
        """Expand the canvas size and position the original image."""
        original_width, original_height = image.size

        target_width = self.width or original_width
        target_height = self.height or original_height

        if target_width < original_width or target_height < original_height:
            raise ValueError("Target dimensions cannot be smaller than the original image.")

        # Determine the fill color
        if self.fillwithpos:
            pos = self._adjust_position(self.fillwithpos, original_width, original_height)
            fill_color = image.getpixel(pos)
        else:
            fill_color = self._hex_to_rgba(self.fillwith)

        expanded_image = Image.new("RGBA", (target_width, target_height), fill_color)
        paste_x, paste_y = self._calculate_position(
            original_width, original_height, target_width, target_height
        )
        paste_x = max(0, min(paste_x + self.dx, target_width - original_width))
        paste_y = max(0, min(paste_y + self.dy, target_height - original_height))

        expanded_image.paste(image, (paste_x, paste_y))
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

    def _calculate_position(self, ow: int, oh: int, ew: int, eh: int) -> Tuple[int, int]:
        """Calculate paste position based on alignment."""
        align_map = {
            'c': ((ew - ow) // 2, (eh - oh) // 2),
            't': ((ew - ow) // 2, 0),
            'b': ((ew - ow) // 2, eh - oh),
            'l': (0, (eh - oh) // 2),
            'r': (ew - ow, (eh - oh) // 2),
            'lt': (0, 0),
            'rt': (ew - ow, 0),
            'lb': (0, eh - oh),
            'rb': (ew - ow, eh - oh),
        }
        return align_map.get(self.align, align_map['c'])

def expand(width: int = None,
           height: int = None,
           fillwith: str = "#00000000", 
           align: str = 'c', 
           dx: int = 0, dy: int = 0, 
           fillwithpos: Optional[Tuple[int, int]] = None) -> ExpandOperator:
    """Create an ExpandOperator instance with the specified settings."""
    return ExpandOperator(width, height, fillwith, align, dx, dy, fillwithpos)
