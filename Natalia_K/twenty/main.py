import os
import requests



open()
# FILE HANDLING MODE
# 'r' - Read mode (default)
# opens for file for reading only 
# it returns an error if the file does not exist

# f = open("example.txt", "r")
# content = f.read()
# print(content)
# f.close()


# 'w' - Write mode
# opens file for writing only
# it creates a new file if the file does not exist
# f = open("example.txt", "w")
# f.write("this is an example of file handling in python")
# f.close()

# 'a' - Append mode
# opens file for appending only
# it creates a new file if the file does not exist
# f = open("example.txt", "a")
# f.write("\nThis line is appended to the file.")
# f.close()

# 'x' - Exclusive creation mode
# opens file for exclusive creation
# it creates a new file if the file does not exist
# it returns an error if the file already exists

# try:
#     f = open("example.txt", "x")
#     f.write("This file is created using exclusive creation mode.")
#     f.close()
# except FileExistsError:
#     print("Error: The file 'example.txt' already exists. Please choose a different name or delete the existing file.")

# print("testing testing")

# binary mode
# 'rb' - Read binary mode
# opens file for reading in binary format


bird_image = requests.get("https://pixabay.com/get/g1deebd4bed5497fc6044d48bc19f8408e53061b42fba76479b2d767ed91a40730b4c477bb1615d7ee96453f4cbfb955b49a0b5d606f856e4a69f23cc60a80765_1920.jpg")
f = open("bird.png", "wb")
# f.write(bird_image.content)
print(bird_image.content)
