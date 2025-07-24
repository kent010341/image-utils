# Resize Operator

The `resize` operator resizes an image to the specified width and height. If only one dimension (width or height) is provided, the other dimension will be scaled proportionally to maintain the aspect ratio.

## CLI Usage

```bash
image-utils resize [OPTIONS] SIZE
```

### Arguments

* `SIZE` (str): Target size in the format `{width}x{height}`. Either `width` or `height` can be omitted to scale proportionally. Examples:

    * `100x200`: Resize to exactly 100x200 pixels.
    * `300x`: Resize to 300 pixels wide, maintaining aspect ratio.
    * `x400`: Resize to 400 pixels high, maintaining aspect ratio.

### Options

* `--input`, `-i` (optional): Path to the input image. If omitted and no data is provided via `stdin`, a file picker will open.

### Examples
1. Resize an image to 100x100 pixels:
    ```bash
    image-utils resize 100x100 --input input.jpg > output.jpg
    ```

2. Resize an image to 100 pixels wide, maintaining aspect ratio:
    ```bash
    image-utils resize 100x --input input.jpg > output.jpg
    ```

3. Resize an image to 50 pixels high, maintaining aspect ratio:
    ```
    image-utils resize x50 --input input.jpg > output.jpg
    ```

## Python Package Usage

Use `resize` as part of a processing pipeline or directly on images.

### Example

Using `resize` independently.

```python
from PIL import Image
from image_utils.operators import resize

# Load an image
input_image = Image.open('input.jpg')

# Resize the image to 100x100 pixels
op = resize(width=100, height=100)
resized_image = op(input_image)

# Save the processed image
resized_image.save('output.jpg')
```

Using `resize` in a pipeline.

```python
from PIL import Image
from image_utils.operators import resize
from image_utils.pipeline import pipe

# Load an image
input_image = Image.open('input.jpg')

# Create a pipeline that combines multiple operators
pipeline = pipe(
    # other operators ...
    resize(width=100, height=100),
    # other operators ...
)

# Process the image through the pipeline
output_image = pipeline(input_image)

# Save the processed image
output_image.save('output.jpg')
```
