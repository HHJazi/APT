Key_table = "162020192181060017052098055154121148213048126085012142240176"
def string_split(inputstr):
    array = []
    n = 3
    for i in range(0, len(inputstr), n):
        array.append(inputstr[i:i+n])
    return array

def string_decryptor(inputstr):
    input_splitted = []
    Keytable_splitted = []
    outputstr = ""
    inputstr_splitted = string_split(inputstr)
    Keytable_splitted = string_split(Key_table)
    Input_array= [None] * len(inputstr_splitted)
    i = 0
    while i < len(inputstr_splitted):
        Input_array[i] = str((int(inputstr_splitted[i]) + 256 - int(Keytable_splitted[i % (len(Keytable_splitted))])) % 256)
        outputstr = outputstr + chr(int(Input_array[i]))
        i += 1
    return outputstr

Inputstr = input("Enter string to be decoded: ")

print(string_split(Inputstr))
print(string_decryptor(Inputstr))

