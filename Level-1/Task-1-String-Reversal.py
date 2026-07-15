print("========== BASIC STRING REVERSAL ==========")

def reverse_text(word):
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    return reversed_word

sample = "hello"
print(reverse_text(sample))