#tests/test_factorial.py
from funciones.factorial import factorial
def test_factorial():
 assert factorial(5) == 120
 assert factorial(-3) is None

