words = open("words.txt", encoding="utf-8").read().split()
seen = set()
unique = []
for word in words:
    if word not in seen:
        seen.add(word)
        unique.append(word)
print("count=", len(unique))
