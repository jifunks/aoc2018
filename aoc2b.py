import difflib

with open('input.txt') as f:
    input_data = f.read().splitlines()

max_length = 0
for id_index, id in enumerate(input_data):
    max_length = len(id)
    for id2 in input_data[id_index:]:
        matched_chars = ''
        for char_index, character in enumerate(id):
            if character == id2[char_index]:
                matched_chars += character

        if len(matched_chars) == max_length - 1:
            print(id, id2)
            print(matched_chars)

