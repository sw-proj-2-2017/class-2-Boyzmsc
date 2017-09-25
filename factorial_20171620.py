while True:
    number = int(input("Enter a number: "))
    def Factorial(num):
        if num == 1:
            return num
        elif num == 0:
            return num+1
        elif num < 0:
            print("Error")
            quit()
        return Factorial(num-1) * num

    print("%d! = %d" %(number,Factorial(number)))
