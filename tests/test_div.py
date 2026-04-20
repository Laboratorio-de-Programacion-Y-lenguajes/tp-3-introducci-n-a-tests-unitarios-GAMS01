"""Tests para la función div(a, b) -> float."""

import pytest

from src.calculator import div


# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0


# --- TU TURNO ---
# 1. Usamos parametrize para las divisiones que dan un número (flotantes y negativos)
@pytest.mark.parametrize("a, b, expected", [
    (33, 2, 16.5),      # División que da resultado decimal (float)
    (50, -2, -25.0),    # División con números negativos (uno negativo)
    (-144, -12, 12.0),  # División con dos números negativos
    (0, 55, 0.0),       # Cero dividido por cualquier número
])
def test_div_parametrizado(a, b, expected):
    """Verifica la división con decimales y negativos."""
    assert div(a, b) == expected


# 2. Test especial para comprobar que la calculadora "grite" si dividimos por cero
def test_div_por_cero():
    """Verifica que dividir por cero lance un ZeroDivisionError."""
    # El bloque 'with' atrapa el error. Si div(73, 0) NO lanza el error, el test falla.
    with pytest.raises(ZeroDivisionError):
        div(73, 0)