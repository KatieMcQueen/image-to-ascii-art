from PIL import Image
imageName = input("Enter the name of the image to open: ")
im = Image.open(imageName)
im = im.resize((400,100), reducing_gap=3.0)
table = ['`', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '~', '+',
              '_', '-', '?', ']', '[', '}', '{', '1', ')', '(', '|', '\\',
              '/', 't', 'f', 'j', 'r', 'x', 'n', 'u', 'v', 'c', 'z', 'X',
              'Y', 'U', 'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q',
              'p', 'd', 'b', 'k', 'h', 'a', 'o', '*', '#', 'M', 'W', '&',
              '8', '%', 'B', '@', '$']
scalar = (len(table)-1)/256
#print(im)
#print(list(im.getdata()))

def getPixelMatrix(img):
    pixels = list(img.getdata())
    matrix = []
    for i in range(0, len(pixels), img.width):
        matrix.append(pixels[i:i+img.width])
    return matrix

def brightnessConvert(matrix, alg="avg"):
    monoMatrix = []
    for row in matrix:
        monoRow = []
        for p in row:
            brightness = (p[0] + p[1] + p[2]) / 3
            brightness = int(256-brightness)
            monoRow.append(brightness)
        monoMatrix.append(monoRow)
    return(monoMatrix)

def bright2ascii(bright):
    bright = float(bright)
    adjusted = round(bright * scalar)
    return table[adjusted]

def matrix2ascii(matrix):
    newMatrix = []
    for row in matrix:
        newRow = []
        for bright in row:
            char = bright2ascii(bright)
            newRow.append(char)
        newMatrix.append(newRow)
    return(newMatrix)

def printMatrix(matrix):
    print('\n')
    for row in matrix:
        for p in row:
            print(p, end='')
        print()

pixelMatrix = getPixelMatrix(im)
brightMatrix = brightnessConvert(pixelMatrix)
asciiMatrix = matrix2ascii(brightMatrix)
printMatrix(asciiMatrix)
