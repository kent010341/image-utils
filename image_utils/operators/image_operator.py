from PIL import Image

class ImageOperator:
    """
    A base class for image processing operators.

    This class defines a common interface for all image processing operators.
    Subclasses should implement the __call__ method to perform their specific
    image processing tasks.

    Methods:
        __call__(image: Image.Image) -> Image.Image:
            Process the input image and return the processed image.
    """
    def __call__(self, image: Image.Image) -> Image.Image:
        """
        Process the input image.

        Args:
            image (Image.Image): The input image to be processed.

        Returns:
            Image.Image: The processed image.

        Raises:
            NotImplementedError: If the method is not overridden by a subclass.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def __repr__(self) -> str:
        """
        Return a string representation of the operator.

        Returns:
            str: A string representation of the operator.
        """
        return f"{self.__class__.__name__}()"
