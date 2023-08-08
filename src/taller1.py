# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: title,-all
#     formats: py:percent,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.0
# ---

# %% [markdown]
# # Introducción a High-Performance Computing
# ---
#
# - **Taller 1**: numpy.
# - **Fecha de entrega**: 5 de septiembre de 2023.
# - **Enlace de entrega**: https://forms.gle/4jft6rSfKcbvh81QA
#
# Importamos librerías:

# %% [code]
import random
import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import ArrayLike
from collections import Counter
from typing import Dict, List, Tuple
from IPython.display import display

# %% [markdown]
# ## Punto 1
# ---
#
# En este punto deberá implementar una función que con operaciones de `numpy` permita calcular las proporciones de letras en una secuencia de texto dada. Debe replicar el comportamiento de la función `letter_count_python`:

# %% [code]
def letter_count_python(seq: str) -> Dict:
    counts = Counter(seq)
    acum = sum(counts.values())
    probs = {key: val / acum for key, val in counts.items()}
    return probs

# %% [markdown]
# Implemente la función `letter_count_numpy`. Está prohibido utilizar ciclos `for` o `while`.

# %% [code]
def letter_count_numpy(seq: str) -> Dict:
    ...

# %% [markdown]
# Las salidas deben ser iguales:

# %% [code]
seq = "thank you, this solved my problem. I think it's a matter of kernel changes."

# %% [code]
display(letter_count_python(seq))

# %% [code]
display(letter_count_numpy(seq))

# %% [markdown]
# ## Punto 2
# ---
#
# En este punto deberá implementar una función que con operaciones de `numpy` permita calcular el valor esperado a partir de un arreglo de valores y sus respectivas probabilidades.
#
# Recuerde que el valor esperado está dado por la siguiente ecuación:
#
# $$
# \mathbb{E}[x] = \sum_i P(x_i) x_i
# $$
#
# Debe replicar el comportamiento de la función `expected_value_python`:

# %% [code]
def expected_value_python(vals: List[float], probs: List[float]) -> float:
    return sum(
            a * b
            for a, b in zip(vals, probs)
            )

# %% [markdown]
# Implemente la función `expected_value_numpy`. Está prohibido utilizar ciclos `for` o `while`.

# %% [code]
def expected_value_numpy(vals: ArrayLike, probs: ArrayLike) -> float:
    ...

# %% [markdown]
# Las salidas deben ser iguales:

# %% [code]
vals = [1., 2., 3., 4.]
probs = [0.3, 0.2, 0.3, 0.2]
display(expected_value_python(vals, probs))

# %% [code]
vals = np.array([1., 2., 3., 4.])
probs = np.array([0.3, 0.2, 0.3, 0.2])
display(expected_value_numpy(vals, probs))

# %% [markdown]
# ## Punto 3
# ---
#
# En este punto deberá implementar el [juego del caos](https://en.wikipedia.org/wiki/Chaos_game) con `numpy`.
#
# La idea es poder replicar el triangulo de Sierpinski implementado en la función `chaos_game_python`:

# %% [code]
def chaos_game_python(n_samples: int) -> List[Tuple[float, float]]:
    points = []
    vertex = [
            (0, 0),
            (0.5, 1),
            (1, 0)
            ]
    p0 = (random.random(), random.random())
    for _ in range(n_samples):
        p1 = random.choice(vertex)
        p0 = (
                (p1[0] + p0[0]) / 2,
                (p1[1] + p0[1]) / 2
                )
        points.append(p0)
    return points

# %% [markdown]
# Debe implementar la función `chaos_game_numpy`. Puede utilizar únicamente un ciclo `for` o `while`:

# %% [code]
def chaos_game_numpy(n_samples: int) -> ArrayLike:
    ...

# %% [markdown]
# Las imagenes deben mostrar una figura similar:

# %% [code]
vals = chaos_game_python(n_samples=10_000)
vals = np.array(vals)
fig, ax = plt.subplots()
ax.scatter(vals[:, 0], vals[:, 1], alpha=0.3, s=2)
fig.show()

# %% [code]
vals = chaos_game_numpy(n_samples=10_000)
fig, ax = plt.subplots()
ax.scatter(vals[:, 0], vals[:, 1], alpha=0.3, s=2)
fig.show()

# %% [markdown]
# ## Punto 4
# ---
#
# Un prestigioso restaurante conocido como _Grandes Comelones_ realizó un evento que consistía en comer muchas hamburguesas en menos de 10 minutos. Las reglas eran las siguientes:
#
# - Si la persona se come más de 10 hamburguesas en el tiempo dado, la comida es gratis.
# - Si la persona no come más de 10 hamburguesas, deberá pagar cada una de las hamburguesas que comió (con sus respectivos precios).
# - El restaurante ofrece tres tipos de hamburguesas: "pollo" (15.000$), "carne" (17.000$) y "pescado" (20.000$).
#
# La idea de este punto es calcular las ganancias obtenidas durante el evento a partir de una matriz de recuentos de unidades vendidas. En esta matriz, cada fila representa un cliente y cada columna un tipo de hamburguesa (el orden de las columnas es pollo:0, carne:1 y pescado:2)
#
# Por ejemplo, en la siguiente matriz:
#
# ```
# [
#  [1, 2, 3],
#  [3, 2, 3]
# ]
# ```
#
# El segundo cliente consumió 3 hamburguesas de pollo, 2 de carne y 3 de pescado.
#
# La idea es replicar la función `burguer_sales_python`:

# %% [code]
def burguer_sales_python(counts:ArrayLike) -> float:
    prices = [15_000, 17_000, 20_000]
    acum = 0
    for customer in range(counts.shape[0]):
        customer_units = 0
        for burger in range(counts.shape[1]):
            customer_units += counts[customer, burger]
        if customer_units > 10:
            continue
        else:
            total_sale = sum(
                    a * b
                    for a, b in zip(prices, counts[customer])
                    )
            acum += total_sale
    return acum

# %% [markdown]
# Debe implementar la función `burguer_sales_numpy`. No puede utilizar ciclos `for` o `while`.

# %% [code]
def burguer_sales_numpy(counts: ArrayLike) -> float:
    ...

# %% [markdown]
# Las salidas deben ser iguales:

# %% [code]
counts = np.array([
    [3, 2, 3],
    [5, 5, 1],
    [10, 0, 0],
    [1, 1, 1],
    [0, 11, 0],
    [0, 0, 15],
    ])
display(burguer_sales_python(counts))

# %% [code]
counts = np.array([
    [3, 2, 3],
    [5, 5, 1],
    [10, 0, 0],
    [1, 1, 1],
    [0, 11, 0],
    [0, 0, 15],
    ])
display(burguer_sales_numpy(counts))
