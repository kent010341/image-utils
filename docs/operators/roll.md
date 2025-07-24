# Roll Operator

The `roll` operator shifts the image content horizontally or vertically by a specified number of pixels, wrapping the content around to the opposite edge.

## CLI Usage

```bash
image-utils roll [OPTIONS] SHIFT
```

### Arguments

* `SHIFT` (int): Number of pixels to shift the image.

### Options

* `--direction`, `-d` (default=`r`): Direction to roll the image. Options are:

    * l: Roll left
    * r: Roll right (default)
    * u: Roll up
    * b: Roll down

* `--input`, `-i` (optional): Path to the input image. If omitted and no data is provided via `stdin`, a file picker will open.

### Examples
1. Roll an image 50 pixels to the right (default direction):
    ```bash
    image-utils roll 50 --input input.png > output.png
    ```

2. Roll an image 30 pixels up:
    ```bash
    image-utils roll 30 --direction u --input input.png > output.png
    ```

## Python Package Usage

Use `roll` as part of a processing pipeline or directly on images.
Example

Using `roll` independently.

```python
from PIL import Image
from image_utils.operators import roll

# Load an image
input_image = Image.open('input.png')

# Roll the image 50 pixels to the right
op = roll(shift=50, direction='r')
rolled_image = op(input_image)

# Save the processed image
rolled_image.save('output.png')
```

Using `roll` in a pipeline.

```python
from PIL import Image
from image_utils.operators import roll
from image_utils.pipeline import pipe

# Load an image
input_image = Image.open('input.png')

# Create a pipeline that combines multiple operators
pipeline = pipe(
    # other operators ...
    roll(shift=50, direction='r'),
    # other operators ...
)

# Process the image through the pipeline
output_image = pipeline(input_image)

# Save the processed image
output_image.save('output.png')
```
