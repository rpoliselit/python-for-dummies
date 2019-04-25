"""
Make a program that reads the full name of a person,
and returns on console:
1-The name with all capital letters.
2-The name with all lowercase letters.
3-How many letters without spaces.
4-How many letters in only first name.
5-Show first and last names in different lines
"""

name = str(input('Enter your fullname:\n')).strip()

print('-'*20,'\nUppercase: ',name.upper())
print('-'*20,'\nLowercase: ',name.lower())
#print('-'*20,'\nNumber of letters: {}'.format(len(name) - name.count(' ')))
print('-'*20,'\nNumber of letters:',len(''.join(name.split())))
print('-'*20,'\nLength of first name: ',len(name.split()[0]))
print('-'*20,'\nFirst name: ',name.split()[0])
print('-'*20,'\nLast name: ',name.split()[-1])
