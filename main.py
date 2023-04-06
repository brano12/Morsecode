MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
is_letter= False

print("Hello\nWrite anything and I will convert it into Morse Code:")
writ_string= input("Your message: ").upper()
morse_code=[]

for letter in writ_string:

    for key in MORSE_CODE_DICT:
        if key == letter:
            new_letter = MORSE_CODE_DICT[key] + " "
            morse_code.append(new_letter)
            is_letter = True
        else:
            pass
    if not is_letter:
        morse_code.append("  ")

    is_letter= False

output = ""
print(output.join(morse_code))














