# input -> number of brackets
# output will be a printing of balanced outputs
# working -> we go different paths based on the idea of if we can do so. If we can open a new bracket, then we do and see where that leads to. And if we can close a pair, then we close and see where that leads to.

def get_balanced_parentheses(open_brac, close, output='',):
    if open_brac < 0 and close < 0:
        print ('invalid')
    # base case
    if open_brac == 0 and close ==0:
        print (output)
        return
    # case 1: we open_brac
    if open_brac > 0:
        get_balanced_parentheses(open_brac - 1, close,output = output + '(')
    # case 2: we can close
    if close > open_brac:
        get_balanced_parentheses(open_brac, close - 1, output = output + ')')

def main(n):
    get_balanced_parentheses(n,n)

main(3)