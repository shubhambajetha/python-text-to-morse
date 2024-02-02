from morse import morse_code_dict


class MorseCodeConverter:
    def __init__(self):
        self.morse_code_dict = morse_code_dict

    def text_to_morse(self, text):
        morse_code = " "
        for char in text.upper():
            if char in self.morse_code_dict:
                morse_code += self.morse_code_dict[char] + " "
            else:
                morse_code += char
        return morse_code

    def morse_to_text(self, morse_code):
        morse_code_split = morse_code.split(' ')
        text = ""
        for code in morse_code_split:
            for key, value in self.morse_code_dict.items():
                if code == value:
                    text += key
                    break
            else:
                text += " "
        return text

# Simple usage
if __name__ == "__main__":
    converter = MorseCodeConverter()

    # Encoding
    text_input = input("Enter text to convert to Morse code: ")
    morse_output = converter.text_to_morse(text_input)
    print(f"Morse code: {morse_output}")

    decode_choice = input("are you interested to decode this into text type 'y' or 'n' ")

    if decode_choice == 'y':
        text_output = converter.morse_to_text(morse_output)
        print(f"here you decode code {text_output}")
    elif decode_choice == 'n':
        print("ok good bye")
    else:
        print("invalid choice type 'yes' or 'no' only")

