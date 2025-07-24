# Trim Operator

The `trim` operator removes transparent borders around an image, automatically cropping to the bounding box of the non-transparent area.

## CLI Usage

```bash
image-utils trim [OPTIONS]
```

### Options

* `--input`, `-i` (optional): Path to the input image. If omitted and no data is provided via `stdin`, a file picker will open.

### Examples
1. Trim transparent borders from an image:
    ```bash
    image-utils trim --input input.png > output.png
    ```

## Python Package Usage

Use `trim` as part of a processing pipeline or directly on images.

### Example

Using `trim` independently.

```python
from PIL import Image
from image_utils.operators import trim

# Load an image
input_image = Image.open('input.png')

# Trim transparent borders
op = trim()
trimmed_image = op(input_image)

# Save the processed image
trimmed_image.save('output.png')
```

Using `trim` in a pipeline.

```python
from PIL import Image
from image_utils.operators import trim
from image_utils.pipeline import pipe

# Load an image
input_image = Image.open('input.png')

# Create a pipeline that combines multiple operators
pipeline = pipe(
    # other operators ...
    trim(),
    # other operators ...
)

# Process the image through the pipeline
output_image = pipeline(input_image)

# Save the processed image
output_image.save('output.png')
```
