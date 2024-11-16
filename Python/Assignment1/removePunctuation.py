import string

def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

input_string = "Hello, world! This is a test. #Python!"
cleaned_string = remove_punctuation(input_string)
print("String without punctuation:", cleaned_string)
