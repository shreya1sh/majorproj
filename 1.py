# run this in any directory
# add -v for verbose
# get Pillow (fork of PIL) from
# pip before running -->
# pip install Pillow

# import required libraries
import os
import sys
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

image = plt.imread('F03_200.tif')
image = np.array(image)
image = image[:,:,1] #if RGB

print(image.shape)


for x in np.arange(0,image.shape[0]):
    for y in np.arange(image.shape[1]):
        if x+4 < image.shape[0] and y+4 < image.shape[1]:
            sum = np.sum(image[x:x+4,y:y+4])
            if sum > 4:
                image[x:x + 4, y:y + 4] = 1
            elif sum < 4:
                image[x:x + 4, y:y + 4] = 0

#photo = Image.open("F02_200.tif")
#photo.show()



def get_size(filename="F02_200.tif"):
    stat = os.stat(filename)
    size = stat.st_size
    return size


print(get_size())
# define a function for
# compressing an image
def compressMe(file, verbose=False):
    # Get the path of the file
    filepath = os.path.join(os.getcwd(),
                            'F02_200.tif')

    # open the image
    picture = Image.open(filepath)

    # Save the picture with desired quality
    # To change the quality of image,
    # set the quality variable at
    # your desired level, The more
    # the value of quality variable
    # and lesser the compression
    picture.save("Compressed_" + file,
                 "PNG",
                 optimize=True,
                 quality=10)
    return


# Define a main function
def main():
    verbose = False

    # checks for verbose flag
    if (len(sys.argv) > 1):

        if (sys.argv[1].lower() == "-v"):
            verbose = True

    # finds current working dir
    cwd = os.getcwd()

    formats = ( '.tif')

    # looping through all the files
    # in a current directory
    for file in os.listdir(cwd):


        if os.path.splitext(file)[1].lower() in formats:
            print('compressing', file)
            compressMe(file, verbose)


    print("Done")


# Driver code
if __name__ == "__main__":
    main()








    import re
    import numpy as np
    from PIL import Image

    print("Huffman Compression Program")
    print("=================================================================")
    h = int(input("Enter 1 if you want to input an colour image file, 2 for default gray scale case:"))
    if h == 1:
        file = input("Enter the filename:")
        my_string = np.asarray(Image.open(file), np.uint8)
        shape = my_string.shape
        a = my_string
        print("Enetered string is:", my_string)
        my_string = str(my_string.tolist())
    elif h == 2:
        array = np.arange(0, 737280, 1, np.uint8)
        my_string = np.reshape(array, (1024, 720))
        print("Entered string is:", my_string)
        a = my_string
        my_string = str(my_string.tolist())

    else:
        print("You entered invalid input")  # taking user input

    letters = []
    only_letters = []
    for letter in my_string:
        if letter not in letters:
            frequency = my_string.count(letter)  # frequency of each letter repetition
            letters.append(frequency)
            letters.append(letter)
            only_letters.append(letter)

    nodes = []
    while len(letters) > 0:
        nodes.append(letters[0:2])
        letters = letters[2:]  # sorting according to frequency
    nodes.sort()
    huffman_tree = []
    huffman_tree.append(nodes)  # Make each unique character as a leaf node


    def combine_nodes(nodes):
        pos = 0
        newnode = []
        if len(nodes) > 1:
            nodes.sort()
            nodes[pos].append("1")  # assigning values 1 and 0
            nodes[pos + 1].append("0")
            combined_node1 = (nodes[pos][0] + nodes[pos + 1][0])
            combined_node2 = (nodes[pos][1] + nodes[pos + 1][1])  # combining the nodes to generate pathways
            newnode.append(combined_node1)
            newnode.append(combined_node2)
            newnodes = []
            newnodes.append(newnode)
            newnodes = newnodes + nodes[2:]
            nodes = newnodes
            huffman_tree.append(nodes)
            combine_nodes(nodes)
        return huffman_tree  # huffman tree generation


    newnodes = combine_nodes(nodes)

    huffman_tree.sort(reverse=True)
    print("Huffman tree with merged pathways:")

    checklist = []
    for level in huffman_tree:
        for node in level:
            if node not in checklist:
                checklist.append(node)
            else:
                level.remove(node)
    count = 0
    for level in huffman_tree:
        print("Level", count, ":", level)  # print huffman tree
        count += 1
    print()

    letter_binary = []
    if len(only_letters) == 1:
        lettercode = [only_letters[0], "0"]
        letter_binary.append(lettercode * len(my_string))
    else:
        for letter in only_letters:
            code = ""
            for node in checklist:
                if len(node) > 2 and letter in node[1]:  # genrating binary code
                    code = code + node[2]
            lettercode = [letter, code]
            letter_binary.append(lettercode)
    print(letter_binary)
    print("Binary code generated:")
    for letter in letter_binary:
        print(letter[0], letter[1])

    bitstring = ""
    for character in my_string:
        for item in letter_binary:
            if character in item:
                bitstring = bitstring + item[1]
    binary = "0b" + bitstring
    print("Your message as binary is:")
    # binary code generated

    uncompressed_file_size = len(my_string) * 7
    compressed_file_size = len(binary) - 2
    print("Your original file size was", uncompressed_file_size, "bits. The compressed size is:", compressed_file_size)
    print("This is a saving of ", uncompressed_file_size - compressed_file_size, "bits")
    output = open("compressed.txt", "w+")
    print("Compressed file generated as compressed.txt")
    output = open("compressed.txt", "w+")
    print("Decoding.......")
    output.write(bitstring)