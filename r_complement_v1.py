
class Number:

    def __init__(self,number,base):

        self.number = number
        self.original_base = base
        self.decimal = self.get_anyBase_to_deci(self.original_base)
        self.binary = self.get_binary()
        self.b_complement = self.get_bComplement()

    def get_binary(self):

        number = int(self.decimal)
        binary = "" 
        base = 2
        while (number > 0):
            rem = str(number % base)
            binary = rem + binary
            number = int(number / base)
        return binary 

    def get_anyBase_to_deci(self,base):

        number = self.number
        decimal = 0
        power = 0
        num_size = len(number)
        for i in range(num_size - 1, -1, -1):
            if 'A' <= number[i] <= 'Z':
                decimal += ord(number[i] - 'A') * base ** power
            else:
                decimal += int(number[i]) * base ** power 
            power += 1

        return str(decimal) 
    
    def get_bComplement(self):

        complement = ""
        for elem in self.binary:
            if elem == '0':
                complement = '1' + complement
            if elem == '1':
                complement = '0' + complement
        return complement[::-1]

def binary_adder(num1,num2):

    binary_1 = num1
    binary_2 = num2

    max_length = max(len(binary_1),len(binary_2))

    binary_1 = binary_1.rjust(max_length,'0')
    binary_2 = binary_2.rjust(max_length,'0')

    result = ['0'] * max_length
    carry = 0

    for i in range(max_length - 1, -1,-1):

        if binary_1[i] == '0' and binary_2[i] == '0' and carry == 0:
            result[i] = '0'
            carry = 0
            continue;
        if binary_1[i] == '0' and binary_2[i] == '0' and carry == 1:
            result[i] = '1'
            carry = 0
            continue;
        if binary_1[i] == '0' and binary_2[i] == '1' and carry == 0:
            result[i] = '1'
            carry = 0
            continue;
        if binary_1[i] == '0' and binary_2[i] == '1' and carry == 1:
            result[i] = '0'
            carry = 1
            continue;
        if binary_1[i] == '1' and binary_2[i] == '0' and carry == 0:
            result[i] = '1'
            carry = 0
            continue;
        if binary_1[i] == '1' and binary_2[i] == '0' and carry == 1:
            result[i] = '0'
            carry = 1
            continue;
        if binary_1[i] == '1' and binary_2[i] == '1' and carry == 0:
            result[i] = '0'
            carry = 1
            continue;
        if binary_1[i] == '1' and binary_2[i] == '1' and carry == 1:
            result[i] = '1'
            carry = 1
            continue;
        
    if (carry):
        result.insert(0,'1_')
    



    
    return "".join(result) 
            
        





base = int(input("Enter base of the input numbers: "))
num1 = Number(str(input("Enter number X:")),base)
num2 = Number(str(input("Enter number Y (to be subtracted):")),base)
print(binary_adder(num1.binary,binary_adder("1",num2.b_complement)))
