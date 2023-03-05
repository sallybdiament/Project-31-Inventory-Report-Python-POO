from inventory_report.inventory.product import Product


def test_cria_produto():
    result = Product('a', 'a', '12/2/22', '12/2/22', 5, 'a')
    assert result is None
