# ConcatMap Operator

The `concatMap` operator dynamically selects an image transformer based on the input image. It enables conditional or data-dependent transformations by mapping an image to a corresponding `ImageTransformer` and applying it immediately.

This operator is inspired by RxJS's `concatMap` and is suitable for advanced logic branching within a pipeline.

> Note: This operator is not exposed to the CLI. It is designed for use in programmatic workflows only.

## Python Package Usage

Use `concat_map` to create conditional branches in a processing pipeline.

### Example

Resize an image based on its aspect ratio: if it's wider than tall, resize width to 256; otherwise, resize height to 256.

```python
from PIL import Image
from image_utils.operators import trim, resize, expand, concat_map
from image_utils.pipeline import pipe

# Load an image
input_image = Image.open('input.jpg')

# Create a conditional pipeline
pipeline = pipe(
    trim(),
    concat_map(lambda img: resize(width=256) if img.width >= img.height else resize(height=256)),
    expand(width=256, height=256)
)

# Apply the pipeline
output_image = pipeline(input_image)

# Save result
output_image.save('output.jpg')
```

### When to Use

Use `concatMap` when:
- You need to branch logic based on the image content (e.g., width, height, color).
- A fixed sequence of operators isn't sufficient.
- You're constructing dynamic sub-pipelines.

This makes `concatMap` essential for building expressive, data-driven pipelines with reusable logic.
