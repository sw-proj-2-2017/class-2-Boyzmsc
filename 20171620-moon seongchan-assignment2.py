try:
    num = int(input("Enter a number:"))
    while num >= 0:
        result = 1
        for k in range (1, num+1):
            result *= k
        print("%d!= %d"%(num,result))
        num = int(input("Enter a number:"))
    if num <= -1:
        print("Error")
except ValueError:
    print("Error")
