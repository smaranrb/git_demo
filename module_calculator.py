'''
This is a simple program that calculates values based on 4 operations.
'''

class ModuleCalculator:
    '''
    Test
    '''
    def add(self, value_x, value_y):
        '''
        Add
        '''
        return value_x + value_y
    def subtract(self, value_x, value_y):
        '''
        Subtract
        '''
        return value_x - value_y
    def multiply(self, value_x, value_y):
        '''
        Multiply
        '''
        return value_x * value_y
    def divide(self, value_x, value_y):
        '''
        Divide
        '''
        if value_y == 0:
            raise ValueError("Division by zero is not allowed")
        return value_x / value_y
