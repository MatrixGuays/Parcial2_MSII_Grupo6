from funciones.multiplicar import multiplicar

def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(-2, 5) == -10