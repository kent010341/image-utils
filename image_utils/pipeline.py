from PIL import Image
from typing import List, Type
from .operators.image_operator import ImageOperator

class Pipeline:
    """
    A class to manage and apply a series of image processing operators.

    This class allows chaining multiple image processing operators and applying them
    sequentially to an input image.

    Attributes:
        operators (List[Type[ImageOperator]]): A list of image processing operators.

    Methods:
        process(image: Image.Image) -> Image.Image:
            Apply the pipeline of operators to the input image and return the processed image.
        add_operator(*operators: Type[ImageOperator]) -> 'Pipeline':
            Add additional operators to the pipeline and return the updated pipeline.
    """
    def __init__(self, operators: List[Type[ImageOperator]] = None):
        """
        Initialize the Pipeline with an optional list of operators.

        Args:
            operators (List[Type[ImageOperator]], optional): A list of image processing operators. Default is None.
        """
        self.operators = operators if operators is not None else []

    def process(self, image: Image.Image) -> Image.Image:
        """
        Apply the pipeline of operators to the input image.

        Args:
            image (Image.Image): The input image to be processed.

        Returns:
            Image.Image: The processed image.
        """
        result = image
        for operator in self.operators:
            result = operator(result)
        return result

    def add(self, *operators: Type[ImageOperator]) -> 'Pipeline':
        """
        Add additional operators to the pipeline.

        Args:
            *operators (Type[ImageOperator]): One or more image processing operators to add to the pipeline.

        Returns:
            Pipeline: The updated pipeline with the added operators.
        """
        self.operators.extend(operators)
        return self

    def __repr__(self) -> str:
        """
        Return a string representation of the pipeline.

        Returns:
            str: A string representation of the pipeline.
        """
        operators_repr = ',\n  '.join(repr(op) for op in self.operators)
        return f"Pipeline(\n  {operators_repr}\n)"

def pipe(*operators: Type[ImageOperator]) -> Pipeline:
    """
    Create a Pipeline with the specified operators.

    Args:
        *operators (Type[ImageOperator]): One or more image processing operators.

    Returns:
        Pipeline: A new Pipeline instance with the specified operators.
    """
    return Pipeline(list(operators))
