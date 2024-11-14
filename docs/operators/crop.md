# Crop Operator

The `crop` operator allows you to crop an image to a specified rectangular area. You can define the boundaries in pixels or as a percentage of the image size.

## CLI Usage

```bash
image-utils crop [OPTIONS]
```

### Options

* `--input`, `-i` (optional): Path to the input image. If omitted and no data is provided via `stdin`, a file picker will open.
* `--left`, `-l` (int | float | str, default=`0`): Left boundary for cropping. Accepts pixels or percentage (e.g., `0.1x` for 10%).
* `--top`, `-t` (int | float | str, default=`0`): Top boundary for cropping. Accepts pixels or percentage (e.g., `0.1x` for 10%).
* `--right`, `-r` (int | float | str, default=`1.0x`): Right boundary for cropping. Accepts pixels or percentage (e.g., `0.9x` for 90%).
* `--bottom`, `-b` (int | float | str, default=`1.0x`): Bottom boundary for cropping. Accepts pixels or percentage (e.g., `0.9x` for 90%).

### Examples

1. Crop an image to a center-aligned square:
    ```bash
    image-utils crop --left 0.1x --top 0.1x --right 0.9x --bottom 0.9x > output.jpg
    ```

2. Crop using pixels for exact boundaries:
    ```bash
    image-utils crop --left 10 --top 10 --right 200 --bottom 200 > output.jpg
    ```

## Python Package Usage

Use `crop` as part of a processing pipeline or directly on images. If no boundaries are specified, the entire image is retained.

### Example

Using `crop` independently.

```python
from PIL import Image
from image_utils.operators import crop

# Load an image
input_image = Image.open('input.jpg')

# Crop the image using boundaries
op = crop(left=0.1, top=0.1, right=0.9, bottom=0.9)
cropped_image = op(input_image)

# Save the processed image
cropped_image.save('output.jpg')
```

Using `crop` in a pipeline.

```python
from PIL import Image
from image_utils.operators import crop
from image_utils.pipeline import pipe

# Load an image
input_image = Image.open('input.jpg')

# Create a pipeline that combines multiple operators
pipeline = pipe(
    # other operators ...
    crop(left=0.1, top=0.1, right=0.9, bottom=0.9),
    # other operators ...
)

# Process the image through the pipeline
output_image = pipeline.process(input_image)

# Save the processed image
output_image.save('output.jpg')
```
