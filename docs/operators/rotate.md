# Rotate Operator

The `rotate` operator rotates an image by a specified angle, expanding the canvas as needed to accommodate the rotated image. The expanded areas can be filled with a specified color, or the fill color can be sampled from a specified location within the original image.

## CLI Usage

```bash
image-utils rotate [OPTIONS] ANGLE
```

### Arguments

* `ANGLE` (float): Rotation angle in degrees. Positive values rotate counterclockwise.

### Options

* `--fillwith` (str, default=`#00000000`): Fill color for the expanded area in HEX format. Default is transparent.
* `--fillwithpos` (tuple, optional): Sample the fill color from the specified coordinates in the original image. Overrides `--fillwith` if set.
* `--input`, `-i` (optional): Path to the input image. If omitted and no data is provided via `stdin`, a file picker will open.

### Examples
1. Rotate an image by 45 degrees with a white background:
    ```bash
    image-utils rotate 45 --fillwith "#FFFFFF" --input input.png > output.png
    ```

2. Rotate by 30 degrees and sample the fill color from the top-left corner of the image:
    ```bash
    image-utils rotate 30 --fillwithpos 0 0 --input input.png > output.png
    ```

## Python Package Usage

Use `rotate` as part of a processing pipeline or directly on images.

### Example

Using `rotate` independently.

```python
from PIL import Image
from image_utils.operators import rotate

# Load an image
input_image = Image.open('input.png')

# Rotate by 45 degrees with a blue background
op = rotate(angle=45, fillwith="#0000FF")
rotated_image = op(input_image)

# Save the processed image
rotated_image.save('output.png')
```

Using `rotate` in a pipeline.

```python
from PIL import Image
from image_utils.operators import rotate
from image_utils.pipeline import pipe

# Load an image
input_image = Image.open('input.png')

# Create a pipeline that combines multiple operators
pipeline = pipe(
    # other operators ...
    rotate(angle=30, fillwith="#FF5733"),
    # other operators ...
)

# Process the image through the pipeline
output_image = pipeline(input_image)

# Save the processed image
output_image.save('output.png')
```
