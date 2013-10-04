# Multiply all the elements in a list
def multiply(l):
    if l == []:
        return 1
    return l[0] * multiply(l[1:])

def factorial (n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Count the number of elements in the list l
def count_list(l):
    if l ==[]:
        return 0
    return 1 + count_list(l[1:])

# Sum all of the elements in a list
def sum_list(l):
    if l == []:
        return 0
    return l[0] + sum_list(l[1:])


#Reverse a list without slicing or loops
def reverse(l):
    if l == []:
        return []
    num = l.pop(0)
    return reverse(l) + [num]


# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)




# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    if len(l) == 0:
        return None
    if l[0] == i:
        return True
    else:
        return find(l[1:], i)


# Determines if a string is a palindrome
def palindrome(some_string):
    first_letter = some_string[0]
    last_letter = some_string[-1]
    if len(some_string) <= 1:
        return True
    if first_letter == last_letter:
        return palindrome(some_string[1:-1])
    return False
     


# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    if folds == 0:
        return (width, height)
    height = height / 2
    return fold_paper(height, width, folds-1)


# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    count = range(n, target + 1)
    num = count.pop(0)
    print num
    if count == []:
        return []
    return count_up(target, count[0])
    
















