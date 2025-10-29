from pytest import raises
from vector import Vector

def test_valid_init():
    v = Vector(1,2)
    assert v.numbers == (1,2)

# testing neg values
def test_negative_valid_init():
    v = Vector(-1, -5, 3)
    assert v.numbers == (-1, -5, 3)

# testing str in the init
def test_string_in_init_fails():
    with raises(TypeError):
        Vector("1")

# testing len() function
def test_diff_lengths():
    vectors = (Vector(1,2), Vector(1), Vector(1,2,3), Vector(1,2,3,4))
    expected_lengths(2,1,3,4)

# with 2 tuples, you can look through them with zip
    for vector, expected_length in zip(vectors, expected_lengths)

# test abs() function
def test_vector_norm_valid():
    v = Vector(1,4)
    expected_norm = (v[0]**2 + v[1]**2)
    assert abs(v) == approx(expected_norm)


def test_empty_vector_fail():
    with raises(ValueError):
        Vector()

