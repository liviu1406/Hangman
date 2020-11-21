vowels = list('aeiou')
consonants = ['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              'z', 'x', 'c', 'v', 'b', 'n', 'm']
# print(vowels)
user = list(input())
# print(user)
for i in user:
    if i in vowels:
        print("vowel")
    elif i in consonants:
        print("consonant")
    else:
        ''.isalpha()
        break




