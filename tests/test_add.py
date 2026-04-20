"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add


# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3


# --- TU TURNO ---
# Parametrize para probar todos los casos pedidos de una sola vez
@pytest.mark.parametrize("a, b, expected", [
    (-10, -15, -25),       # Sumar dos números negativos
    (20, -5, 15),        # Sumar un número positivo y uno negativo
    (0, 42, 42),          # Sumar con cero
    (3.2, 4.7, 7.9),    # Sumar dos números decimales (float)
])

def test_add_parametrizado(a, b, expected):
    """Verifica la suma con negativos, ceros y decimales."""
    assert add(a, b) == expected
