from PIL import Image, ImageSequence
from typing import List, Optional, Callable, Union, Iterator

class GifWrapper:
    """
    A wrapper for handling GIF animations, allowing frame indexing, slicing, and applying operators.

    Attributes:
        filepath (str): The path to the GIF file.
        frames (List[Image.Image]): The list of frames in the GIF.
        durations (List[int]): The duration (in milliseconds) for each frame.
        loop (int): The loop count for the GIF animation.
    """

    def __init__(self, filepath: str):
        """
        Initialize the GifWrapper.

        Args:
            filepath (str): The path to the GIF file.
        """
        self.filepath = filepath
        self.image = Image.open(filepath)

        # Load all frames and their durations
        self.frames = [frame.copy() for frame in ImageSequence.Iterator(self.image)]
        self.durations = getattr(self.image.info, "duration", [100] * len(self.frames))
        self.loop = getattr(self.image.info, "loop", 0)

    def __getitem__(self, index: Union[int, slice]) -> Union[Image.Image, List[Image.Image]]:
        """
        Get a frame or a slice of frames.

        Args:
            index (int or slice): The index or slice to retrieve.

        Returns:
            Image.Image or List[Image.Image]: A single frame or a list of frames.
        """
        return self.frames[index]

    def __setitem__(self, index: int, frame: Image.Image):
        """
        Set a frame at the given index.

        Args:
            index (int): The index of the frame to set.
            frame (Image.Image): The new frame to set.
        """
        self.frames[index] = frame

    def __len__(self) -> int:
        """
        Get the number of frames in the GIF.

        Returns:
            int: The number of frames.
        """
        return len(self.frames)

    def __iter__(self) -> Iterator[Image.Image]:
        """
        Iterate over the frames.

        Returns:
            Iterator[Image.Image]: An iterator over the frames.
        """
        return iter(self.frames)

    def apply(self, operator: Callable[[Image.Image], Image.Image]) -> 'GifWrapper':
        """
        Apply an operator to all frames.

        Args:
            operator (Callable[[Image.Image], Image.Image]): The operator to apply.

        Returns:
            GifWrapper: The modified GifWrapper instance.
        """
        self.frames = [operator(frame) for frame in self.frames]
        return self

    def apply_with_index(self, operator_factory: Callable[[Image.Image, int], Image.Image]) -> 'GifWrapper':
        """
        Apply an operator to all frames with the frame index provided.

        Args:
            operator_factory (Callable[[Image.Image, int], Image.Image]): A factory function
            that takes a frame and its index and returns a processed frame.

        Returns:
            GifWrapper: The modified GifWrapper instance.
        """
        self.frames = [operator_factory(frame, i) for i, frame in enumerate(self.frames)]
        return self

    def save(self, output_filepath: str, duration: Optional[Union[int, List[int]]] = None, loop: Optional[int] = None):
        """
        Save the GIF to a file.

        Args:
            output_filepath (str): The path to save the output GIF.
            duration (int or List[int], optional): The duration (in milliseconds) for each frame. Default is the original durations.
            loop (int, optional): The loop count for the GIF. Default is the original loop count.
        """
        duration = duration or self.durations
        loop = loop if loop is not None else self.loop
        self.frames[0].save(
            output_filepath,
            save_all=True,
            append_images=self.frames[1:],
            duration=duration,
            loop=loop,
            disposal=2  # Clear each frame before displaying the next
        )

    def export_frames(self, directory: str):
        """
        Export all frames as individual image files.

        Args:
            directory (str): The directory to save the frames.
        """
        for i, frame in enumerate(self.frames):
            frame.save(f"{directory}/frame_{i}.png")

    def to_image_sequence(self) -> Iterator[Image.Image]:
        """
        Return the frames as an iterator compatible with ImageSequence.

        Returns:
            Iterator[Image.Image]: An iterator over the frames.
        """
        return iter(self.frames)

    def __repr__(self) -> str:
        """
        Return a string representation of the GifWrapper.

        Returns:
            str: A string representation of the GifWrapper.
        """
        return f"GifWrapper(filepath={self.filepath}, frames={len(self.frames)})"
