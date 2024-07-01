from PIL import Image
from io import BytesIO
from image_utils.processors.resize_image_processor import ResizeImageProcessor

def test_resize_image_processor():
    # Create an in-memory image
    original_image = Image.new("RGB", (200, 100), "blue")
    img_byte_arr = BytesIO()
    original_image.save(img_byte_arr, format='PNG')
    img_byte_arr = BytesIO(img_byte_arr.getvalue())

    # Test resizing
    processor = ResizeImageProcessor(size='100x50')
    processor.input_image = Image.open(img_byte_arr)
    processor.format = 'PNG'
    resized_image = processor.process()

    assert resized_image.size == (100, 50)

def test_resize_image_processor_width_only():
    # Create an in-memory image
    original_image = Image.new("RGB", (200, 100), "blue")
    img_byte_arr = BytesIO()
    original_image.save(img_byte_arr, format='PNG')
    img_byte_arr = BytesIO(img_byte_arr.getvalue())

    # Test resizing with width only
    processor = ResizeImageProcessor(size='100x')
    processor.input_image = Image.open(img_byte_arr)
    processor.format = 'PNG'
    resized_image = processor.process()

    assert resized_image.size == (100, 50)

def test_resize_image_processor_height_only():
    # Create an in-memory image
    original_image = Image.new("RGB", (200, 100), "blue")
    img_byte_arr = BytesIO()
    original_image.save(img_byte_arr, format='PNG')
    img_byte_arr = BytesIO(img_byte_arr.getvalue())

    # Test resizing with height only
    processor = ResizeImageProcessor(size='x50')
    processor.input_image = Image.open(img_byte_arr)
    processor.format = 'PNG'
    resized_image = processor.process()

    assert resized_image.size == (100, 50)
