"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


# --- TU TURNO ---
# Usamos parametrize para probar todos los casos pedidos de una sola vez
@pytest.mark.parametrize("a, b, expected", [
    (128, 0, 0),        # Multiplicar por cero
    (-7, -8, 56),       # Multiplicar dos números negativos (resultado positivo)
    (-11, 5, -55),      # Multiplicar un positivo y un negativo (resultado negativo)
    (404, 1, 404),      # Multiplicar por 1 (elemento neutro)
    (3.5, 2.0, 7.0),    # Multiplicar dos decimales (float)
])
def test_mul_parametrizado(a, b, expected):
    """Verifica la multiplicación con ceros, negativos, neutro y decimales."""
    assert mul(a, b) == expected
