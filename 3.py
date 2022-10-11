def asciiToSentence(string, length) :
    num = 0
    text = ""
    for i in range(length) :
        #string to num
        num = num * 10 + (ord(string[i]) -
                          ord('0'))
        #A-Z 65-90 a-z 92-122
        if ((num >= 65 and num <= 90) or 
            (num >= 97 and num <= 122)) :
            # Convert num to char
            ch = chr(num)
            text += ch
            # Reset num to 0
            num = 0
    return text

if __name__ == "__main__" :
    string = "671111101031149711611710897116105111110115"
    length = len(string)
    print(asciiToSentence(string, length))