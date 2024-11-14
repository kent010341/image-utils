# Gray Scale Operator

The `gray_scale` operator converts an image to grayscale, transforming it into shades of gray while preserving the alpha channel.

## CLI Usage

```bash
image-utils gray_scale [OPTIONS]
```

### Options

* `--input`, `-i` (optional): Path to the input image. If omitted and no data is provided via `stdin`, a file picker will open.

### Examples
1. Convert an image to grayscale:
    ```bash
    image-utils gray_scale --input input.png > output.png
    ```

## Python Package Usage

Use `gray_scale` as part of a processing pipeline or directly on images.

### Example

Using `gray_scale` independently.

```python
from PIL import Image
from image_utils.operators import gray_scale

# Load an image
input_image = Image.open('input.png')

# Convert the image to grayscale
op = gray_scale()
gray_image = op(input_image)

# Save the processed image
gray_image.save('output.png')
```

Using `gray_scale` in a pipeline.

```python
from PIL import Image
from image_utils.operators import gray_scale
from image_utils.pipeline import pipe

# Load an image
input_image = Image.open('input.png')

# Create a pipeline that combines multiple operators
pipeline = pipe(
    # other operators ...
    gray_scale(),
    # other operators ...
)

# Process the image through the pipeline
output_image = pipeline.process(input_image)

# Save the processed image
output_image.save('output.png')
```
