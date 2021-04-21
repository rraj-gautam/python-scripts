def return_middle():
    a = 1
    return a
    a = 2 

print(return_middle())  #return 1


######################################################

def no_expression_list():
    return    # No return expression list.
    """return pass  # No return statement """

print(no_expression_list())

######################################################

def multiple_returns(n):
    if(n):
        return "First Return Statement"
    else:
        return "Second Return Statement"

print(multiple_returns(True))  # output: First Return Statement
print(multiple_returns(False)) # output:  Second Return Statement
