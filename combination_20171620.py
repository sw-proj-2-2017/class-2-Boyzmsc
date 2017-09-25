while True:
    m = int(input("m = "))
    n = int(input("n = "))
    def Combination(m,n):
        if m >= 0 and n >= 0 and m >= n:
            if n == 0 or m == n:
                return 1
            else:
                return Combination(m - 1, n - 1) + Combination(m - 1, n)
        else:
            print("Error")
            quit()

    print("C(%d,%d) = %d" %(m,n,Combination(m,n)))
