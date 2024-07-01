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

## Combining Commands

You can use the commands together with pipes (`|`) to chain operations. For example:

1. Crop an image and then resize it:  
   ```bash
   image-utils crop -i input.png --align center | image-utils resize 100x100 > output.png
   ```
2. Resize an image and then crop it:  
   ```bash
   image-utils resize 200x200 -i input.jpg | image-utils crop --align top > output.png
   ```

## Conclusion

The Image Utils Package provides flexible command-line tools for image processing. With support for piping and redirection, it can easily be integrated into larger workflows and automated scripts.  
For any questions or issues, feel free to open an issue on the [GitHub repository](https://github.com/kent010341/image-utils).
