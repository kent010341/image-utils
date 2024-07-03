# Image Utils Package

A versatile package for image processing utilities, offering various command-line tools for image manipulation. The package supports piping and redirection of input and output, making it easy to integrate into automated workflows.

## Installation

To install the package locally using `pip`, navigate to the project directory and run:

```bash
pip install .
```

## Command Usage

### Resize Command
Resize an image to the specified dimensions.

#### Usage
```bash
image-utils resize [OPTIONS] SIZE
```

#### Options
- `-i, --input`: Path to the input image. If not provided, the command will prompt you to select an image file.

#### Examples

1. Resize an image to 100x100 pixels:  
   ```bash
   image-utils resize 100x100 -i input.jpg > output.jpg
   ```
2. Resize an image to 100 pixels wide, maintaining aspect ratio:  
   ```bash
   image-utils resize 100x -i input.jpg > output.jpg
   ```
3. Resize an image to 50 pixels high, maintaining aspect ratio:  
   ```bash
   image-utils resize x50 -i input.jpg > output.jpg
   ```
4. Resize an image by piping the input:  
   ```bash
   cat input.jpg | image-utils resize 100x100 > output.jpg
   ```

### Crop Command
Crop an image to its bounding box and convert it to a square with optional alignment.

#### Usage
```bash
image-utils crop [OPTIONS]
```

#### Options
- `-i, --input`: Path to the input image. If not provided, the command will prompt you to select an image file.
- `-a, --align`: Align the cropped image in the square. Choices are top, bottom, left, right, center. Default is center.

#### Examples
1. Crop an image to a square, centered:  
   ```bash
   image-utils crop -i input.png --align center > output.png
   ```
2. Crop an image to a square, aligned to the top:  
   ```bash
   image-utils crop -i input.png --align top > output.png
   ```
3. Crop an image by piping the input:  
   ```bash
   cat input.png | image-utils crop --align center > output.png
   ```

### Combining Commands

You can use the commands together with pipes (`|`) to chain operations. For example:

1. Crop an image and then resize it:  
   ```bash
   image-utils crop -i input.png --align center | image-utils resize 100x100 > output.png
   ```
2. Resize an image and then crop it:  
   ```bash
   image-utils resize 200x200 -i input.jpg | image-utils crop --align top > output.png
   ```

## Usage as a Python Package

You can also use the `image-utils` as a library in your Python projects to leverage its image processing capabilities. Below is an example of how to use the package programmatically:

#### Example Usage

Here's an example demonstrating how to use the package to apply a sequence of image processing operations:  

```python
from PIL import Image
from image_utils.operators import crop, resize
from image_utils.pipeline import pipe

# Load an image
input_image = Image.open('input.png')

# Create a pipeline and process the image
pipeline = pipe(
    crop(align='center'),
    resize(width=100, height=100)
)

output_image = pipeline.process(input_image)

# Save the processed image
output_image.save('output.png')
```

### Creating Custom Pipelines

ou can create custom pipelines by chaining multiple operators together. Each operator modifies the image and passes it to the next operator in the pipeline.

```python
from PIL import Image
from image_utils.operators import crop, resize
from image_utils.pipeline import pipe

# Load an image
input_image = Image.open('input.png')

# Define a custom pipeline
pipeline = pipe(
    crop(align='center'),
    resize(width=200)
)

# Process the image
output_image = pipeline.process(input_image)

# Save the processed image
output_image.save('output.png')
```

### Using with Custom Operators

You can also create your own custom operators by subclassing `ImageOperator` and adding them to the pipeline.

```python
from PIL import Image
from image_utils.operators.image_operator import ImageOperator
from image_utils.pipeline import pipe

class CustomOperator(ImageOperator):
    def __call__(self, image: Image.Image) -> Image.Image:
        # Custom image processing logic here
        return image

# Load an image
input_image = Image.open('input.png')

# Create a pipeline with the custom operator
pipeline = pipe(
    CustomOperator()
)

# Process the image
output_image = pipeline.process(input_image)

# Save the processed image
output_image.save('output.png')
```

### Adding More Operators to an Existing Pipeline

You can extend an existing pipeline by adding more operators using the `add` method.

```python
from PIL import Image
from image_utils.operators import crop, resize
from image_utils.pipeline import pipe

# Load an image
input_image = Image.open('input.png')

# Create a pipeline
pipeline = pipe(
    crop(align='center')
)

# Add more operators to the pipeline
pipeline.add(
    resize(width=100, height=100)
)

# Process the image
output_image = pipeline.process(input_image)

# Save the processed image
output_image.save('output.png')
```

## Conclusion

The Image Utils Package provides flexible command-line tools for image processing. With support for piping and redirection, it can easily be integrated into larger workflows and automated scripts. Additionally, the package can be used as a library within Python projects, offering a versatile and modular approach to image processing.

By utilizing the Pipeline Design Pattern, the package allows you to chain multiple image processing operations in a clear and maintainable way. This design pattern ensures that each operation is a modular and reusable component, making it easy to create complex image processing workflows. You can also extend existing pipelines by adding more operators, providing great flexibility and scalability.

For any questions or issues, feel free to open an issue on the [GitHub repository](https://github.com/kent010341/image-utils).
