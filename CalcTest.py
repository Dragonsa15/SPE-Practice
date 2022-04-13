from Calc import Calculator 
import math

print(Calculator)
def test_calc_sqrt():
    # "Verify the output of `calc_addition` function"
    Calc = Calculator("")
    output = Calc.sqrt(4)
    assert output == 2
 
def test_calc_factorial():
    # “””Verify the output of `calc_substraction` function”””
    Calc = Calculator("")
    output = Calc.factorial(2)
    assert output == 2
     
def test_calc_log():
    # “””Verify the output of `calc_multiply` function”””
    Calc = Calculator("")
    output = Calc.log(10)
    assert output == math.log(10)

def test_calc_pow():
    Calc = Calculator("")
    output = Calc.pow(2,2)
    assert output == 4

