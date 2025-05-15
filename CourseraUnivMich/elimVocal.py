word_without_vowels = ""

user_word = str(input("Palabra: "))
user_word = user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter

print(word_without_vowels)