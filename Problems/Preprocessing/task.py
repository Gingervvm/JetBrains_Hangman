input_string = input()
to_replace = [",", ".", "!", "?"]
input_replace = input_string
for sign in to_replace:
    input_replace = input_replace.replace(sign, "")
print(input_replace.lower())