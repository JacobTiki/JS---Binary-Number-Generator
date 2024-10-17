binary = [0, 0, 0, 0]
def generateBinary(number):
    for i in range(4):
        if(number >= 8):
            binary[0] = 1
            number -= 8
        elif(number >= 4):
            binary[1] = 1
            number -= 4
        elif(number >= 2):
            binary[2] = 1
            number -= 2
        elif(number >= 1):
            binary[3] = 1
            number -= 1
    return binary 
generateBinary(6)
num = ""
for digit in binary:
    num = num + str(digit)
print(num)