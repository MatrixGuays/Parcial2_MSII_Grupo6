from funciones.dividir import dividir

def test_dividir():
    """Pruebas para la función dividir"""
    # Caso normal
    assert dividir(10, 2) == 5
    assert dividir(15, 3) == 5
    assert dividir(7, 2) == 3.5
    
    # División por cero
    assert dividir(5, 0) is None
    assert dividir(0, 0) is None
    
    # Números negativos
    assert dividir(-10, 2) == -5
    assert dividir(10, -2) == -5
    assert dividir(-10, -2) == 5