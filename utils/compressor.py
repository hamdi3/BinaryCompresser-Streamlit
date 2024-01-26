import ctypes
import os

# Load the library
if os.name == 'nt':
    compressor_lib = ctypes.CDLL("data/libs/compressor_enc_lib.dll")
elif os.name == 'posix':
    compressor_lib = ctypes.CDLL("data/libs/compressor_enc_lib.so")

# Specify the functions
file_to_binary_string = compressor_lib.file_to_binary_string
binary_string_to_file = compressor_lib.binary_string_to_file

# Specify the argument types
file_to_binary_string.argtypes = [ctypes.c_char_p,ctypes.c_char_p, ctypes.c_char_p]
binary_string_to_file.argtypes = [ctypes.c_char_p,ctypes.c_char_p, ctypes.c_char_p]