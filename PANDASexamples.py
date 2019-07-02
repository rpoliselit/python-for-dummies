import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#series
print(f'{" SERIES ":*^40}')
grades = pd.Series([3,8,5,10,7])
print(grades)
print('-'*40)
print(grades.values)
print('-'*40)
print(grades.index)
print('-'*40)
grades = pd.Series([3,8,5,10,7], index=["Newton", "Gauss", "Faraday", "Feynman", "Hooke"])
print(grades)
print('-'*40)
print(grades['Feynman'])
print('-'*40)
print(f'Mean value: {grades.mean():.2f}')
print(f'Standard deviation: {grades.std():.2f}')
print('-'*40)
print(grades.describe())


#data frame
print(f'{" DATA FRAME ":*^40}')
df = pd.DataFrame({'Students' : ["Newton", "Gauss", "Faraday", "Feynman", "Hooke"],
                   'Absences' : [3,4,2,1,4],
                   'Exams' : [3,8,5,10,7],
                   'Seminars': [8.5,7.5,9.0,7.5,8.0]})
print(df)
print('-'*40)
print(df.dtypes)
print('-'*40)
print(df.columns)
print('-'*40)
print(df['Seminars'])
print('-'*40)
print(df.sort_values(by='Seminars'))
print('-'*40)
print(df.describe())
print('-'*40)
print(df[df['Exams'] > 7.0])
print('-'*40)
print(df[(df['Seminars'] > 8.0) & (df['Absences'] < 3)])
print('-'*40)


#data manipulating

#data visualization
