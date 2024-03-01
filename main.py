morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}

def text_to_morse():
    text = input("Text: ")
    morse_text = ""

    for char in text:
        if char in morse_code_dict:
            morse_text += morse_code_dict[char]
            morse_text += " "
        else:
            morse_text += "/"

    print(morse_text)

def morse_to_text():
    morse_text = input("Morse: ")
    text = ""

    words = morse_text.split('/')
    for word in words:
        characters = word.split()
        for char in characters:
            text += get_key_from_value(char)
        text += " "

    print(text)
def get_key_from_value(keyvalue):
    for key, value in morse_code_dict.items():
        if value == keyvalue:
            return key

    return None

while True:
    option = input("What do you want to write: ")

    if option == "text":
        text_to_morse()
    elif option == "morse":
        morse_to_text()
    elif option == "exit":
        break
    else:
        print("try again")
