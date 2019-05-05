"""
Make a program that reads a sentence
and identifies whether it is a palindrome
or not, disregarding the spaces.
"""
print('{:=^40}'.format(' PALINDROME ANALYSIS '))

sentence0 = str(input('Type a sentense:\n')).upper().split()
sentence1 = ''.join(sentence0) #to be checked
sentence2 = ' '.join(sentence0) #to be print

print('-'*40)
print('This sentense "{}" '.format(sentence2), end = '')

#alternative without 'for'
#if sentence1 == sentence1[::-1]:
#    print('is a palindrome!!!!')
#else:
#    print('is NOT a palindrome...')


sum = 0
for k in range(0,len(sentence1)):
    if sentence1[k] == sentence1[-1*(k+1)]:
        sum += 1
if sum == len(sentence1):
    print('is a PALINDROME!!!!')
else:
    print('is NOT a palindrome...')
