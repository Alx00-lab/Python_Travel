palabras = ["gato", "perro", "gato", "pez", "perro", "perro"]

# create an empty dictionary
# to store the count of each word

repeated_words = {} 
for word in palabras:
    repeated_words[word] = repeated_words.get(word, 0) + 1

# print the dictionary repeated words

for word, count in repeated_words.items():
    if count > 1:
        print(f"{word} se repite {count} veces")
    else:
        print(f"{word} no se repite")


