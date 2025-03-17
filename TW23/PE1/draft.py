excludeWord = {"and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"}

def process_text(text):

    clear = "".join(char if char.isalnum() or char.isspace() else " " for char in text)

    words = clear.split()

    counts = {}
    total = 0

    for word in words:
        lower_word = word.lower()
        if lower_word not in excludeWord:
            counts[word] = counts.get(word, 0) + 1
            total += 1

    lowercase = [word for word in counts if word.islower()]
    uppercase = [word for word in counts if not word.islower()]

    lowercase.sort()
    uppercase.sort()

    print(" ")
    for word in lowercase + uppercase:
        print(f"{word:<10} - {counts[word]}")

    print(f"Total words filtered: {total}")


text = input("Enter a string statement:\n")
process_text(text)