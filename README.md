# Práctica de Estática - Ley de Hooke

Este repositorio contiene un script en Python que genera gráficas de **regresión lineal** a partir de datos experimentales de elongación y fuerza obtenidos en una práctica de laboratorio sobre la **Ley de Hooke**.

## 📌 Propósito del Código

El objetivo del código es:

- Visualizar la relación entre la **fuerza aplicada (N)** y la **elongación (m)** de dos resortes distintos.
- Calcular y mostrar la **constante elástica** (\(k\)) de cada resorte mediante una regresión lineal.
- Comprobar experimentalmente la validez de la **Ley de Hooke**:  
  \[
  F = k \cdot \Delta L
  \]

## 📊 ¿Qué hace el script?

- Recibe los valores de masa, longitud inicial y final del resorte.
- Convierte los datos a unidades del Sistema Internacional (metros y newtons).
- Calcula la elongación y la fuerza.
- Aplica una **regresión lineal** para encontrar el valor de \(k\).
- Genera dos gráficas:
  - **Primera configuración** (resorte más flexible)
  - **Segunda configuración** (resorte más rígido)

## 🧪 Contexto

Esta práctica se realizó como parte del curso de **Estática** en la Universidad Anáhuac Mayab, con el objetivo de comprobar experimentalmente el comportamiento elástico de los materiales y validar la Ley de Hooke.

## 🛠 Requisitos

- Python 3.x
- Bibliotecas:
  - matplotlib
  - numpy

Puedes instalarlas con:

```bash
pip install matplotlib numpy
```

📚 Créditos
Práctica realizada por el equipo:
Pedro Guillermo Moguel Vela, Jose Ricardo Pacheco Chanico, Helena Isabel Correa Sandoval, Fátima Guadalupe Navas Ramírez, Valentina Ordóñez Gutiérrez

Profesor: Marco Antonio Reyes García
Universidad Anáhuac Mayab – Ingeniería en Tecnologías de la Información
