from Steganography import create_image

message = 'Faculty of Computers and Artificial Intelligence Helwan University'
create_image(message, 'original_image.png', 'secret_image.png')