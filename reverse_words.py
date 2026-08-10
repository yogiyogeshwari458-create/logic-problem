sentence = input("Enter a sentence: ")

words = sentence.split()

result = []

for word in words:
    result.append(word[::-1])

print("Reversed sentence:", " ".join(result))