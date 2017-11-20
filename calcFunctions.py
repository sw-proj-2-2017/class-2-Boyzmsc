
def call(n,num):
    if n == 1:
        return factorial(num)
    elif n == 2:
        return decToBin(num)
    elif n == 3:
        return binToDec(num)
    elif n == 4:
        return decToRoman(num)
    elif n == 5:
        return romanToDec(num)

def factorial(numStr):
    try:
        n = int(numStr)
        if n == 0:
            return 1
        elif n == 1:
            return n
        elif n < 0:
            return "ValueError"
        else:
            return factorial(n - 1) * n
    except:
        return 'Error!'

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    result = ''
    n = int(numStr)
    try:
        if (0 < n and n < 4000):
            for value,letter in romans:
                while n >= value:
                    result += letter
                    n -= value
        else:
            return 'Error!'
        return result

    except:
        return 'Error!'

def romanToDec(Str):
    try:
        result = 0
        romanStr = str(Str)
        if romanStr == "":
            return 'Error!'
        
        for value, letter in romans:
            if (len(letter) == 1) and (len(romanStr) != 0):
                while romanStr[0] == letter:
                    result += value
                    romanStr = romanStr[1:]
                    if len(romanStr) == 0:
                        break
            elif (len(letter) == 2) and (len(romanStr) != 0):
                while romanStr[:2] == letter:
                    result += value
                    romanStr = romanStr[2:]
                    if len(romanStr) == 0:
                        break
        return result

    except:
        return 'Error!'





