"""
Make a program that reads height and weight of
a person, calculates its body mass index (BMI),
and returns the status accourding to:
- Very severely underweight: to 15
- Severely underweight: from 15 to 16
- Underweight: from 16 to 18.5
- Normal (healthy weight): from 18.5 to 25
- Overweight: from 25 to 30
- Obese Class I (Moderately obese): from 30 to 35
- Obese Class II (Severely obese): from	35 to 40
- Obese Class III (Very severely obese): from 40 to 45
- Obese Class IV (Morbidly Obese): from 45 to 50
- Obese Class V (Super Obese): from 50 to 60
- Obese Class VI (Hyper Obese): from 60
"""
print('{}\nBODY MASS INDEX\n{}'.format('+=+'*20,'+=+'*20))
mass = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in metters: '))

bmi = mass / height**2

print('Your BMI is {:.1f}.'.format(bmi))

if bmi < 15:
    print('VERY SEVERELY UNDERWEIGHT!!')
elif bmi < 16:
    print('severely underweight!'.upper())
elif bmi < 18.5:
    print('underweight.'.title())
elif bmi < 25:
    print('healthy weight.'.capitalize())
elif bmi < 30:
    print('Overweight.')
elif bmi < 35:
    print('Moderately obese!'.upper())
elif bmi  < 40:
    print('SEVERELY obese!!'.upper())
elif bmi < 45:
    print('very severely obese!!!'.upper())
elif bmi < 50:
    print('Morbidly obese!!!!'.upper())
elif bmi < 60:
    print('super obese!!!!!'.upper())
elif bmi >= 60:
    print('hyper obese!!!!!!'.upper())
