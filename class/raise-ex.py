class ShortInputException(Exception):
    '''A user-defined exception class'''
    def __init__(self, length ,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Enter something-->')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('Why did you do an EOFError on me?')
except ShortInputException as SIE:
    print('ShortInputException The input was {0} long,'
    'excepted atleast {1}'.format(SIE.length, SIE.atleast))
else:
    print('No exception was raised.')
