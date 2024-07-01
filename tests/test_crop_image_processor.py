from PIL import Image
from io import BytesIO
from image_utils.processors.crop_image_processor import CropImageProcessor

def test_crop_image_processor_center():
    # Create an in-memory image with a transparent border
    original_image = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
    for i in range(75, 150):
        for j in range(50, 150):
            original_image.putpixel((i, j), (255, 0, 0, 255))
    
    img_byte_arr = BytesIO()
    original_image.save(img_byte_arr, format='PNG')
    img_byte_arr = BytesIO(img_byte_arr.getvalue())

    # Test cropping
    processor = CropImageProcessor(input_path=None, align='center')
    processor.input_image = Image.open(img_byte_arr)
    processor.format = 'PNG'
    cropped_image = processor.process()

    assert cropped_image.size == (100, 100)
    assert cropped_image.getpixel((0, 0)) == (0, 0, 0, 0)
    assert cropped_image.getpixel((50, 50)) == (255, 0, 0, 255)

def test_crop_image_processor_top():
    # Create an in-memory image with a transparent border
    original_image = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
    for i in range(75, 150):
        for j in range(50, 150):
            original_image.putpixel((i, j), (255, 0, 0, 255))
    
    img_byte_arr = BytesIO()
    original_image.save(img_byte_arr, format='PNG')
    img_byte_arr = BytesIO(img_byte_arr.getvalue())

    # Test cropping
    processor = CropImageProcessor(input_path=None, align='top')
    processor.input_image = Image.open(img_byte_arr)
    processor.format = 'PNG'
    cropped_image = processor.process()

    assert cropped_image.size == (100, 100)
    assert cropped_image.getpixel((0, 0)) == (0, 0, 0, 0)
    assert cropped_image.getpixel((50, 0)) == (255, 0, 0, 255)
