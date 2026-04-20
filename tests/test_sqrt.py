"""Tests para la función sqrt(x) -> float."""

import pytest

from src.calculator import sqrt


# --- EJEMPLO (no borrar) ---
def test_sqrt_cuadrado_perfecto():
    """Ejemplo: la raíz de 9 debe dar 3.0."""
    assert sqrt(9) == 3.0


# --- TU TURNO ---
# Usamos parametrize para las raíces válidas
@pytest.mark.parametrize("x, expected", [
    (0, 0.0),           # Raíz de 0 (resultado: 0.0)
    (56.25, 7.5),       # Raíz de un número que no es cuadrado perfecto (resultado decimal exacto)
    (289, 17.0),        # Otro cuadrado perfecto con números nuevos
])
def test_sqrt_parametrizado(x, expected):
    """Verifica raíces cuadradas de cero y números con resultado decimal."""
    assert sqrt(x) == expected


# Test especial para la excepción de números negativos
def test_sqrt_negativo():
    """Verifica que calcular la raíz de un número negativo lance un ValueError."""
    # Si sqrt() no frena la ejecución al recibir -144, el test fallará
    with pytest.raises(ValueError):
        sqrt(-144)