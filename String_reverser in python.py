def string_reverser(word):
    baam: str = ''
    for i in range(len(word) - 1, -1, -1):
        baam += word[i]

    return baam


word = input('Please enter a string to be reversed: \n')
print(string_reverser(word))