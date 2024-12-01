import pytest
from quadratic_solver import solve_quadratic

def test_two_real_roots():
    assert solve_quadratic(1, -3, 2) == (2.0, 1.0)

def test_one_real_root():
    assert solve_quadratic(1, 2, 1) == (-1.0, -1.0)

def test_no_real_roots():
    assert solve_quadratic(1, 0, 1) == "Нет действительных корней"

def test_invalid_a():
    with pytest.raises(ValueError):
        solve_quadratic(0, 2, 1)
