def divideString(testStr, number):
    
    if len(testStr) < number:
        return testStr
    else:
        split_part = testStr[:number]
        remaining_part = testStr[number:]
        return split_part + "|" + divideString(remaining_part, number)
    
print(divideString('MADAMMADAM', 4))



    
    
    
