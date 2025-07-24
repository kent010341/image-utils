# Expand Operator

The `expand` operator increases the canvas size of an image to a specified width and height, placing the original image within the new canvas according to alignment settings and filling the background with a specified color.

## CLI Usage

```bash
image-utils expand [OPTIONS] SIZE
```

### Arguments

* `SIZE` (str): Target size in the format `{width}x{height}`. Either `width` or `height` can be omitted, in which case the original dimension will be used. Examples:

    * `100x200`: Expand canvas to 100x200 pixels.
    * `300x`: Expand canvas to 300 pixels wide, original height retained.
    * `x400`: Expand canvas to 400 pixels high, original width retained.

### Options

* `--fillwith` (str, default=`#00000000`): Fill color for the expanded area in HEX format. Default is transparent.

* `--align` (str, default=c): Alignment of the original image on the expanded canvas. Options:
    * `c`: Center
    * `t`: Top
    * `b`: Bottom
    * `l`: Left
    * `r`: Right
    * `lt`: Left-top
    * `rt`: Right-top
    * `lb`: Left-bottom
    * `rb`: Right-bottom

* `--dx` (int, default=`0`): Horizontal shift from the aligned position.

* `--dy` (int, default=`0`): Vertical shift from the aligned position.

* `--fillwithpos` (tuple, optional): Sample the fill color from the specified coordinates in the original image. Overrides `--fillwith` if set.

* `--input`, `-i` (optional): Path to the input image. If omitted and no data is provided via `stdin`, a file picker will open.

### Examples
1. Expand the canvas to 200x200 pixels, centering the image with a white background:
    ```bash
    image-utils expand 200x200 --fillwith "#FFFFFF" --align c --input input.png > output.png
    ```

2. Expand the width to 300 pixels, keeping the original height and aligning the image to the left:
    ```bash
    image-utils expand 300x --align l --input input.png > output.png
    ```

3. Expand the canvas and sample the fill color from the top-left corner of the image:
    ```bash
    image-utils expand 400x400 --fillwithpos 0 0 --input input.png > output.png
    ```

## Python Package Usage

Use `expand` as part of a processing pipeline or directly on images.

### Example

Using `expand` independently.

```python
from PIL import Image
from image_utils.operators import expand

# Load an image
input_image = Image.open('input.png')

# Expand the canvas to 300x300 pixels with a red background and center alignment
op = expand(width=300, height=300, fillwith="#FF0000", align='c')
expanded_image = op(input_image)

# Save the processed image
expanded_image.save('output.png')
```

Using `expand` in a pipeline.

```python
from PIL import Image
from image_utils.operators import expand
from image_utils.pipeline import pipe

# Load an image
input_image = Image.open('input.png')

# Create a pipeline that combines multiple operators
pipeline = pipe(
    # other operators ...
    expand(width=400, height=400, fillwith="#000000", align='rb', dx=10, dy=20),
    # other operators ...
)

# Process the image through the pipeline
output_image = pipeline(input_image)

# Save the processed image
output_image.save('output.png')
```
