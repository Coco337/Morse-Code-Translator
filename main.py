import tkinter as tk

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

def text_to_morse(text):
    morse_text = ""

    for char in text:
        if char in morse_code_dict:
            morse_text += morse_code_dict[char]
            morse_text += " "
        else:
            morse_text += "/"

    return morse_text

def morse_to_text(morse_text):
    text = ""

    words = morse_text.split('/')
    for word in words:
        characters = word.split()
        for char in characters:
            text += get_key_from_value(char)
        text += " "

    return text
def get_key_from_value(keyvalue):
    for key, value in morse_code_dict.items():
        if value == keyvalue:
            return key

    return None

class MyGUI(tk.Tk):

    def __init__(self):
        super().__init__()

        self.geometry("800x500")
        self.title("Morse Code Translator")

        self.label = tk.Label(self, text = "Morse Code Translator", font = ('Comic Sans MS', 20))
        self.label.pack(pady = 10)

        self.textbox = tk.Text(self, height=3, font=('Comic Sans MS', 16))
        self.textbox.pack(padx= 10, pady= 10)

        self.buttonframe = tk.Frame(self)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)

        self.btn_text_to_morse = tk.Button(self.buttonframe, text= "Convert to Morse", font=('Comic Sans MS', 16), command=self.c_text_to_morse)
        self.btn_text_to_morse.grid(row= 0, column= 0, padx= 5, sticky='we')

        self.btn_morse_to_text = tk.Button(self.buttonframe, text= "Convert to Text", font=('Comic Sans MS', 16), command=self.c_morse_to_text)
        self.btn_morse_to_text.grid(row= 0, column= 1, padx= 5, sticky='we')

        self.btn_erase = tk.Button(self.buttonframe, text= "Erase", font=('Comic Sans MS', 16), command=self.erase)
        self.btn_erase.grid(row= 0, column= 2, padx= 5, sticky='we')

        self.buttonframe.pack(fill='x', pady= 10, padx= 10)
        self.output = None

        self.mainloop()

    def c_text_to_morse(self):
        if self.output:
            self.output.destroy()

        msg = self.textbox.get('1.0', tk.END).strip()

        morse_msg = text_to_morse(msg)
        self.output = tk.Label(self, text = morse_msg, font=('Comic Sans MS', 16))
        self.output.pack(pady= 10)

    def c_morse_to_text(self):
        msg = self.textbox.get('1.0', tk.END).strip()

        text_msg = morse_to_text(msg)
        self.output = tk.Label(self, text = text_msg, font=('Comic Sans MS', 16))
        self.output.pack(pady= 10)
    def erase(self):
        self.textbox.delete('1.0', tk.END)
        if self.output:
            self.output.destroy()

gui = MyGUI()