
def count_vowels(input_string):
    vowels = "aeiou"
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1

    return count


input_str = "hello world"
result = count_vowels(input_str)

print("Number of vowels:", result)
