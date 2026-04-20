"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8


# --- TU TURNO ---
# Usamos parametrize para cubrir las potencias especiales
@pytest.mark.parametrize("a, b, expected", [
    (999, 0, 1),        # Cualquier número elevado a 0 (resultado: 1)
    (42, 1, 42),        # Número elevado a 1 (resultado: el mismo número)
    (-5, 2, 25),        # Base negativa con exponente par (resultado positivo)
    (400, 0.5, 20.0),   # Exponente decimal, ej: 400 ** 0.5 (raíz cuadrada)
])
def test_pow_parametrizado(a, b, expected):
    """Verifica potencias con casos borde, exponentes pares y decimales."""
    assert pow_(a, b) == expected