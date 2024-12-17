import math

def calculate_how_many_rectangles(roof_length, roof_width, rectangle_length, rectangle_width):
    if any(val <= 0 for val in [roof_length, roof_width, rectangle_length, rectangle_width]):
        return "Todos los valores deben ser positivos"
    
    if max(rectangle_length, rectangle_width) > max(roof_length, roof_width) or min(rectangle_length, rectangle_width) > min(roof_length, roof_width):
        return "Los paneles no caben en el techo rectangular"
    else:
        return math.trunc((roof_length * roof_width) / (rectangle_length * rectangle_width))
        
# C A S O S   D E   P R U E B A 
print("C A S O S  D E  P R U E B A  T E C H O  R E C T A N G U L A R")
# Paneles 1x2 y techo 2x4 ⇒ Caben 4
print(f"Paneles 1x2 y techo 2x4 ⇒ Caben 4 : y la respuesta es:  {calculate_how_many_rectangles(2, 4, 1, 2)}")
# Paneles 1x2 y techo 3x5 ⇒ Caben 7
print(f"Paneles 1x2 y techo 3x5 ⇒ Caben 7 y la respuesta es: {calculate_how_many_rectangles(3, 5, 1, 2)}")
# Paneles 2x2 y techo 1x10 ⇒ Caben 0
print(f"Paneles 2x2 y techo 1x10 ⇒ Caben 0 y la respuesta es: {calculate_how_many_rectangles(1, 10, 2, 2)}")



def calculate_panels_in_triangle(roof_height, roof_width, panel_length, panel_width):
    # Validar que los parámetros de entrada sean positivos
    if any(val <= 0 for val in [roof_height, roof_width, panel_length, panel_width]):
        return "Todos los valores deben ser positivos"
    
    # Verificar que los paneles no sean más grandes que el techo
    if max(panel_length, panel_width) > max(roof_height, roof_width):
        return "Los paneles no pueden instalarse en el techo triangular"
    
    def count_panels_in_orientation(length, width):
        """
        Calcular paneles en una orientación específica
        length: dimensión más larga del panel
        width: dimensión más corta del panel
        """
        panels_total = 0
        # Determina cuantas filas de paneles caben en la altura del triángulo
        max_vertical_panels = int(roof_height // length) + 1
        
        for row in range(max_vertical_panels):
            # Calcular la longitud de la base del trapecio en la posición actual
            current_base_width = roof_width * (1 - ((row + 1) * length / roof_height))
            
            # Determinar cuántos paneles pueden colocarse horizontalmente en esta base
            panels_in_row = math.trunc(current_base_width / width)
            panels_total += panels_in_row
        
        return panels_total
    
    # Calcular paneles en ambas orientaciones
    panels_horizontal = count_panels_in_orientation(panel_length, panel_width)
    panels_vertical = count_panels_in_orientation(panel_width, panel_length)
    
    # Devolver la orientación con más paneles
    return {
        "Paneles horizontales": panels_horizontal,
        "Paneles verticales": panels_vertical,
        "Orientación óptima": "Horizontal" if panels_horizontal >= panels_vertical else "Vertical",
        "Número máximo de paneles": max(panels_horizontal, panels_vertical)
    }
print("C A S O S  D E  P R U E B A  T E C H O  Y R I A N G U L A R ")
# Ejemplos de uso
print(calculate_panels_in_triangle(22, 10, 2, 1))
print(calculate_panels_in_triangle(8, 10, 1, 2))