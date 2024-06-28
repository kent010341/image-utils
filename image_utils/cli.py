import argparse
from .processors.resize_image_processor import ResizeImageProcessor
from .processors.crop_image_processor import CropImageProcessor

def main():
    parser = argparse.ArgumentParser(prog='image-utils', description='A command-line tool for image processing.')
    subparsers = parser.add_subparsers(dest='command')

    # Resize subcommand
    resize_parser = subparsers.add_parser('resize', help='Resize an image')
    resize_processor = ResizeImageProcessor(resize_parser)

    # Crop subcommand
    crop_parser = subparsers.add_parser('crop', help='Crop an image')
    crop_processor = CropImageProcessor(crop_parser)

    args = parser.parse_args()

    if args.command == 'resize':
        resize_processor.run()
    elif args.command == 'crop':
        crop_processor.run()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
