#!/usr/bin/env python3

# Date = 11 Sept 2018
# Version = i
# OriginalAuthor = Oliver Bonham-Carter

# Description: A basic calculator: This program asks the users to enter two numbers.
# Then the user will enter a mathematical operator to be applied to the numbers for
# the calculation.

def getResponse(prmpt, task ="string"):
# Handles the user input aspect for the program
# prmpt: the string of the question to ask the user
# task: if the parameter for this is "float" then return a float, otherwise
# return a string

    response_str = input(prmpt)
    if task == "float":
        return int(response_str)
    else:
        return response_str
#end of getResponse()


print("Please add the doCalc() (accepting three parameters) function to perform the mathematics of the program")



def main(): # driver function
    print("  -------------------------------------------------")
    print("  |   This is a program to compute the addition,  |")
    print("  | subtraction, multiplication, division and     |")
    print("  | modulus of two user-entered numbers.          |")
    print("  -------------------------------------------------")
    prmpt = "  Enter the first number in your equation : "
    num1_flt = getResponse(prmpt,"float") # specify a float to return
    print("    *Your response is :",num1_flt)

    prmpt = "  Enter the second number in your equation : "
    num2_flt = getResponse(prmpt,"float") # specify a float to return
    print("    *Your response is :",num2_flt)

    prmpt = "  Select an operator (+, -, *, / or %) : "
    op_str = getResponse(prmpt) # since no second option is added, we return a string.
    print("    *Your response is :",op_str)

    print("   The result of <<",num1_flt, op_str,num2_flt,">> is :",doCalc(num1_flt, num2_flt, op_str)) # call function to perform the calculation
    print("")
#end of main()



main() # begin the program
