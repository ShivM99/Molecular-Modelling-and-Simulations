#Root finding by secant method
x = True
while x:
    try:
        x1 = float(input("Enter the 1st possible value of x: "))
        x2 = float(input("Enter the 2nd possible value of x: "))
    except ValueError:
        print ("Invalid type of input")
        continue
    f_x1 = (x1*x1) - (4*x1) - 10
    f_x2 = (x2*x2) - (4*x2) - 10
    if f_x1 == 0:
        print (x1,"is the root of the equation: x^2-4x-10")
        print ("Number of iterations done: 0")
    if f_x2 == 0:
        print (x2,"is the root of the equation: x^2-4x-10")
        print ("Number of iterations done: 0")
        break
    else:
        count = 0
        while x:
            count += 1
            print ("Iteration:",count)
            x3 = x2 - (f_x2*(x2-x1))/(f_x2-f_x1)
            print (f"x1 = {x1}\tx2 = {x2}\tx3 = {x3}")
            f_x3 = (x3*x3) - (4*x3) - 10
            print (f"f(x1) = {f_x1}\tf(x2) = {f_x2}\tf(x3) = {f_x3}")
            if f_x3 >= 0.00001 or f_x3 <= -0.00001: #This is the error tolerance for secant method
                x1 = x2
                f_x1 = f_x2
                x2 = x3
                f_x2 = f_x3
            else:
                print (f"{'-'*50}")
                print (x3,"is the root of the equation: x^2-4x-10")
                print ("Number of iterations done:",count)
                x = False
