# -*- coding: utf-8 -*-

# Binary Dispersion Plot
#
# Author: Keyboardroaster <keyboardroaster@gmail.com>
# gitificial@github.com
# 

"""
A utility for displaying binary dispersion.
"""

def dispersion_plot(plottitle, xlabel, **kwargs):    
        
    """
    Generate a binary dispersion plot.
    
    Be aware that kwargs is a dictionary. Dictionaries in python are unordered.
    So kwargs ignores the key-value input data order. Therefore a dictionary 
    sort was introduced, e.g. following key-value order...
    
    dispersion_plot("Dispersion", "xlabel", data3 = [0,1,0], data1= [1,1,0], data2= [1,1,0])

    ...plots the data by ascending order of the key (data1, data2, data3).
    
    :param title: Diagram title
    :type title: str
    :param xlabel: x-axis label
    :type xlabel: str
    
    :param \**kwargs:
    See below

    :Keyword Arguments:
        **key1 (str): list
        **key2 (str): list
        ...
    """

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        raise ValueError('matplotlib is missing')

    labels = ['']
    labelticks = [0,1]
    x = []    
    longest_list_size = 0
    pos = 0
    
    if(len(kwargs.items()) != 0):
        
        for key, values in sorted(kwargs.iteritems()):
            #print(key, values)
        
            # get last y-axis tick from labelticks and append last labeltick+0.5 for current key 
            labelticks.append(labelticks[-1] + 0.5)
            
            # get size of the longest data list
            if(longest_list_size < len(values)):
                longest_list_size = len(values)
            else:
                pass # do nothing
                
        # create values for x-axis
        for i in range (0,longest_list_size):
            x.append(i)        
        
        
        for key, values in sorted(kwargs.iteritems()):
            labels.append(key)
            
            # expand shorter data lists with 0 to the size of the largest list
            if(len(values) < longest_list_size):
                for i in range(0, longest_list_size - len(values)):
                    values.append(0)
                    
            #plt.plot(x, add_gain(invert_list(values), pos), "b|")
            plt.plot(x, add_gain(values, pos), "b|")

            #print(key)
            #print(pos)
            pos += 0.5
    else:
        pass # do nothing
    
    # turn offset off
    plt.ticklabel_format(useOffset=False)  

    plt.yticks(labelticks, labels)

    # x1,x2,y1,y2 => x,y-axes ranges
    plt.axis((-0.5,(longest_list_size + 1), 0.5, (len(kwargs.items()) ))) 

    plt.title(plottitle)
    plt.xlabel(xlabel)
    plt.show()
    
def add_gain(list, gain):
    """
    Amplifies each element containing a 1 with gain.
    
    :param list: list where each element is either a 0 or a 1
    :type list: list
    :param gain: 
    :type gain: int
    """  
    
    list_with_gain = []
    for value in list:
        list_with_gain.append(value * (gain + 1))
        #print(value * (gain + 1))
    return list_with_gain

def invert_list(list):
    """
    Toggles a lists elements from 0 to 1 and vice versa.
    
    :param list: list where each element is either a 0 or a 1
    :type list: list
    """    
    
    inverted_list = []
    for value in list:
        if(value == 0):
            value = 1
            inverted_list.append(value)
        elif(value == 1):
            value = 0
            inverted_list.append(value)
        else:
            print("value not valid")
    return inverted_list
    

if __name__ == '__main__':
    
    # Example:
    dispersion_plot("Dispersion Title", "Position", data3 = [0,1,0,0,1,0,1,0,1,1], data1= [1,1,0,1,1,0,0,1,0,1], data2= [0,1,1,1,1,0,1,1,0,1]) 
