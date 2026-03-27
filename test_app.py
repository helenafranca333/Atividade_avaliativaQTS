from app import calcular_total, validar_pedido

def test_calcular_total_basico():
    assert calcular_total(2, 5) == 10


def test_calcular_total_zero():
    assert calcular_total(0, 10) == 0


def test_validar_pedido_valido():
    assert validar_pedido("Coxinha", 2, 5) == "Pedido válido"

