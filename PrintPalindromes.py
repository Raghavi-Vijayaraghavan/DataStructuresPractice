def divideString(testStr):
    if len(testStr) == 1:
        return testStr
    else:
        for i in range(0,len(testStr),1):
            print(testStr, i)
            return divideString(testStr[i:len(testStr)//2])
        

    

print(divideString("ABCDEFG"))
