"""classify_triangle() is a function that takes three  parameters: a, b, and c. 
The three parameters represent the lengths of the sides of a triangle. 
The function returns a string that specifies whether the triangle is 
scalene, isosceles, or equilateral, and whether it is a right triangle as well.
"""

def classify_triangle(a, b, c):

    if a==b and b==c:
        triangle_type = "Equilateral"
        return triangle_type

    elif a==b or b==c or a==c:
        triangle_type = "Isosceles"
        return triangle_type

    else:
        triangle_type = "Scalene"
        return triangle_type

def right_triangle(a, b, c):

    if (a*a)+(b*b) == (c*c):
        triangle_type = "Right Angle"
        return triangle_type