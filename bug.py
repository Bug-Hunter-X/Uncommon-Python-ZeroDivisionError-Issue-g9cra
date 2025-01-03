def function_with_uncommon_error(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error(10, 0)
print(result) # This will raise ZeroDivisionError as expected

result = function_with_uncommon_error(0, 10)
print(result) # This will print 10 as expected

result = function_with_uncommon_error(0, 0) #This will return 0 without error. 
print(result) #Unexpected behavior. We should've had ZeroDivisionError

#Another example
def some_function(x, y):
  if x > 0 and y > 0:
    return x / y
  else:
    return 0

print(some_function(10, 0)) # Output: 0. This is incorrect. Should raise ZeroDivisionError

print(some_function(0, 10)) # Output: 0

print(some_function(0, 0)) # Output: 0