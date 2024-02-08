def Triangle(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()
print("hello")
Triangle(10)
