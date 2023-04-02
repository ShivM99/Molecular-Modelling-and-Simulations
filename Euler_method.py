#Euler's method
x = float (input ("Enter the initial value of x: "))
step = float (input ("Enter the step size: "))
y = x**3
print ("Initial value of y:", y)
for _ in range (1000):
    x += step
    y += (step*3*x*x)
print ("Final value of y at x = 2.1:", y)
