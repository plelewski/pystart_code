text = 'kubek'

parameter = 2
encr_text = []

for char in text:
    if char.isalpha():
        encr_text.append(ord(char) + parameter)

for encr_char in encr_text:
    print(chr(encr_char), ' ', chr(encr_char - parameter))
