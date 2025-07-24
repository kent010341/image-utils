from PIL import Image
from typing import List, Union
from .core.image_transformer import ImageTransformer

class Pipeline(ImageTransformer):
    """
    A composable pipeline for sequential image transformations.

    This class allows chaining multiple image transformers (either operators or other pipelines)
    and applying them in order via a single callable interface.

    Attributes:
        transformers (List[ImageTransformer]): A list of image transformers.

    Methods:
        add(*transformers: ImageTransformer) -> 'Pipeline':
            Add additional transformers to the pipeline.
    """

    def __init__(self, transformers: List[ImageTransformer] = None):
        """
        Initialize the Pipeline with an optional list of transformers.

        Args:
            transformers (List[ImageTransformer], optional): A list of callable image transformers. Defaults to empty.
        """
        self.transformers = transformers if transformers is not None else []

    def __call__(self, image: Image.Image) -> Image.Image:
        """
        Apply the pipeline of transformations to the input image.

        Args:
            image (Image.Image): The input image to be transformed.

        Returns:
            Image.Image: The transformed image.
        """
        result = image
        for transformer in self.transformers:
            result = transformer(result)
        return result

    def add(self, *transformers: ImageTransformer) -> 'Pipeline':
        """
        Add additional transformers to the pipeline.

        Args:
            *transformers (ImageTransformer): One or more callable image transformers.

        Returns:
            Pipeline: The updated pipeline.
        """
        self.transformers.extend(transformers)
        return self

    def __repr__(self) -> str:
        """
        Return a string representation of the pipeline.

        Returns:
            str: A multiline string showing each transformer in the pipeline.
        """
        transformers_repr = ',\n  '.join(repr(t) for t in self.transformers)
        return f"Pipeline(\n  {transformers_repr}\n)"

def pipe(*transformers: ImageTransformer) -> Pipeline:
    """
    Create a Pipeline instance from a list of image transformers.

    Args:
        *transformers (ImageTransformer): One or more callable image transformers.

    Returns:
        Pipeline: A new Pipeline instance.
    """
    return Pipeline(list(transformers))
