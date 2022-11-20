#Root finding by Newton-Raphson method
x = True
while x:
    try:
        x1 = float(input("Enter the 1st possible value of x: "))
    except ValueError:
        print ("Invalid type of input")
        continue
    f_x1 = (x1*x1) - (4*x1) - 10
    ff_x1 = (2*x1) - 4
    if f_x1 == 0:
        print (x1,"is the root of the equation: x^2-4x-10")
        print ("Number of iterations done: 0")
        break
    else:
        count = 0
        while x:
            count += 1
            print ("Iteration:",count)
            x2 = x1 - (f_x1/ff_x1)
            print (f"x1 = {x1}\tx2 = {x2}")
            f_x2 = (x2*x2) - (4*x2) - 10
            print (f"f(x1) = {f_x1}\tf(x2) = {f_x2}")
            ff_x2 = (2*x2) - 4
            print (f"f'(x1) = {ff_x1}\tf'(x2) = {ff_x2}'")
            if f_x2 >= 0.00001 or f_x2 <= -0.00001: #This is the error tolerance for Newton-Raphson method
                x1 = x2
                f_x1 = f_x2
                ff_x1 = ff_x2
            else:
               print (f"{'-'*50}")
               print (x2,"is the root of the equation: x^2-4x-10")
               print ("Number of iterations done:",count)
               x = False 
