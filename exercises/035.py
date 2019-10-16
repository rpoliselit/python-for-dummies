"""
Make a program that reads the length of three lines,
and returns whether they can form a triangle.
"""

edges = []
triangle = False

for k in range(3):
    edges.append(float(input('{}º length: '.format(k+1))))

if edges[0] + edges[1] > edges[2] \
    and edges[1] + edges[2] > edges[0] \
    and edges[0] + edges[2] > edges[1]:
    triangle = True

print('-'*20)
print("""Is it possible to create a triangle
with edges {:.1f}, {:.1f}, and {:.1f}?""".format(edges[0],edges[1],edges[2]))
print(triangle)
