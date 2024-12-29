from calculations import calculate_annuity, calculate_mortgage, estimate_retirement_balance, time_to_double, solve_logarithmic, to_scientific_notation, from_scientific_notation
import pytest

def test_calculate_annuity():
    assert calculate_annuity(1000, 0.05, 10, False) == pytest.approx(12833.59, rel=1e-2)

def test_calculate_mortgage():
    assert calculate_mortgage(200000, 0.04 / 12, 30 * 12) == pytest.approx(954.83, rel=1e-2)

def test_estimate_retirement_balance():
    assert estimate_retirement_balance(500, 10000, 0.07, 30 * 12) == pytest.approx(1000000.00, rel=1e-2)

def test_time_to_double():
    assert time_to_double(0.07) == pytest.approx(10.24, rel=1e-2)

def test_solve_logarithmic():
    assert solve_logarithmic(10, 100) == 2

def test_to_scientific_notation():
    assert to_scientific_notation(12345) == "1.2345e+04"

def test_from_scientific_notation():
    assert from_scientific_notation("1.2345e+04") == 12345.0