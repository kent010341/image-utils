from PIL import Image
from io import BytesIO
from image_utils.operators import crop

def test_crop_operator_center():
    # Create an in-memory image with a transparent border
    original_image = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
    for i in range(50, 150):
        for j in range(50, 150):
            original_image.putpixel((i, j), (255, 0, 0, 255))
    
    img_byte_arr = BytesIO()
    original_image.save(img_byte_arr, format='PNG')
    img_byte_arr = BytesIO(img_byte_arr.getvalue())

    # Test cropping
    operator = crop(align='center')
    cropped_image = operator(Image.open(img_byte_arr))

    assert cropped_image.size == (100, 100)
    assert cropped_image.getpixel((0, 0)) == (255, 0, 0, 255)
    assert cropped_image.getpixel((50, 50)) == (255, 0, 0, 255)

def test_crop_operator_top():
    # Create an in-memory image with a transparent border
    original_image = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
    for i in range(50, 150):
        for j in range(50, 150):
            original_image.putpixel((i, j), (255, 0, 0, 255))
    
    img_byte_arr = BytesIO()
    original_image.save(img_byte_arr, format='PNG')
    img_byte_arr = BytesIO(img_byte_arr.getvalue())

    # Test cropping with top alignment
    operator = crop(align='top')
    cropped_image = operator(Image.open(img_byte_arr))

    assert cropped_image.size == (100, 100)
    assert cropped_image.getpixel((0, 0)) == (255, 0, 0, 255)
    assert cropped_image.getpixel((50, 0)) == (255, 0, 0, 255)
