# Babita 25-Mar-19
# Program to display plots of functions x, x square and 2 raise to x in range[0.4]

import math
import matplotlib.pyplot as plt

# Main Program
#plot_x()
#plot_x_square()
#plot_2_raise_to_x()

# code to plot all the 3 functions together

data = [0,1,2,3,4] # Data set for f(x) = x, here both and y(f(x)) will have the same values, linear straight line graph
data_sq = [0,0,0,0,0] # Array to store the output of the function f(x) = x*x 
data_2_raise_x  = [0,0,0,0,0] # Array to store the output of the function f(x) =  2 raise to x 

# Populate the output values for the functions (x square and 2 raise to x)
for i in range(0,5):
    data_sq[i] = data[i] * data[i] # Populate the data_sq array with the square of each input data element
    data_2_raise_x[i] = math.pow(2, data[i]) # Populate the data_1_raise_x array with 2 raise to i for each of input i values [0 to 4]


# Plot the graph to display all the 3 graphs together
# First 2 arguments are the data set corresonding to function f(x) = x, 
# Here input and output both are from same list (data), this graph is shown in blue dashed line

# Argument 4 and 5 are the data set corresonding to function f(x) = x * x, 
# Here input and output are represented using array 'data'and 'data_sq', this graph is shown in red dash dot line

# Argument 7 and 8 are the data set corresonding to function f(x) = 2 raise to x, 
# Here input and output are represented using array 'data'and 'data_2_raise_x', this graph is shown in green solid line 

plt.plot(data, data, 'b--', data, data_sq, 'r-.', data, data_2_raise_x, 'g')
plt.ylabel('f(x)') # Y axis Label 
plt.xlabel('x') # X axis Label
plt.title("Graph of functions -> x, x*x, 2**x" ) # Title of Graph
plt.axis([0,4,0,16]) # (0,4) - X axis scale, (0,16) - Y axis scale
plt.annotate('f(x)=x', xy=(3,3), xytext=(3.5, 6), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('f(x)=x*x', xy=(3,9), xytext=(2.5, 11), arrowprops=dict(facecolor='black', shrink=0.05),)
plt.annotate('f(x)=2**x', xy=(1,2), xytext=(0.35, 4), arrowprops=dict(facecolor='black', shrink=0.05),)
plt.show()


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

#def plot_2_raise_to_x():
