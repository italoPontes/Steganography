import unittest
import numpy as np
import sys
import os
# Add the "src" directory to the Python module search path
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.insert(0, src_path)
# Now you can import the steganography module
from steganography import Steganography


class TestSteganography(unittest.TestCase):

    def setUp(self):
        # Create an instance of the Steganography class
        self.steganography = Steganography()

        # Create test images
        self.embedded_image = np.zeros((100, 100, 3), dtype=np.uint8)
        self.hidden_image = np.random.randint(0, 256,
                                              (50, 50, 3),
                                              dtype=np.uint8)

    def test_get_coordinates_from_position(self):
        row, column = self.steganography.get_coordinates_from_position(10, 100)
        self.assertEqual(row, 0)
        self.assertEqual(column, 10)

    def test_get_binary(self):
        binary = self.steganography.get_binary(10, 32)
        self.assertEqual(binary, '00000000000000000000000000001010')
        binary = self.steganography.get_binary(11, 32)
        self.assertEqual(binary, '00000000000000000000000000001011')

    def test_modify_last_bit(self):
        modified_pixel = self.steganography.modify_last_bit(10, 0)
        self.assertEqual(modified_pixel, 10)
        modified_pixel = self.steganography.modify_last_bit(10, 1)
        self.assertEqual(modified_pixel, 11)
        modified_pixel = self.steganography.modify_last_bit(10, -1)
        self.assertEqual(modified_pixel, 10)
        modified_pixel = self.steganography.modify_last_bit(10, 3)
        self.assertEqual(modified_pixel, 10)

    def test_get_resolution(self):
        width, height, resolution = \
            self.steganography.get_resolution(self.embedded_image)
        self.assertEqual(width, 100)
        self.assertEqual(height, 100)
        self.assertEqual(resolution, 10000)

    def test_resize_embedded_image(self):
        resized_image = \
            self.steganography.resize_embedded_image(self.embedded_image,
                                                     self.hidden_image)
        self.assertEqual(resized_image.shape[:2], (300, 300))

    def test_embed_header(self):
        steganography_image = \
            self.steganography.embed_header(self.embedded_image,
                                            self.hidden_image)
        width = self.steganography.get_header(steganography_image, 100, 0)
        height = self.steganography.get_header(steganography_image, 100, 1)
        self.assertEqual(width, 50)
        self.assertEqual(height, 50)

    def test_encoden_n_decode_image(self):
        encoded_image = \
            self.steganography.encode(self.embedded_image,
                                      self.hidden_image)
        secret_image = self.steganography.decode(encoded_image)
        self.assertTrue(np.array_equal(self.hidden_image, secret_image))

    def test_get_hidden_image(self):
        encoded_image = \
            self.steganography.encode(self.embedded_image,
                                      self.hidden_image)
        hidden_image = self.steganography.get_hidden_image(encoded_image,
                                                           50, 50, 300)
        self.assertTrue(np.array_equal(self.hidden_image, hidden_image))


if __name__ == '__main__':
    unittest.main()
