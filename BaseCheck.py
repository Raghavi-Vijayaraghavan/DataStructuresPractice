def baseCheck(base, number):
    if number == 1:
        return True

    else:
        if number % base == 0:
            return baseCheck(base, number//base)
            
        else:
            return False
        
        
print(baseCheck(2, 254))   
