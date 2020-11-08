# Caesar cipher
text = input("Enter one line of text: ")
shift = input("Enter a number between 1 and 25: ")
cipher = ''

while not isinstance(shift, int):
    shift = input("You need to enter a number, please try again: ")

while int(shift) > 25 or int(shift) < 1:
    shift = input("number not between 1 and 25, please try again: ")
shift = int(shift)
if int(shift) >= 1 and int(shift) <= 25:
    for char in text:
        if not char.isalpha():
            cipher = cipher + char
            continue
        if char.isupper() == True:
            code = ord(char) + shift
            if code > ord('Z'):
                code = code - ord('Z') + ord('A') - 1
            cipher = cipher + chr(code)
        if char.islower() == True:
            code = ord(char) + shift
            if code > ord('z'):
                code = code - ord('z') + ord('a') - 1
            cipher = cipher + chr(code)
print(cipher)
