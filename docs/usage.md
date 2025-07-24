# Image Utils Usage Guide

The Image Utils Package offers a flexible and modular approach for image processing, accessible both via command-line interface (CLI) and as a Python package. Each command/operator supports versatile image input/output methods, making it easy to integrate into automated workflows.

For more details on each specific operator's functionality and options, refer to the individual documentation files under the [`operators/`](operators/) directory.

## Command-Line Interface (CLI) Usage

All CLI commands in Image Utils support standard input and output handling, providing a seamless experience for image processing tasks. The commands allow three primary ways to specify image inputs:
1. **File input using `--input` option**: Specify the path to an image file.
2. **Piped input from stdin**: Stream image data directly from the command line.
3. **File picker**: If no input is specified, a file selection dialog will open.

### Basic Command Structure
```bash
image-utils <command> [OPTIONS] > output.png
```

By default, commands output the processed image to stdout, allowing results to be redirected into files or piped to other commands for chaining operations.

### Examples

* Resize an image:
    ```bash
    image-utils resize 100x100 --input input.jpg > output.jpg
    ```

* Trim and resize:
    ```bash
    image-utils trim --input input.jpg | image-utils resize 100x100 > output.jpg
    ```

### Common CLI Behaviors

All commands share the following consistent behaviors:

* **Input Handling**: Commands accept images through `--input` or stdin. If neither is provided, a file picker will open.
* **Output to stdout**: Commands output the processed image to stdout, enabling flexible redirection and chaining.
* **Error Handling**: Commands provide feedback if an invalid option or input is encountered.

These shared features allow for flexible integration in shell scripts, batch processing, or manual workflows.

## Using as a Python Package

Image Utils can also be used directly in Python projects, making it possible to create more complex, programmatically controlled image processing workflows.

### Basic Package Usage

Here's an example of how to use the package to apply a sequence of image processing operations with a custom pipeline:

```python
from PIL import Image
from image_utils.operators import trim, resize
from image_utils.pipeline import pipe

# Load an image
input_image = Image.open('input.png')

# Define a processing pipeline
pipeline = pipe(
    trim(),  # Remove transparent borders
    resize(width=100, height=100)  # Resize to 100x100 pixels
)

# Process the image through the pipeline
output_image = pipeline(input_image)

# Save the processed image
output_image.save('output.png')
```

### Creating a Custom Operator

In addition to the built-in operators, you can create custom operators by subclassing `ImageOperator`. This allows you to define unique image transformations tailored to specific requirements and include them in a pipeline as modular components.

#### Example: Custom Operator

Here’s an example of a custom operator that inverts the colors of an image:

```python
from PIL import ImageOps, Image
from image_utils.operators.image_operator import ImageOperator
from image_utils.pipeline import pipe

# Define a custom operator by subclassing ImageOperator
class InvertOperator(ImageOperator):
    def __call__(self, image: Image.Image) -> Image.Image:
        # Apply inversion using ImageOps
        return ImageOps.invert(image)

# Load an image
input_image = Image.open('input.png')

# Create a pipeline with the custom operator
pipeline = pipe(
    InvertOperator()
)

# Process the image
output_image = pipeline(input_image)

# Save the processed image
output_image.save('output.png')
```

### Adding More Operators to an Existing Pipeline

You can extend an existing pipeline by adding more operators using the `add` method, making it easy to build complex image processing workflows dynamically.

```python
from PIL import Image
from image_utils.operators import trim, resize
from image_utils.pipeline import pipe

# Load an image
input_image = Image.open('input.png')

# Start a pipeline with trimming
pipeline = pipe(
    trim()
)

# Dynamically add resizing to the pipeline
pipeline.add(
    resize(width=100, height=100)
)

# Process and save the image
output_image = pipeline(input_image)
output_image.save('output.png')
```

## Conclusion

The Image Utils Package provides a versatile and cohesive image processing solution, whether accessed through CLI or Python. It supports a range of commands and operators, each with consistent input/output handling, making it easy to create powerful image processing pipelines. The CLI’s ability to chain commands and redirect output allows for streamlined command-line workflows, while the Python API offers robust tools for modular and reusable image processing in code.
