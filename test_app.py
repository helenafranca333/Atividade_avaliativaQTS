from cantina import calcular_total, validar_pedido

def test_validar_pedido_quantidade_invalida():
    assert validar_pedido("Suco", 0, 5) == "Pedido inválido"


def test_calcular_total_erro():
    assert calcular_total(2, 5) == 11
