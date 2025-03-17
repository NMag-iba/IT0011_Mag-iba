statement = """The quick brown fox jumps over the lazy dog near the bank of the river the Quick Brown Fox Jumps Over The Lazy Dog Near The Bank Of The River The quick brown fox jumps over the lazy dog near the bank of the river the Quick Brown Fox Jumps Over The Lazy Dog Near The Top Of The River The slow Brown fox jumps over the lazy dog near the bank of the river the Fast Brown Fox Jumps Over The Lazy Cat near The Bank Of The River The quick brown fox jumps over the Good Cat near the bank of the river the Quick Brown Fox Jumps Over The Lazy Dog Near The Bank Of The Mountain"""
excluded_words = {"and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"}

words = statement.split()

word_count = {}

for word in words:
    word = word.strip(".,!?")  
    if word.lower() not in excluded_words:  
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

lowercase_words = []
uppercase_words = []

for word, count in word_count.items():
    if word.islower():
        lowercase_words.append((word, count))
    else:
        uppercase_words.append((word, count))

n = len(lowercase_words)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if lowercase_words[j][0] > lowercase_words[j + 1][0]:  
            temp = lowercase_words[j]
            lowercase_words[j] = lowercase_words[j + 1]
            lowercase_words[j + 1] = temp

n = len(uppercase_words)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if uppercase_words[j][0] > uppercase_words[j + 1][0]:  
            temp = uppercase_words[j]
            uppercase_words[j] = uppercase_words[j + 1]
            uppercase_words[j + 1] = temp

for word, count in lowercase_words:
    print(f"{word.ljust(10)} - {count}")

for word, count in uppercase_words:
    print(f"{word.ljust(10)} - {count}")

print(f"\nTotal words filtered: {sum(word_count.values())}")