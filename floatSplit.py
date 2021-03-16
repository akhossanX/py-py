

def split_float(number):

    """
    this function takes a float as parameter and returns 
    the same float with only 2 digits after the dot sign (.),
    furthermore it replaces the dot with a colon (french notation of float numbers)
  
    """

    if type(number) is not float:
        raise TypeError("the parameter must be a float type")

    string = str(number)
    number1 = string.split(".")

    #this is a very powerful tool in python 
    splited = ",".join([number1[0], number1[1][:2]])

    return splited



def unknown_function(msg, *parameters):

    """
    this function takes an unbounded number of parameters (theoritically)
    """
    print(msg, " dynamic params {} ".format(parameters))

if __name__ == "__main__":

    print(split_float(input("enter a float number\n")))
    params = [3, 5, 6, 7, 8]
    print(*params)
