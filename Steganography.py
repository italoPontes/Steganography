import cv2
import math
import numpy as np

class Steganography:
    def get_coordinates_from_position(self, pixel_position: int() = 0, width: int() = 0):
        """
        Calculates the row and column coordinates from pixel position and width.

        Args:
            pixel_position (int): The pixel position.
            width (int): The width of the grid.

        Returns:
            row, column (int, int): A tuple containing the row and column coordinates.
        """
        if (pixel_position == 0) or (width == 0):
            return 0, 0

        row = pixel_position // width
        column = pixel_position % width

        return row, column


    def from_binary_to_decimal(self, binary: str() = '0') -> int:
        """
        Converts binary number to decimal integer.

        Args:
            binary (str): Binary string.

        Returns:
            int: Decimal integer.
            
        Examples:
            >>> from_binary_to_decimal('00000001')
            1
            >>> from_binary_to_decimal('00001010')
            10
            >>> from_binary_to_decimal('01100100')
            100
        """
        decimal = 0
        for i, bit in enumerate(reversed(binary)):
            if bit == '1':
                decimal += 2 ** i
        return decimal


    def get_binary(self, pixel_value: int() = 0,
                    size: int() = 8) -> str:
        """
        Converts an integer to a binary string representation.

        Args:
            pixel_value (int): The integer value to convert.
            size (int): The size of the binary string.

        Returns:
            str: The binary string representation of the integer.

        Examples:
            >>> get_binary(1)
            '00000001'
            >>> get_binary(10)
            '00001010'
            >>> get_binary(100)
            '01100100'
        """
        if size == 32:
            return f"{pixel_value:032b}"
        return f"{pixel_value:08b}"


    def modify_last_bit(self, pixel_value: int() = 0,
                        new_last_bit: int() = 0) -> int():
        """
        Modifies the last bit of a pixel value.

        Args:
            pixel_value (int): The original pixel value (0 to 255).
            new_last_bit (int): The new value for the last bit (0 or 1).

        Returns:
            int: The modified pixel value if the new last bit is 0 or 1, otherwise returns the original pixel value.

        Example:
            >>> modify_last_bit(10, 1)
            11

        Explanation:
            The binary representation of pixel_value is '00001010',
            and the last bit will be replaced by the new_last_bit: '00001011',
            which is equivalent to 11 in integer.
        """
        new_last_bit = int(new_last_bit)
        if new_last_bit not in {0, 1}:
            return pixel_value
        output_value = (pixel_value & -2) | (new_last_bit & 1)
        return output_value


    def get_resolution(self, image: np.array([]) = []):
        """
        Calculates the width, height, and resolution of the input image.

        Args:
            image (numpy.array): The input image.

        Returns:
            tuple: A tuple containing the width, height, and resolution of the image.
        """
        height, width = image.shape[:2]
        resolution = height * width
        return width, height, resolution


    def resize_embedded_image(self, embedded_image: np.array([]) = [],
                                hidden_image: np.array([]) = [],
                                pixel_size: int() = 8,
                                header_size: int() = 32):
        """
        Resizes the embedded image if necessary to accommodate the hidden image.

        Args:
            embedded_image (numpy.array): Image used to hide another image.
            hidden_image (numpy.array): Image to be hidden.
            pixel_size (int): Size of each pixel in bits.
            header_size (int): Size of the header in bits.

        Returns:
            numpy.array: Resized embedded image if necessary.

        Raises:
            ValueError: If the hidden image is larger than the embedded image.
        """
        dst_width, dst_height, dst_resolution = self.get_resolution(embedded_image)
        _, _, src_resolution = self.get_resolution(hidden_image)

        total_bits_required = (src_resolution * pixel_size) + header_size
        proportion_factor = math.ceil(total_bits_required / dst_resolution)

        if proportion_factor < 1:
            return embedded_image

        new_width = proportion_factor * dst_width
        new_height = proportion_factor * dst_height

        embedded_image_resized = cv2.resize(embedded_image,
                                    dsize=(new_width, new_height))
        
        return embedded_image_resized


    def embed_header(self, embedded_image: np.array([]) = [],
                            hidden_image: np.array([]) = [],
                            header_size: int() = 32):
        """
        Embeds information from the hidden image into the embedded image.

        Args:
            embedded_image (numpy.array): Image used to hide another image.
            hidden_image (numpy.array): Image to be hidden.
            header_size (int): Size of the header in bits.

        Returns:
            numpy.ndarray: Embedded image with hidden information.
        """
        if not isinstance(embedded_image, np.ndarray) or not isinstance(hidden_image, np.ndarray):
            raise TypeError("Both embedded_image and hidden_image must be numpy arrays.")

        # Get resolutions of both images
        src_width, src_height, _ = self.get_resolution(hidden_image)
        dst_width, _, _ = self.get_resolution(embedded_image)

        # Embed header information
        for dimension, channel in zip([src_height, src_width], [0, 1]):
            binary_value = self.get_binary(dimension, header_size)
            for position in range(header_size):
                bit = int(binary_value[position])
                # Get coordinates in the embedded image
                row, column = self.get_coordinates_from_position(position, dst_width)
                # Modify the last bit of the pixel value in the embedded image
                pixel_value_dst = embedded_image[row, column, channel]
                pixel_value_dst = self.modify_last_bit(pixel_value_dst, bit)
                embedded_image[row, column, channel] = pixel_value_dst

        return embedded_image


    def encode_image(self, hidden_image: np.ndarray([]) = [], embedded_image: np.ndarray([]) = [],
                    header_size: int() = 32, depth: int() = 3, pixel_size: int() = 8):
        """
        Encodes the hidden image into the embedded image.

        Args:
            hidden_image (numpy.ndarray): Image to be hidden.
            embedded_image (numpy.ndarray): Image used to hide another image.
            header_size (int): Size of the header in bits.
            depth (int): Number of color channels in the images.
            pixel_size (int): Size of each pixel in bits.

        Returns:
            numpy.ndarray: Encoded image with hidden information.
        """
        if not isinstance(hidden_image, np.ndarray) or not isinstance(embedded_image, np.ndarray):
            raise TypeError("Both hidden_image and embedded_image must be numpy arrays.")

        src_width, _, src_resolution = self.get_resolution(hidden_image)
        dst_width, _, _ = self.get_resolution(embedded_image)
            
        encoded_image = embedded_image.copy()
        for channel in range(depth):
            for pixel_position_src in range(src_resolution):
                row_src, column_src = self.get_coordinates_from_position(pixel_position_src, src_width)
                pixel_value_src = hidden_image[row_src, column_src, channel]
                pixel_value_src = self.get_binary(pixel_value_src, pixel_size)
                jump_size = (pixel_position_src * pixel_size)

                for bit_position in range(pixel_size):
                    dst_position = header_size + jump_size + bit_position
                    row_dst, column_dst = self.get_coordinates_from_position(dst_position, dst_width)
                    pixel_value_dst = embedded_image[row_dst, column_dst, channel]
                    pixel_value_dst = self.modify_last_bit(pixel_value_dst, pixel_value_src[bit_position])
                    encoded_image[row_dst, column_dst, channel] = pixel_value_dst
        return encoded_image

    def encode(self, embedded_image: np.array([]) = [], hidden_image: np.array([]) = [],
                header_size: int() = 32, pixel_size: int() = 8,
                depth: int() = 3):
        """
        Encodes the hidden image into the embedded image.

        Args:
            embedded_image (numpy.ndarray): Image used to hide another image.
            hidden_image (numpy.ndarray): Image to be hidden.

        Returns:
            numpy.ndarray: Encoded image with hidden information.
        """
        embedded_image = self.resize_embedded_image(embedded_image = embedded_image,
                                                    hidden_image = hidden_image,
                                                    pixel_size = pixel_size,
                                                    header_size = header_size)

        embedded_image = self.embed_header(embedded_image = embedded_image,
                                                hidden_image = hidden_image,
                                                header_size = header_size)

        encoded_image = self.encode_image(hidden_image = hidden_image,
                                            embedded_image = embedded_image,
                                            header_size = header_size,
                                            depth = depth,
                                            pixel_size = pixel_size)

        return encoded_image


    



    



    def get_header(self, image: np.array([]) = [],
                    width: int() = 0,
                    header_size: int() = 0,
                    channel: int() = 0):
        """
        Retrieves the header information from the image.

        Args:
            image (numpy.ndarray): The input image.
            width (int): The width of the image.
            header_size (int): The size of the header in bits.
            channel (int): The color channel to extract the header information from.

        Returns:
            int: The decimal value of the header information.
        """
        if not isinstance(image, np.ndarray):
            raise TypeError("The image must be a numpy array.")

        if header_size <= 0 or header_size > width:
            raise ValueError("Header size must be a positive integer less than or equal to the width.")

        if channel < 0 or channel >= image.shape[2]:
            raise ValueError("Invalid channel value.")

        dimension = ""
        for position in range(header_size):
            row, column = self.get_coordinates_from_position(position, width)
            pixel_value = image[row, column, channel]
            last_bit = str(pixel_value % 2)
            dimension += last_bit
            
        dimension = self.from_binary_to_decimal(dimension)
        return dimension


    def get_hidden_image(self, embedded_image: np.array([]) = [],
                            src_width: int() = 0,
                            src_height: int() = 0,
                            dst_width: int() = 0,
                            depth: int() = 3,
                            header_size: int() = 0,
                            pixel_size: int() = 0) -> np.array([]):
        """
        Retrieves the image channel from the embedded image.

        Args:
            src_width (int): The width of the source image.
            src_height (int): The height of the source image.
            dst_width (int): The width of the destination image.
            depth (int): Number of color channels in the images.
            header_size (int): Size of the header in bits.
            pixel_size (int): Size of each pixel in bits.

        Returns:
            numpy.ndarray: Image channel extracted from the embedded image.
        """
        if not all(isinstance(param, int) and param > 0 for param in [src_width, src_height, dst_width, depth, header_size, pixel_size]):
            raise ValueError("All parameters must be positive integers.")

        src_resolution = src_width * src_height
        image = np.ndarray(shape = (src_height, src_width, depth), dtype=int)

        for channel in range(depth):
            for pixel_position in range(src_resolution):
                pixel_position_dst = header_size + (pixel_position * pixel_size)
                pixel_value_src = ""
                for pixel_bit in range(pixel_size):
                    dst_row, dst_column = self.get_coordinates_from_position(pixel_position_dst + pixel_bit, dst_width)
                    pixel_value_dst = embedded_image[dst_row, dst_column, channel]
                    last_bit = str(pixel_value_dst % 2)
                    pixel_value_src += last_bit
                pixel_value_src = self.from_binary_to_decimal(pixel_value_src)
                src_row, src_column = self.get_coordinates_from_position(pixel_position, src_width)
                image[src_row, src_column, channel] = pixel_value_src
                
        return image

    def decode(self, encoded_image: np.array([]) = [], header_size: int() = 32,
                pixel_size: int() = 8, depth: int() = 3):
        """
        Decodes the hidden image from the encoded image.

        Args:
            encoded_image (numpy.ndarray): Image with hidden information.
            header_size (int): Size of the header in bits.
            pixel_size (int): Size of each pixel in bits.
            depth (int): Number of color channels in the images.

        Returns:
            numpy.ndarray: Decoded hidden image.
        """
        dst_width = encoded_image.shape[1]
        
        src_height = self.get_header(encoded_image, dst_width,
                                header_size, channel = 0)

        src_width = self.get_header(encoded_image, dst_width,
                                header_size, channel = 1)
        
        output_image = self.get_hidden_image(embedded_image = encoded_image,
                                            src_width = src_width,
                                            src_height = src_height,
                                            dst_width = dst_width,
                                            depth = depth,
                                            header_size = header_size,
                                            pixel_size = pixel_size)
        return output_image