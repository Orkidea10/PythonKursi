def add(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def concatenate(x,y):
    return str(x)+ str(y)

def operate(operation,x,y):
    return operation(x,y)

result_add= operate(add, 2, 4)
result_subtraction= operate(subtraction, 7, 2)
result_concatenate= operate(concatenate, "hello", " orkidea")

print(result_add)
print(result_subtraction)
print(result_concatenate)