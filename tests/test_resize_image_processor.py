from PIL import Image
from io import BytesIO
from image_utils.operators import resize

def test_resize_operator():
    # Create an in-memory image
    original_image = Image.new("RGB", (200, 100), "blue")
    img_byte_arr = BytesIO()
    original_image.save(img_byte_arr, format='PNG')
    img_byte_arr = BytesIO(img_byte_arr.getvalue())

    # Test resizing
    operator = resize(100, 50)
    resized_image = operator(Image.open(img_byte_arr))

    assert resized_image.size == (100, 50)

def test_resize_operator_width_only():
    # Create an in-memory image
    original_image = Image.new("RGB", (200, 100), "blue")
    img_byte_arr = BytesIO()
    original_image.save(img_byte_arr, format='PNG')
    img_byte_arr = BytesIO(img_byte_arr.getvalue())

    # Test resizing with width only
    operator = resize(width=100)
    resized_image = operator(Image.open(img_byte_arr))

    assert resized_image.size == (100, 50)

def test_resize_operator_height_only():
    # Create an in-memory image
    original_image = Image.new("RGB", (200, 100), "blue")
    img_byte_arr = BytesIO()
    original_image.save(img_byte_arr, format='PNG')
    img_byte_arr = BytesIO(img_byte_arr.getvalue())

    # Test resizing with height only
    operator = resize(height=50)
    resized_image = operator(Image.open(img_byte_arr))

    assert resized_image.size == (100, 50)
