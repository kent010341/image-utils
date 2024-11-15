# Image Utils Package

**Image Utils** is a powerful and versatile package for image processing, designed to simplify common tasks such as cropping, resizing, rotating, and more. Whether you're working from the command line or integrating it into Python projects, Image Utils provides an intuitive interface with robust capabilities.

---

## Key Features

- **Comprehensive Command-Line Tools**: Perform image transformations with simple, easy-to-remember commands.
- **Flexible Input/Output**: Supports piping, file-based input/output, and interactive file pickers.
- **Modular Design**: Chain multiple operations together to create complex image processing workflows.
- **Python Integration**: Use as a Python library for advanced and customizable pipelines.

---

## Installation

Install the package locally using `pip`:

```bash
pip install .
```

---

## Quick Start

### Command-Line Example

1. Resize an image to 100x100 pixels and save the result:

    ```bash
    image-utils resize 100x100 --input input.png > output.png
    ```

2. **Chain multiple commands: crop and then rotate an image:**

    ```bash
    image-utils crop --left 10 --top 10 --right 200 --bottom 200 --input input.png | \
    image-utils rotate 45 --fillwith "#FFFFFF" > output.png
    ```

3. **Prepare an image for Telegram stickers:**

    Telegram requires sticker images to be 512x512 pixels, and typically users prefer stickers to have minimal transparent padding. This example trims the image to its non-transparent area and resizes it to 512x512. A file picker will appear if `--input` is not provided.

    ```bash
    image-utils trim | image-utils resize 512x512 > sticker.png
    ```

   **Steps**:
   - The `trim` command removes any transparent padding around the image.
   - The `resize` command ensures the image meets Telegram's size requirement.

   Run the command, and select the input file when prompted by the file picker.

### Python Example

Programmatically apply a series of transformations:

```python
from PIL import Image
from image_utils.operators import crop, resize, rotate
from image_utils.pipeline import pipe

# Load an image
input_image = Image.open("input.png")

# Create a processing pipeline
pipeline = pipe(
    crop(left=10, top=10, right=200, bottom=200),
    resize(width=100, height=100),
    rotate(angle=45, fillwith="#FFFFFF")
)

# Process the image and save the result
output_image = pipeline.process(input_image)
output_image.save("output.png")
```
---

## Available Commands

| Command | Rescription |
| - | - |
| `resize` | Resize an image to specified dimensions. |
| `crop` | Crop an image to a specified rectangular area. |
| `trim` | Remove transparent borders from an image. |
| `roll` | Roll (shift) the image horizontally/vertically. |
| `gray_scale` | Convert an image to grayscale. |
| `expand` | Expand the canvas of an image. |
| `rotate` | Rotate an image with canvas expansion. |
| `flip` | Flip an image horizontally or vertically. |

---

## Why Choose Image Utils?

1. Ease of Use: Simple CLI commands and Python APIs for seamless integration.
2. Performance: Built with robust libraries like Pillow for reliable and efficient processing.
3. Flexibility: Suitable for both ad-hoc tasks and complex workflows.
4. Open Source: Designed to be extensible and welcoming to contributions from the open-source community.

---

## Documentation

* [Usage Guide](docs/usage.md): Detailed instructions and examples for all commands.
* [Operator Reference](docs/operators/): Specific documentation for each operator.

---

## License

This project is licensed under the terms of the [LICENSE](LICENSE).
