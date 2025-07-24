from ..pipeline import pipe
from ..operators import trim, resize

def tg_sticker():
    """Create a pipeline for processing images into Telegram stickers format."""
    return pipe(
        trim(),
        resize(width=256, height=256),
    )
