def count_characters(input_string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel_count = consonant_count = space_count = other_count = 0
    
    for char in input_string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        elif char == " ":
            space_count += 1
        else:
            other_count += 1
    
    print(f"Vowels: {vowel_count}, Consonants: {consonant_count}, Spaces: {space_count}, Others: {other_count}")

input_string = input("Enter a string: ")
count_characters(input_string)



def sum_of_digits(input_string):
    total = 0
    for char in input_string:
        if char.isdigit():
            total += int(char)
    print(f"Sum of digits: {total}")

input_string = input("Enter a string containing digits: ")
sum_of_digits(input_string)


def pattern_a(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "".join(str(j) for j in range(1, i + 1)))

n = 5
pattern_a(n)



def pattern_b(n):
    i = 1
    while i <= n:
        if i % 2 != 0:
            print(" " * (n - i) + str(i) * i)
        i += 1

n = 7
pattern_b(n)
