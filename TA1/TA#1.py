text = input("Enter string: ")
vowels = 0
consonants = 0
spaces = 0
others = 0

alph_vowel = "AEIOUaeiou"
for char in text:
    if char in alph_vowel:  
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isspace():  
        spaces += 1
    else:  
        others += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)
print("Other Characters:", others)