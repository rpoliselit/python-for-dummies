"""
Make a program that reads some phrase,
and returns:
1-number of times the letter 'A' appears
2-which is the position of first 'A'
3-which is the position of last 'A'
"""

phrase = str(input('Enter a phrase:\n')).strip().upper()

print('This has {} A letter.'.format(phrase.count('A')))
print('The first A is at {}º.'.format(phrase.find('A'))+1)
print('The last A is at {}º.'.format(phrase.rfind('A'))+1)
