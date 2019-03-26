# Babita 25-Mar-19
# Program to display plots of functions x, x square and 2 raise to x in range[0.4]

import matplotlib.pyplot as plt

def plot_x():
    # Function to plot a graph of y= x OR f(x) = x
    # This is a linear straight line graph as y=x
    # Graph has to be plotted for the range (0,4)

    # Declare an array with x and y values for the function y = x
    plot_arr = [0,1,2,3,4]
    
    plt.plot(plot_arr, plot_arr)
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.title("Graph of f(x) = x")
    plt.axis([0,4,0,4])
    plt.show()


def plot_x_square():
    # Function to plot a graph of y= x square OR f(x) = x * x
    # Graph has to be plotted for the range (0,4)

    # Declare an array with x and y values for the function y = x *x
    input_arr = [0,0,0,0,0]
    output_arr = [0,0,0,0,0]
    for i in range (0,5):
        input_arr[i]= i
        output_arr[i]=i*i
        
    plt.plot(input_arr, output_arr)
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.title("Graph of f(x) = x * x")
    plt.axis([0,4,0,16])
    plt.show()


# Main Program
plot_x()
plot_x_square()
#plot_2_raise_to_x()


