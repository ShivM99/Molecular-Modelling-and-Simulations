x = float (input ("Enter the initial value of x: "))
y = x**3
x_final = float (input ("Enter the final value of x: "))
step = float (input ("Enter the step size: "))
i = int ((x_final-x)/step)
for _ in range (0,i):
    y_new = y + step*(3*x*x)
    x += step
    y = y_new
print (f"Value of y at x={x_final}: {y}")
