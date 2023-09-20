def digital_root(n):
    if n < 10:
        return n
    
    digit_sum = sum(int(digit) for digit in str(n))
    
    return digital_root(digit_sum)


num = 493193
result = digital_root(num)
print("Digital root:", result)






