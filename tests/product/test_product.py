from inventory_report.inventory.product import Product


def test_cria_produto():
    result = f"{Product('1', 'a', 'a', '12/2/22', '12/2/22', 5, 'a')}"
    exp = "O produto a fabricado em 12/2/22 por a com validade "
    exp2 = "até 12/2/22 precisa ser armazenado a."
    assert result == exp+exp2
