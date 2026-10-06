import pytest
from quote import build_quote

def hammer(quantity, stock=12):
    return {
        "id": 1,
        "name": "Hammer",
        "price": 10.0,
        "stock": stock,
        "quantity": quantity,
    }


def test_empty_input():
        lines = []
        with pytest.raises(ValueError,match="^quote needs at least one line$"): 
                build_quote(lines)

def test_item_quantity_zero():
        with pytest.raises(ValueError,match="^quantity must be at least 1 for Hammer"):
                build_quote([hammer(0)])
