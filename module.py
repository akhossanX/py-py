
import os

def stack_overflow(root, power):
    """
    this function is meant to calculate the power of an integer
    """
    root = root ** power 
    return root


if __name__ == "__main__":

    root = input("please enter your root number ")
    power = input("enter the power")
    result = stack_overflow(root, power)
    print(result)

