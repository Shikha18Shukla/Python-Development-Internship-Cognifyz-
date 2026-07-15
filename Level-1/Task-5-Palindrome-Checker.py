print("========== PALINDROME CHECK ==========")
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print(f'"{word}" is a palindrome.')
else:
    print(f'"{word}" is not a palindrome.')