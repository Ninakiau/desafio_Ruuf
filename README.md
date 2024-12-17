# 🧩 **Calculadora de Paneles Solares**

Este proyecto resuelve un problema matemático de optimización para determinar la **máxima cantidad de paneles solares** que pueden caber dentro de un techo rectangular o triangular.

## 📋 **Descripción del Proyecto**
 
El algoritmo implementado realiza lo siguiente:
- Calcula la cantidad máxima de paneles solares en un **techo rectangular**.
- Calcula la cantidad máxima de paneles solares en un **techo triangular isósceles** (BONUS).

---

## 🛠️ **Instrucciones de Ejecución**

1. **Clona este repositorio** en tu máquina local:
   ```bash
   git clone https://github.com/Ninakiau/desafio_Ruuf.git
   cd tu-repositorio
   ```

2. **Requisitos**:
   - Asegúrate de tener **Python 3.x** instalado.
   - Jupyter Notebook (opcional si deseas correr el archivo .ipynb)

   ````bash
   pip install notebook
   ````

   

3. **Ejecuta el programa** desde la terminal:
   ```bash
   python panels.py
   ```

4. **Prueba el programa** con los siguientes casos:
   ```python
   # Ejemplo de ejecución para techo rectangular
   print(calculate_how_many_rectangles(2, 4, 1, 2))  # Salida esperada: 4
   print(calculate_how_many_rectangles(3, 5, 1, 2))  # Salida esperada: 7
   print(calculate_how_many_rectangles(1, 10, 2, 2)) # Salida esperada: 0

   # Ejemplo de ejecución para techo triangular
   print(calculate_panels_in_triangle(22, 10, 2, 1)) # Resultado detallado
   print(calculate_panels_in_triangle(8, 10, 1, 2))  # Resultado detallado
   ```

---

## 🚀 **Funciones Implementadas**

### 1. **`calculate_how_many_rectangles()`**
Esta función calcula cuántos paneles rectangulares pueden caber dentro de un techo rectangular.

#### Parámetros:
- `roof_length` (float): Longitud del techo.
- `roof_width` (float): Ancho del techo.
- `rectangle_length` (float): Longitud del panel solar.
- `rectangle_width` (float): Ancho del panel solar.

#### Ejemplo:
```python
calculate_how_many_rectangles(3, 5, 1, 2) # Salida esperada: 7
```

---

### 2. **`calculate_panels_in_triangle()`**  
Esta función calcula cuántos paneles caben en un **techo triangular isósceles**, probando dos orientaciones posibles de los paneles solares (horizontal y vertical).

#### Parámetros:
- `roof_height` (float): Altura del triángulo.
- `roof_width` (float): Ancho de la base del triángulo.
- `panel_length` (float): Longitud del panel solar.
- `panel_width` (float): Ancho del panel solar.

#### Ejemplo:
```python
calculate_panels_in_triangle(22, 10, 2, 1)
```

---

## ✅ **Casos de Prueba**

### Rectangular:
| Paneles  | Techo | Resultado |
|----------|-------|-----------|
| 1x2      | 2x4   | 4         |
| 1x2      | 3x5   | 7         |
| 2x2      | 1x10  | 0         |

### Triangular:
| Techo (Alto x Base) | Paneles  | Resultado Detallado |
|----------------------|----------|---------------------|
| 22x10               | 2x1      | Detalle de paneles  |
| 8x10                | 1x2      | Detalle de paneles  |

---

## 🌟 **Bonus**
El programa optimiza entre las orientaciones de los paneles solares:
- **Horizontal**
- **Vertical**

La solución final devuelve la cantidad máxima de paneles con la orientación más eficiente.

---

## 🔗 **Enlaces**
- 👉[Repositorio en GitHub de Claudia Ortiz](https://github.com/Ninakiau)
- 🌚[LinkedIn](https://www.linkedin.com/in/claudia-dev/)

---

