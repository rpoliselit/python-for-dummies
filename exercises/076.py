"""
Make a program that has a word with
several words, and show for each
word that they are like vowals.
"""

words = ('moonlight','holy','saber','hunter','doll','blood','great ones',
         'Ludwig','Ebrietas','Kos','sword','old','oaths','cainhurst')

#just to identify each vowals
# for word in words:
#     print(f'{word.upper()} contains the following vowals: ', end = '')
#     if word.find('a') != -1:
#         print('A', end = ' ')
#     if word.find('e') != -1:
#         print('E', end = ' ')
#     if word.find('i') != -1:
#         print('I', end = ' ')
#     if word.find('o') != -1:
#         print('O', end = ' ')
#     if word.find('u') != -1:
#         print('U', end = ' ')
#     print('')

#show all them, repeating if necessary
for word in words:
    print(f'{word.upper()} contains the following vowals: ', end = '')
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f'{letter.upper()}', end = ' ')
    print('')
