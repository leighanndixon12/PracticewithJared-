def digital_root(num):
    return_num = 0
    str_num = str(num)
    number_places = []

    while len(str_num) > 1:
        temp = 0
        number_places = [int(num) for num in str_num]
        str_num = str(sum(number_places))

    return_num = int(str_num)
    
    return return_num
        # repeat until length of string is 1
    # turn string to int then return 

test_num = 2902
print('the digital root of {test} is {digital_root}'.format(test = test_num, digital_root = digital_root(test_num)))