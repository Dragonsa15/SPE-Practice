from cmath import e
import pytest
from Calc import Calculator
import math
# "Constants"
# Testing code for calculator Class

NUMBER_1 = 16
NUMBER_2 = 1


# Fixtures
@pytest.fixture
def calculator():
    return Calculator()


@pytest.mark.parametrize("a,expected", [
    (NUMBER_1, math.sqrt(NUMBER_1)),
    (NUMBER_2, math.sqrt(NUMBER_2)),
])
def test_sqrt(calculator,a,expected):
    try:
        answer = calculator.ChoiceMapping(1,[a])    
        # print(a,expected,answer)
        assert expected == answer
    except EOFError as e:
        print(end="")



@pytest.mark.parametrize("a,expected", [
    (NUMBER_1, math.factorial(NUMBER_1)),
    (NUMBER_2, math.factorial(NUMBER_2)),
])
def test_fac(calculator,a,expected):
    try:
        answer = calculator.ChoiceMapping(2, [a])
        assert expected == answer
    except EOFError as e:
        print(end="")
    

@pytest.mark.parametrize("a,expected", [
    (NUMBER_1, math.log(NUMBER_1)),
    (NUMBER_2, math.log(NUMBER_2)),
])
def test_log(calculator,a,expected):
    try:
        answer = calculator.ChoiceMapping(3, [a])
        assert expected == answer
    except EOFError as e:
        print(end="")
    

@pytest.mark.parametrize("a,b,expected", [
    (NUMBER_1, NUMBER_2, math.pow(NUMBER_1,NUMBER_2)),
    (NUMBER_2, NUMBER_1, math.pow(NUMBER_2,NUMBER_1)),
])
def test_pow(calculator,a,b,expected):
    try:
        answer = calculator.ChoiceMapping(4,[a,b])
        assert expected == answer
    except EOFError as e:
        print(end="")
    

def test_baseScreen(calculator):
    try:
        calculator.BaseScreen()
        assert True
    except EOFError as e:
        print(end="")

