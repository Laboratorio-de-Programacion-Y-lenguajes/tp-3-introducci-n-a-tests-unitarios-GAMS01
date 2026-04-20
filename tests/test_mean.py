"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0


# --- TU TURNO ---
# Usamos parametrize para las listas con datos válidos
@pytest.mark.parametrize("values, expected", [
    ([73.0], 73.0),                     # Lista con un solo elemento
    ([-10, -20, -30, -40], -25.0),      # Lista con números negativos
    ([1.5, 3.5, 7.0], 4.0),             # Lista con números decimales (float)
])
def test_mean_parametrizado(values, expected):
    """Verifica el promedio con listas de un elemento, negativos y decimales."""
    assert mean(values) == expected


# Test especial para la excepción de lista vacía
def test_mean_lista_vacia():
    """Verifica que calcular el promedio de una lista vacía lance un ValueError."""
    # Si mean() no lanza un error al recibir [], el test fallará
    with pytest.raises(ValueError):
        mean([])