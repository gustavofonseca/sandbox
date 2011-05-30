"""
    >>> Dispatcher.handle_for_me('the animal who says "auau"')
    handled by a Dog instance!
    
    >>> Dispatcher.handle_for_me('the animal who says "miau"')
    handled by a Cat instance!
    
    >>> Dispatcher.handle_for_me('the animal who says "hakuna matata"')
    Dog does not have a sucessor =/
"""

class Animal(object):
    def __init__(self):
        self.sucessor = None
        
class Cat(Animal):
    def process_request(self, request):
        if 'miau' in request:
            print 'handled by a Cat instance!'
        elif self.sucessor is not None: 
            self.sucessor.process_request(request)
        else:
            print 'Cat does not have a sucessor =/'
            
class Dog(Animal):
    def process_request(self, request):
        if 'auau' in request:
            print 'handled by a Dog instance!'
        elif self.sucessor is not None: 
            self.sucessor.process_request(request)
        else:
            print 'Dog does not have a sucessor =/'

class Dispatcher(object):
    cat = Cat()
    dog = Dog()    
    cat.sucessor = dog
    
    @classmethod
    def handle_for_me(cls, request):
        cls.cat.process_request(request)

if __name__ == '__main__':
    import doctest
    doctest.testmod()