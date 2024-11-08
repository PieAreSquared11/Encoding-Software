class Interpret:
    key = []

    def __init__(self, file):
        file = open(file)
        content = file.readlines()

        for line in content:
            self.sort_data(line)

    def sort_data(self, line):
        l_content = line.split(" ")

        operators = [list(item).pop(0) for item in l_content]
        numbers = [float(item[1:]) for item in l_content]

        self.key.append(list(zip(operators, numbers)))

class Encode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.key_len = len(key)
        self.current_pointer_add = 0
        self.string_data = ""

        #pointers as to where currently am in key
        self.pointers = [0 for i in range(len(self.key[0]))]

        self.end_data = []

        for letter in data:
            self.encode_letter(letter)

        self.string_data = " ".join([str(item) for item in self.end_data])

            
    def encode_letter(self, letter):
        encoded_letter = ord(letter)
        i = 0

        for pointer in self.pointers:
            #get data for specific point in key
            data = self.key[pointer][i]

            operator = data[0]
            number = data[1]

            if operator == "+":
                encoded_letter += number
            elif operator == "-":
                encoded_letter -= number
            elif operator == "x":
                encoded_letter *= number
            elif operator == "/":
                encoded_letter /= number

            i += 1

        self.pointers = self.increment_pointers(self.pointers)

        self.end_data.append(encoded_letter)

    def increment_pointers(self, arr):
        for i in range(len(arr)):
            if arr[i] < 9:
                arr[i] += 1
                break
            elif arr[i] == 9 and i < len(arr) - 1:
                arr[i] = 0  # Reset current item to 0
                continue  # Move to the next item in the next iteration
            
        print(arr)
        return arr

class Decode:
    def __init__(self, key, data):
        key = [list(reversed(line)) for line in key]

        self.key = key
        self.data = data
        self.key_len = len(key)
        self.current_pointer_sub = 9

        #pointers as to where currently am in key
        self.pointers = [0 for i in range(len(self.key[0]))]

        self.string_data = ""

        for letter in data.split(" "):
            self.decode_letter(float(letter))

            
    def decode_letter(self, enc_letter):
        decoded_letter = enc_letter
        i = 0

        for pointer in list(reversed(self.pointers)):
            #get data for specific point in key
            data = self.key[pointer][i]

            operator = data[0]
            number = data[1]

            if operator == "+":
                decoded_letter -= number
            elif operator == "-":
                decoded_letter += number
            elif operator == "x":
                decoded_letter /= number
            elif operator == "/":
                decoded_letter *= number

            i += 1

        self.pointers = self.increment_pointers(self.pointers)

        self.string_data += str(chr(int(decoded_letter)))

    def increment_pointers(self, arr):
        for i in range(len(arr)):
            if arr[i] < 9:
                arr[i] += 1
                break
            elif arr[i] == 9 and i < len(arr) - 1:
                arr[i] = 0  # Reset current item to 0
                continue  # Move to the next item in the next iteration
            
        print(arr)
        return arr
    
def decode_uni(data):
    return_data = ""

    for item in data.split(" "):
        return_data += chr(int(item))

    return return_data