#!/usr/bin/python3
for letter_ascii in range(97, 123):
    if chr(letter_ascii) != 'q' and chr(letter_ascii) != 'e':
        print("{}".format(chr(letter_ascii)), end="")
