#This is the tut  for the decordator
#https://www.youtube.com/watch?v=MYAEv3JoenI



class cat():
    
    any_number = 10

    def __init__(self,input_name):
        self.name = input_name
    
    def bark(self):
        print(f"{self.name} said Meow meow nigga!")
        self.any_number += 36

    def meow(self):
        print(f"{self.name} stand down what good my nigga")


def add(input_1,input_2,input_3):

    return(input_1 + input_2 + input_3)

def multi(input_1,input_2,input_3):

    return(input_1*input_2*input_3)

def math(func,input_1,input_2,input_3):

    print(func(input_1,input_2,input_3))


math(multi,3,4,5)


#This is basicallty a decorater function of a function.
#Also its a demonstration of first class function
#here function is used as a variable and then executed!!!

def outer_function(input_string):
    
    def inner_function():
        print(input_string.upper())
        return inner_inner_function
        
    def inner_inner_function():
        print(input_string.lower())
    
    return inner_function    #This is ready to be executed function....its the return of the outer_function

#From this function_variable is a ready to be executed inner_function
function_variable = outer_function("This is just a input string") 

function_variable()
# Here you executed the inner_function so what it does is printing the input_string
# This is equivalent to 

outer_function("This is a input string")()
# To execute the inner_inner_function then this is the way.
outer_function("This is a another input string")()()

def math_function(a,b,c):
    if(a == 0):
        string = "Can't divide by zero!!!"
        return string
    return ((b+c)/a**2) 


print(math_function(4,3,5))


#If you wanna add something to the function or edit the fucntion itself,then you can actually 
#Use the decorators

#here is the code !!!

def math_function(a,b,c):
    print(f"This is the __name__{__name__}")
    return ((b+c)/a**2)

def decorator(input_function):
    def wrapper_function(a,b,c):
        if(a==0):
            print("Cannot divide by zero!!")
            return
        return input_function(a,b,c)

    return wrapper_function

math_function = decorator(math_function)

print(math_function(3,1,2))

#This is equivalent to this syntaxx
#Here is a video for help!!
# https://www.youtube.com/watch?v=MYAEv3JoenI

@decorator
def math_function(a,b,c):
    return((b+c)/a)

