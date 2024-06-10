
codedStrings = []
def sliceCodedString(testStr):
    if testStr.find('*') != -1:
        exit

    else:
        numIndices = []
        for ch in testStr:
            if ch.isdigit():
                numIndices.append(testStr.index(ch))
                if len(numIndices) == 3 or testStr.index(ch) == len(testStr)-1:
                    break
        if len(numIndices) in [3,2]:
            codeStr = testStr[numIndices[0]:numIndices[1]]
            remStr = testStr[numIndices[1]:]
            codedStrings.append(codeStr)
            if len(numIndices) == 2:
                codedStrings.append(remStr)
                remStr = '*'+testStr
        
        if len(numIndices) == 1:
            codedStrings.append(testStr)
            remStr = '*'+testStr
        sliceCodedString(remStr)
        
def decodeString():
    outputStr = ''
    for string in codedStrings:
        outputStr = outputStr + int(string[0]) * string[1:]
    return outputStr
       
sliceCodedString('1ab2abc3cd4d5e6f')
print(decodeString())





            
            
                
        
