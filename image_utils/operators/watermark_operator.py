from PIL import Image, ImageDraw, ImageFont
from .image_operator import ImageOperator
import math

class WatermarkOperator(ImageOperator):
    """
    An image processing operator to add a watermark text to an image.

    Attributes:
        text (str): The watermark text to be added to the image.
        color (str): The color of the watermark text in hex. Default is 'FFFFFF'.
        opacity (int): The opacity level of the watermark text. Default is 30.
        angle (Union[int, str]): The angle at which the watermark text is placed.
                                 Can be an integer or 'diagonal' for auto-calculated diagonal placement.
        font_size (int): The font size of the watermark text. Default is auto.
        
    Methods:
        __call__(image: Image.Image) -> Image.Image:
            Add the watermark to the input image and return the processed image.
    """
    def __init__(self, text: str, color: str = 'FFFFFF', opacity: int = 30, angle: int | str = 0, font_size: int = None):
        """
        Initialize the WatermarkOperator with the specified parameters.

        Args:
            text (str): The watermark text to be added to the image.
            color (str): The color of the watermark text in hex. Default is 'FFFFFF'.
            opacity (int): The opacity level of the watermark text. Default is 30.
            angle (Union[int, str]): The angle at which the watermark text is placed.
                                     Can be an integer or 'diagonal' for auto-calculated diagonal placement.
            font_size (int): The font size of the watermark text. Default is auto.
        """
        self.text = text
        self.color = color
        self.opacity = opacity
        self.angle = angle
        self.font_size = font_size

    def _calculate_font_size(self, image: Image.Image, text: str, angle: float) -> int:
        """
        Calculate the font size to fit the text within the image dimensions considering the rotation angle.

        Args:
            image (Image.Image): The input image.
            text (str): The watermark text to be added to the image.
            angle (float): The angle at which the watermark text is placed.

        Returns:
            int: The calculated font size.
        """
        width, height = image.size

        # Start with a large font size
        font_size = 1000  # Start with a large font size to determine the correct scale
        font = ImageFont.truetype("arial.ttf", font_size)
        text_width, text_height = ImageDraw.Draw(image).textsize(text, font=font)

        # Calculate the rotated text bounding box dimensions
        theta = math.radians(angle)
        rotated_width = text_width * math.cos(theta) + text_height * math.sin(theta)
        rotated_height = text_width * math.sin(theta) + text_height * math.cos(theta)

        # Scale down font size to fit within image dimensions
        scale_factor = min(width / rotated_width, height / rotated_height)
        adjusted_font_size = int(font_size * scale_factor)

        return adjusted_font_size

    def __call__(self, image: Image.Image) -> Image.Image:
        """
        Add the watermark to the input image and return the processed image.

        Args:
            image (Image.Image): The input image to be processed.

        Returns:
            Image.Image: The image with the watermark added.
        """
        # Convert color hex to RGBA
        r, g, b = tuple(int(self.color[i:i+2], 16) for i in (0, 2, 4))
        watermark_color = (r, g, b, int(255 * (self.opacity / 100)))

        # Create a transparent image for the watermark
        watermark = Image.new('RGBA', image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(watermark)

        # Determine the angle
        if self.angle == 'diagonal':
            angle = math.degrees(math.atan(image.height / image.width))
        else:
            angle = self.angle

        # Load the default PIL font
        font_path = "arial.ttf"  # This should be the path to a real font file
        try:
            if self.font_size is None:
                font_size = self._calculate_font_size(image, self.text, angle)
            else:
                font_size = self.font_size

            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            font = ImageFont.load_default()

        # Calculate text size and positioning with the default font
        bbox = draw.textbbox((0, 0), self.text, font=font)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

        # Calculate text position based on alignment
        x = (image.width - text_width) / 2
        y = (image.height - text_height) / 2

        # Apply watermark
        draw.text((x, y), self.text, font=font, fill=watermark_color)
        watermark = watermark.rotate(angle, expand=1)

        # Resize watermark to match original image size
        watermark = watermark.resize(image.size, resample=Image.Resampling.LANCZOS)

        # Composite the watermark with the original image
        watermarked_image = Image.alpha_composite(image.convert('RGBA'), watermark)

        return watermarked_image

    def __repr__(self) -> str:
        """
        Return a string representation of the WatermarkOperator.

        Returns:
            str: A string representation of the WatermarkOperator.
        """
        return f"WatermarkOperator(text='{self.text}', color='{self.color}', opacity={self.opacity}, angle='{self.angle}', font_size={self.font_size})"

def watermark(text: str, color: str = 'FFFFFF', opacity: int = 30, angle: int | str = 0, font_size: int = None) -> WatermarkOperator:
    """
    Create a WatermarkOperator instance with the specified parameters.

    Args:
        text (str): The watermark text to be added to the image.
        color (str): The color of the watermark text in hex. Default is 'FFFFFF'.
        opacity (int): The opacity level of the watermark text. Default is 30.
        angle (Union[int, str]): The angle at which the watermark text is placed.
                                 Can be an integer or 'diagonal' for auto-calculated diagonal placement.
        font_size (int): The font size of the watermark text. Default is auto.

    Returns:
        WatermarkOperator: An instance of WatermarkOperator.
    """
    return WatermarkOperator(text=text, color=color, opacity=opacity, angle=angle, font_size=font_size)