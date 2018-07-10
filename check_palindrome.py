from string import punctuation

def reverse(text):
    # if not isinstance(text, str):
    #     raise Exception('type of text is not str')
    return text[::-1]

def is_palindrome(text):

    text = text.lower()
    text = text.replace(' ', '')
    for char in punctuation:
        text = text.replace(char, '')
    return text == reverse(text)

def main():
    something = input('Please input your what do you want to say:')

    if is_palindrome(something):
        print('Yes, "{0}" is a palindrome '.format(something))
    else:
        print('Yes, "{0}" is not a palindrome '.format(something))
        main()

if __name__ == '__main__':
    main()
else:
    print('this module was imported by another module!')
