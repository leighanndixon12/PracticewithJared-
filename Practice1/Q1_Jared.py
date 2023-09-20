def vowel_count(sentence):
    word = sentence.lower()
    vowels = ['a','e','i','o','u']
    count = 0
    for char in word:
        if char in vowels:count += 1
    return count

test_string = 'hello can you here me'
print('there are {num} vowels in test string'.format(num = vowel_count(test_string)))