"""
Make a program that has a function
called grades(), which one can get
several grades of a student.
It returns a dictionary with following
informations:
- Amount of grades
- Higher grade
- Lower grade
- Average grade
- Status (optional): Approved or disapproved.

Add docstrings
"""

def grades(*arg , status = False):
    """
    -> Student's school performance.
    :arg: grades of a students.
    :status: indicates whether student is approved or not.
    """
    dict = {'Amount' : len(arg),
            'Highter' : max(arg),
            'Lower' : min(arg),
            'Average': sum(arg)/len(arg)}

    if status == True:
        if dict['Average'] < 4.5:
            dict['Status'] = 'DISAPPROVED'
        elif dict['Average'] < 6:
            dict['Status'] = 'FINAL EXAM'
        else:
            dict['Status'] = 'APPROVED'

    return dict


#main program
ans = grades(5.3, 10, 3.5, status=True)
print('-'*40,'\n',ans)
