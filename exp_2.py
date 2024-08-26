# To write a function foo(list_:list) #list of integers that_ 
# that shifts all odd numbers to the left and even numbers to the right.
# The transformation of list must take place without changing the order!

#Example: [1,3,4,5,8,9,11,13,18]
#After transformation: [1,3,5,9,11,13,4,8,18]
def odd_or_even(f):
    if f % 2 == 0:
        return "even"
    else:
        return "odd"
def foo(list_:list) -> list:
    evens = [list_[x] for x in range(len(list_)) if odd_or_even(list_[x])=="even"]
    odds  = [list_[x] for x in range(len(list_)) if odd_or_even(list_[x])=="odd"]
    return odds + evens
print(foo([1,3,4,5,8,9,11,13,18]))
