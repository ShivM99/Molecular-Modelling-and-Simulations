#Minima finding by golden section method
x = True
while x:
    try:
        n1 = float(input("Enter the 1st possible value of x: "))
        n2 = float(input("Enter the 2nd possible value of x: "))
    except ValueError:
        print ("Invalid type of input")
        continue
    a = min(n1,n2)
    b = max(n1,n2)
    f_a = (a*a) - (4*a) - 10
    f_b = (b*b) - (4*b) - 10
    count = 0
    while x:
        count += 1
        print ("Iteration:",count)
        x1 = b - 0.618*(b-a)
        x2 = a + 0.618*(b-a)
        print (f"a = {a}\tb = {b}\tx1 = {x1}\tx2 = {x2}")
        f_x1 = (x1*x1) - (4*x1) - 10
        f_x2 = (x2*x2) - (4*x2) - 10
        print (f"f(a) = {f_a}\tf(b) = f_b\tf(x1) = {f_x1}\tf(x2) = {f_x2}")
        if round(f_x1,5) != round(f_x2,5):
            if f_x1 < f_a and f_x1 < f_b:
                if f_x1 < f_x2:
                    b = x2
                    f_b = f_x2
                else:
                    a = x1
                    f_a = f_x1
            else:
                print ("Values of n1 and n2 do not bracket the minima")
                break
        else:
            print (f"{'-'*50}")
            print (x1,"is the minima of the equation: x^2-4x-10")
            print ("Number of iterations done:",count)
            x = False
