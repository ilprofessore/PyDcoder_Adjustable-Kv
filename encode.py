# defining the main coding function.
def encode_module(input_sentence):
    # below line converts all the input text into lowercase for ease.
    input_sentence = input_sentence.lower()
    output_code = ""
    for letter in input_sentence:
        if letter == "a":
            output_code = output_code + "1"
        elif letter == "b":
            output_code = output_code + "2"
        elif letter == "c":
            output_code = output_code + "3"
        elif letter == "d":
            output_code = output_code + "4"
        elif letter == "e":
            output_code = output_code + "5"
        elif letter == "f":
            output_code = output_code + "6"
        elif letter == "g":
            output_code = output_code + "7"
        elif letter == "h":
            output_code = output_code + "8"
        elif letter == "i":
            output_code = output_code + "9"
        elif letter == "j":
            output_code = output_code + "!"
        elif letter == "k":
            output_code = output_code + "@"
        elif letter == "l":
            output_code = output_code + "#"
        elif letter == "m":
            output_code = output_code + "$"
        elif letter == "n":
            output_code = output_code + "%"
        elif letter == "o":
            output_code = output_code + "^"
        elif letter == "p":
            output_code = output_code + "&"
        elif letter == "q":
            output_code = output_code + "*"
        elif letter == "r":
            output_code = output_code + "("
        elif letter == "s":
            output_code = output_code + ")"
        elif letter == "t":
            output_code = output_code + "_"
        elif letter == "u":
            output_code = output_code + "+"
        elif letter == "v":
            output_code = output_code + "-"
        elif letter == "w":
            output_code = output_code + "="
        elif letter == "x":
            output_code = output_code + "<"
        elif letter == "y":
            output_code = output_code + ">"
        elif letter == "z":
            output_code = output_code + "?"
        elif letter == " ":
            output_code = output_code + "|"
        elif letter == ",":
            output_code = output_code + "`"
        elif letter == ".":
            output_code = output_code + "~"
    return output_code
# simple code, no rocketscience.