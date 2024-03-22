def removeVovle(word):
    shortenWord = []

    for char in word:
        if char not in ['a','e','i','o','u','A','E','I','O','U']:
            shortenWord.append(char)
    return ''.join(shortenWord)

user = input('name: ')
print(removeVovle(user))