"""
Working with strings.
"""

text = str('The zen of Python')
text2 = str('   Praticing python   ')
print('-'*20)

#Slicing
print(text[5])
print(text[3:])
print(text[:10])
print(text[2:11:3])
print(text[-4])
print(text[::-1])
print('-'*20)

#Analyzing
print(len(text))
print(text.count('n'))
print(text.count('n',1,-5))
print(text.find('ho'))
print(text.find('CSharp'))
print('Python' in text)
print('CSharp' in text)
print('-'*20)

#Manipulating
print(text.replace('Python','CSharp'))
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text2.strip())
print(text2.rstrip())
print(text2.lstrip())
print('-'*20)

#Separeting and joining
print(text.split())
print('-'.join(text.split()))
