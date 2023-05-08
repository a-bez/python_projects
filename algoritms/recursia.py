# the Fuctorial

from itertools import count


def fuct(x):
    if x == 1:
        return 1
    return fuct(x-1)*x

print('The fuctorial if ', fuct(4))



# thr Fibonachi

def fib(c):
    if c == 1:
        return 0
    elif c == 2:
        return 1
    return fib(c-1)+fib(c-2)

print('The fibonachi if ',fib(5))

print('----------------')



# the palindrome

def polindrome(str):
    if len(str) <= 1:
        return 'polindrome'
    if str[0] != str[-1]:
        return 'not polindrome'
    return polindrome(str[0:-1])

print('this string is', polindrome('fd'))


print('----------------')




# the sum calculation

def SumCalc(lst):
    if len(lst) == 0:
        return 0
    else:
        sum = SumCalc(lst[1:])
        sum += lst[0]
        return sum

print('the sum of numbers of the list is equal', SumCalc([1, 2, 3]))

print('----------------')




# the sum calculation of negativ numbers

def SumCalcnegativvalues(lst):
    if len(lst) == 0:
        return 0
    else:
        count = SumCalcnegativvalues(lst[1:])
        if lst[0] < 0:
            count += 1
        return count

print('the count of negative numbers in this list is equal', SumCalcnegativvalues([1, -2, -3]))