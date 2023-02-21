"""Practice importing from other modules"""

#from lessons import my_functions

from lessons.my_functions import addition #imports function instead of whole file

#print (my_functions.addition(1,2))

#print(my_functions.my_variable)

if __name__ == "__main__":
    print ("Howdy!")

print(addition(1,2))
