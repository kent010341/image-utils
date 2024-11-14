# Flip Operator

The `flip` operator flips an image either horizontally or vertically.

## CLI Usage

```bash
image-utils flip [OPTIONS] DIRECTION
```

### Arguments

* `DIRECTION` (str): Direction to flip the image. Options are:
    * `h`: Flip horizontally
    * `v`: Flip vertically

### Options

* `--input`, `-i` (optional): Path to the input image. If omitted and no data is provided via `stdin`, a file picker will open.

### Examples
1. Flip an image horizontally:
    ```bash
    image-utils flip h --input input.png > output.png
    ```

2. Flip an image vertically:
    ```bash
    image-utils flip v --input input.png > output.png
    ```

## Python Package Usage

Use `flip` as part of a processing pipeline or directly on images.

### Example

Using `flip` independently.

```python
from PIL import Image
from image_utils.operators import flip

# Load an image
input_image = Image.open('input.png')

# Flip the image horizontally
op = flip(direction='h')
flipped_image = op(input_image)

# Save the processed image
flipped_image.save('output.png')
```

Using `flip` in a pipeline.

```python
from PIL import Image
from image_utils.operators import flip
from image_utils.pipeline import pipe

# Load an image
input_image = Image.open('input.png')

# Create a pipeline that combines multiple operators
pipeline = pipe(
    # other operators ...
    flip(direction='h'),
    # other operators ...
)

# Process the image through the pipeline
output_image = pipeline.process(input_image)

# Save the processed image
output_image.save('output.png')
```
