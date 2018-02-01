class MyClass():
    """Base class"""

    #Init is constructor - self is implicit argument passed to all methods
    def __init__(self):
        #setting a constructor with the self property
        self.property = 1 
        return
    
    #another method
    def func(self, parameter_list):
        #does nothing
        pass
    
    #'abstract' method, throws an error if it's ran
    def funcname(self, parameter_list):
        raise NotImplementedError

    
#Inheritance, multiple inheritance (all classes implicitly inherit object, not needed strictly)
class MyClass2(MyClass, Object):
    """Extension of base class"""
    
    #overriding just by re-implementing the method
    def func(self, parameter_list):
        return parameter_list

    def func2(self):
        print('hello')    


#This block is the entry point to the program, if it's being ran as a standalone program and not being called from some external package
if __name__ == '__main__':
    #class instansiation
    obj = MyClass2()
    #accessing properties
    print(obj.property)
    #calling methods
    print(obj.func("This is now implemented"))



    