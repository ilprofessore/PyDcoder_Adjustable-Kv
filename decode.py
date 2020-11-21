# creating the main decoding module.
def decode_module(input_sentence):
    # below line converts all the input to lowercase for ease.
    output_code = ""
    for letter in input_sentence:
        if letter == "1":
            output_code = output_code + "a"
        elif letter == "2":
            output_code = output_code + "b"
        elif letter == "3":
            output_code = output_code + "c"
        elif letter == "4":
            output_code = output_code + "d"
        elif letter == "5":
            output_code = output_code + "e"
        elif letter == "6":
            output_code = output_code + "f"
        elif letter == "7":
            output_code = output_code + "g"
        elif letter == "8":
            output_code = output_code + "h"
        elif letter == "9":
            output_code = output_code + "i"
        elif letter == "!":
            output_code = output_code + "j"
        elif letter == "@":
            output_code = output_code + "k"
        elif letter == "#":
            output_code = output_code + "l"
        elif letter == "$":
            output_code = output_code + "m"
        elif letter == "%":
            output_code = output_code + "n"
        elif letter == "^":
            output_code = output_code + "o"
        elif letter == "&":
            output_code = output_code + "p"
        elif letter == "*":
            output_code = output_code + "q"
        elif letter == "(":
            output_code = output_code + "r"
        elif letter == ")":
            output_code = output_code + "s"
        elif letter == "_":
            output_code = output_code + "t"
        elif letter == "+":
            output_code = output_code + "u"
        elif letter == "-":
            output_code = output_code + "v"
        elif letter == "=":
            output_code = output_code + "w"
        elif letter == "<":
            output_code = output_code + "x"
        elif letter == ">":
            output_code = output_code + "y"
        elif letter == "?":
            output_code = output_code + "z"
        elif letter == "|":
            output_code = output_code + " "
        elif letter == "`":
            output_code = output_code + ","
        elif letter == "~":
            output_code = output_code + "."
    return output_code
# code is simple, no one can get confused here.