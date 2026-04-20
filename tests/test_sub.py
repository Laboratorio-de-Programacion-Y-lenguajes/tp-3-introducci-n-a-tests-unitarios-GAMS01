"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub


# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3


# --- TU TURNO ---
# Usamos parametrize para probar todos los casos pedidos de una sola vez
@pytest.mark.parametrize("a, b, expected", [
    (3, 10, -7),        # Restar un número mayor al primero (resultado negativo)
    (15, 0, 15),        # Restar cero
    (-12, -5, -7),      # Restar dos números negativos (-12 - (-5) = -7)
    (10.5, 2.5, 8.0),   # Restar dos números decimales (float)
])
def test_sub_parametrizado(a, b, expected):
    """Verifica la resta con casos borde y decimales."""
    assert sub(a, b) == expected
