"""
Make an algoritm that reads the wage of employee,
and returns the new wage with increase of 15%.
"""

list_wage = []
number_employees = int(input('How many employees will be promoted? \n'))

for i in range(number_employees):
    list_wage.append(float(input('What is the wage {}? \n'.format(i+1))))

def promotion(percentage, wage = list_wage):
    new_wage = [j * (1 + percentage) for j in wage]
    for k in new_wage:
        print("New wage {}: US$ {:.2f}.".format(new_wage.index(k), k))

promotion(15/100)
