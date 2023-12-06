with open('dec-6-input-1.txt', 'r') as f:
    total = 0
    for line in f:
        concatenatedString = ''
        finalString = ''
        for char in line:
            if char.isdigit():
                concatenatedString += char
        finalString += concatenatedString[0]
        finalString += concatenatedString[-1]
        curNum = int(finalString)
        total += curNum
        print("Total is:",total, "And the Number is:",curNum)
    print(total)
