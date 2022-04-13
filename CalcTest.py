from cmath import e
import pytest
from Calc import Calculator
import math
# "Constants"

NUMBER_1 = 16
NUMBER_2 = 1


# Fixtures

@pytest.fixture
def calculator():
    return Calculator()


# Helpers



# Test Cases

@pytest.mark.parametrize("a,expected", [
    (NUMBER_1, math.sqrt(NUMBER_1)),
    (NUMBER_2, math.sqrt(NUMBER_2)),
])
def test_sqrt(calculator,a,expected):
    answer = calculator.ChoiceMapping(1,[a])    
    print(a,expected,answer)
    assert expected == answer



@pytest.mark.parametrize("a,expected", [
    (NUMBER_1, math.factorial(NUMBER_1)),
    (NUMBER_2, math.factorial(NUMBER_2)),
])
def test_fac(calculator,a,expected):
    answer = calculator.ChoiceMapping(2, [a])
    assert expected == answer


@pytest.mark.parametrize("a,expected", [
    (NUMBER_1, math.log(NUMBER_1)),
    (NUMBER_2, math.log(NUMBER_2)),
])
def test_log(calculator,a,expected):
    answer = calculator.ChoiceMapping(3, [a])
    assert expected == answer


@pytest.mark.parametrize("a,b,expected", [
    (NUMBER_1, NUMBER_2, math.pow(NUMBER_1,NUMBER_2)),
    (NUMBER_2, NUMBER_1, math.pow(NUMBER_2,NUMBER_1)),
])
def test_pow(calculator,a,b,expected):
    answer = calculator.ChoiceMapping(4,[a,b])
    assert expected == answer


# def test_divide_by_zero(calculator):
#     with pytest.raises(ZeroDivisionError) as e:
#         calculator.divide(NUMBER_1, 0)
#     assert "division by zero" in str(e.value)


