# Newton Raphson method algorithm according to the working of the method taught
# in class

def f(x):
    # Here, we write the equation we're using for the algorithm (q4 in the 
    # numericals solved)
    return x**3 - 3*x - 5

def f_derivative(x):
    # derivative of the given function
    return 3*x*x - 3

def newton(x):
    # Implementation of the formula in Newton Raphson method 
    xnext = x - f(x)/f_derivative(x)

    # Assigning the accuracy measure
    accuracy = xnext - x

    # Now, the method's working takes place via iterations
    while (abs(accuracy) >= 0.0001):
        xnext = x - f(x)/f_derivative(x)

        # Accuracy calculated during the execution of the loop
        accuracy = xnext - x
        x = xnext
        print("Next iteration is: ", "%0.4f"%x)
    
    # The required output
    print("The required root is: ", "%0.4f"%x)

# Obtaining values from the user for first and second approximations
a = input("Enter the first approximation (a) : ")
b = input("Enter the second approximation (b) : ")
a = float(a)
b = float(b)

# Finding values of the functions using the given approximations
fa = f(a)
fb = f(b)

# If the given approximations evaluate to 0, they are obviously, the root of the given
# equation
if f(a) == 0:
    print("Given a = ", a," is the root of the equation")

elif f(b) == 0:
    print("Given b = ", b, " is the root of the equation")

# Testing the case for whence the function cannot work
elif f(a)*f(b) > 0:
    print("Root does not lie within the given interval [a, b]")

else:
    print("Root exists within [a, b]")

    # Checking the absolute values of the functions and proceeding to the Newton Raphson
    # algorithm
    if abs(fa) < abs(fb):
        x = a
    else:
        x = b
    newton(x)

