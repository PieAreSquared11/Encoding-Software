from classes_and_functions import *

interpret = Interpret("key.txt")

print(Encode(interpret.key, input("encode data . . . ")).string_data)
print(Decode(interpret.key, input("decode data . . . ")).string_data)