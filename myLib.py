# Author : Pranit Ghag
# This is a custom library made using functions imported using matplotlib
# This also has a constant TOTAL_VOTES

# Importing matplotlib library
import matplotlib.pyplot as plt

# Function defined to plot the values
def plot(l1,l2,title,xlabel,ylabel,n):
    # Function for pLotting the graph
    plt.plot(l1,l2,'ro')
    # Function for labelling the x axis
    plt.xlabel(xlabel)
    # Function for labelling the y axis
    plt.ylabel(ylabel)
    # Function for giving a title to the plot
    plt.title(title)
    # Using for loop to name each of the points plotted on the graph
    for i, txt in enumerate(n):
        plt.annotate(txt, (l1[i], l2[i]))
    # Function for showing the graph in a window
    plt.show()

# Constant. The number of people that voted
TOTAL_VOTES = 50000
