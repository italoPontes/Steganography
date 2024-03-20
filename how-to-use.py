import cv2
import argparse
from src.steganography import Steganography

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Steganography - Hide and ' \
                                 'Extract Secret Messages in Images.')

# Add subparsers for encode and decode modes
subparsers = parser.add_subparsers(dest='mode',
                                   help='Choose encode or decode mode.')

# Subparser for encode mode
encode_parser = subparsers.add_parser('encode',
                                      help='Encode a message into an image')
encode_parser.add_argument('-secret_image',
                           type=str,
                           help='Input image to be hidden.',
                           default='data/secret-image.jpg')
encode_parser.add_argument('-cover_image',
                           type=str,
                           help='Input image to cover the secret image.',
                           default='data/Monalisa.png')
encode_parser.add_argument('-output_image',
                           type=str,
                           help='Output image file with secret image.',
                           default='data/steganography-image.png')

# Subparser for decode mode
decode_parser = subparsers.add_parser('decode',
                                      help='Decode a hidden message ' \
                                           'from an image.')
decode_parser.add_argument('-steganography_image',
                           type=str,
                           help='Input image file with hidden message.',
                           default='data/steganography-image.png')
decode_parser.add_argument('-secret_image',
                           type=str,
                           help='Secret image retrieved from input image.',
                           default='data/retrieved-image.png')

# Parse the command-line arguments
args = parser.parse_args()

model = Steganography()

# Access the values of the parameters
if args.mode == 'encode':
    cover_image = args.cover_image
    secret_image = args.secret_image
    output_image = args.output_image

    cover_img = cv2.imread(cover_image)
    secret_img = cv2.imread(secret_image)

    encoded_img = model.encode(cover_img, secret_img)
    
    cv2.imwrite(output_image, encoded_img)
    
elif args.mode == 'decode':
    steganography_image = args.steganography_image
    secret_image = args.secret_image

    steganography_img = cv2.imread(steganography_image)

    retrieved_img = model.decode(steganography_img)

    cv2.imwrite(secret_image, retrieved_img)
