import pytest
from app.calculator import apply_discount

def test_discount_applied():
    assert apply_discount(1200) == 1020  # CP01

def test_negative_amount_error():
    with pytest.raises(ValueError):
        apply_discount(-50)              # CP02

def test_boundary_limit():
    assert apply_discount(1000) == 1000  # CP03