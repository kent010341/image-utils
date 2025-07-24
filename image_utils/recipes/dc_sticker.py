from ..core.image_transformer import ImageTransformer
from ..operators import trim, concat_map, resize, expand
from ..pipeline import pipe
from PIL import Image

def dc_sticker():
    """Create a pipeline for processing images into Discord stickers format."""
    return pipe(
        trim(),
        concat_map(_resize_image),
        expand(width=256, height=256),
    )

def _resize_image(image: Image.Image) -> ImageTransformer:
    """Determine the resizing strategy based on the image dimensions."""
    width, height = image.size
    if width > height:
        return resize(width=256)
    else:
        return resize(height=256)
