
# WAP to check if the given contact number is valid or invalid using regular expressions.


import re

# Method 1:

phno = input('enter a contact number: ')


pat = r'^(\+?\d?\s?)?-?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
# pat = r'[\+\d\s]?-?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'

matchs = re.search(pat, phno)
if matchs:
    print('This number is valid')
else:
    print('This number is invalid')


#---------------------------------------------------------------------------------


# Method 2:

pattern = ['\d{10}', '\d{3}-\d{3}-\d{4}', '\d{3}.\d{3}.\d{4}', 
        '\(\d{3}\)\d{3}-\d{4}', '\(\d{3}\)-\d{3}-\d{4}',
        '\d{3}\s\d{3}\s\d{4}', '+\d\d{10}', '+\d\s\d{3}.\d{3}.\d{4}', 
        '+\d{3}-\d{3}-\d{4}', '\d-\d{3}-\d{3}-\d{4}']

phno = input('enter a contact number: ')

def fun(pattern, phno):
    for i in range(0,len(pattern)):
        matchs = re.findall(pattern[i], phno)
        if matchs:
            return True
    return False

if fun(pattern, phno):
    print('This number is valid')
else:
    print('This number is invalid')

