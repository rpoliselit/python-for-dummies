from fp002_Vector2D import Vector

def new_print(string):
    print('_'*30 + '\n' + str(string))

v1 = Vector(3,4)
v2 = Vector(10,-7)

new_print(v1)
new_print(abs(v1))
new_print(bool(v1))
new_print(v1 + v2)
new_print(abs(v1 + v2))
new_print(v1 * 2)
