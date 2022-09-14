import pytest
from triangle import classify_triangle, right_triangle

#Unit testing 6 cases below:
@pytest.mark.parametrize("a,b,c", (
    (3,4,5),
    (5,12,13),
    (8,15,17),
    (3,4,6)
))
def test_right_triangle(a,b,c):
    test_triangle = right_triangle(a,b,c)
    assert test_triangle == "Right Angle","c square is not equal to a square plus b square."

@pytest.mark.parametrize("a,b,c", (
    (3,3,3),
    (12,12,12),
    (8,8,9),
    (7,4,6)
))
def test_Equilateral_triangle(a,b,c):
    test_triangle = classify_triangle(a,b,c)
    assert test_triangle == "Equilateral","all sides should be of same length."

@pytest.mark.parametrize("a,b,c", (
    (5,4,5),
    (12,12,13),
    (8,15,15),
    (4,4,6)
))
def test_Isosceles_triangle(a,b,c):
    test_triangle = classify_triangle(a,b,c)
    assert test_triangle == "Isosceles","two sides should be of same length."

@pytest.mark.parametrize("a,b,c", (
    (3,4,5),
    (5,12,13),
    (8,15,17),
    (3,4,6)
))
def test_Scalene_triangle(a,b,c):
    test_triangle = classify_triangle(a,b,c)
    assert test_triangle == "Scalene","all sides should be different lengths."