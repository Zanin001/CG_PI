import matplotlib.pyplot as plt
import math

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Entrada inválida")

def calculate_distance(point1, point2):
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5

def is_triangle(side_lengths):
    a, b, c = sorted(side_lengths)
    
    if (a + b > c):
        if (a == b and a == c):
            return True, "As coordendas forma um triângulo equilatero"
        if (a == b or a == c or b == c):
            return True, "As coordendas forma um triângulo isósceles"
        if (a != b and a != c and b != c):
            return True, "As coordendas forma um triângulo escaleno"

    return False, "As coordenadas não foram um triângulo"

def calculate_angles(coordinates):
    if len(coordinates) != 4:
        return []

    angles = []
    for i in range(4):
        p1, p2, p3 = coordinates[i], coordinates[(i + 1) % 4], coordinates[(i + 2) % 4]

        vector1 = (p2[0] - p1[0], p2[1] - p1[1])
        vector2 = (p3[0] - p2[0], p3[1] - p2[1])
        dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]
        magnitude1 = math.sqrt(vector1[0]**2 + vector1[1]**2)
        magnitude2 = math.sqrt(vector2[0]**2 + vector2[1]**2)
        angle = math.degrees(math.acos(dot_product / (magnitude1 * magnitude2)))
        angles.append(angle)

    return angles

def is_quadrilateral(coordinates):
    angles = calculate_angles(coordinates)

    a = calculate_distance(coordinates[0], coordinates[1])
    b = calculate_distance(coordinates[1], coordinates[2])
    c = calculate_distance(coordinates[2], coordinates[3])
    d = calculate_distance(coordinates[3], coordinates[0])

    if all(angle == 90 for angle in angles):
        if (a == b and c == d):
            return True, "As coordenadas formam um quadrado"
        else:
            return True, "As coordenadas formam um retângulo"

    return False, "As coordenadas não formam um quadrilátero"

def plot_form(coordinates, title):
    x_coords, y_coords = zip(*coordinates)
    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]
    
    plt.plot(x_coords, y_coords, marker='x')
    plt.title(title)
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.grid(True)
    plt.axis('auto')
    plt.show(block=False)

def get_triangle(): 
    coordinates = []

    for i in range(3):
        x = get_float_input(f"Digite a coordenada x{i + 1}: ")
        y = get_float_input(f"Digite a coordenada y{i + 1}: ")
        coordinates.append((x, y))

    side_lengths = [calculate_distance(coordinates[0], coordinates[1]),
                    calculate_distance(coordinates[1], coordinates[2]),
                    calculate_distance(coordinates[2], coordinates[0])]

    isTriangle, message = is_triangle(side_lengths)

    print(message)
    if isTriangle:
        plot_form(coordinates, message)
        return coordinates
    return []

def get_quadrilateral():
    coordinates = []

    for i in range(4):
        x = get_float_input(f"Digite a coordenada x{i + 1}: ")
        y = get_float_input(f"Digite a coordenada y{i + 1}: ")
        coordinates.append((x, y))

    isSquare, message = is_quadrilateral(coordinates)
    
    print(message)
    if isSquare:
        plot_form(coordinates, message)
        return coordinates
    return []

def translate_shape(shape, dx, dy):
    translated_shape = [(x + dx, y + dy) for x, y in shape]
    return translated_shape

def scale_uniformly(shape, scale_factor):
    scaled_shape = [(x * scale_factor, y * scale_factor) for x, y in shape]
    return scaled_shape

def scale_nonuniformly(shape, scale_x, scale_y):
    scaled_shape = [(x * scale_x, y * scale_y) for x, y in shape]
    return scaled_shape

def rotate_clockwise(shape, angle_degrees, origin):
    angle_radians = math.radians(angle_degrees)
    rotated_shape = []
    for x, y in shape:
        translated_x = x - origin[0]
        translated_y = y - origin[1]
        rotated_x = translated_x * math.cos(angle_radians) + translated_y * math.sin(angle_radians)
        rotated_y = -translated_x * math.sin(angle_radians) + translated_y * math.cos(angle_radians)
        new_x = rotated_x + origin[0]
        new_y = rotated_y + origin[1]
        rotated_shape.append((new_x, new_y))
    return rotated_shape

def rotate_counterclockwise(shape, angle_degrees, origin):
    angle_radians = math.radians(angle_degrees)
    rotated_shape = []
    for x, y in shape:
        translated_x = x - origin[0]
        translated_y = y - origin[1]
        rotated_x = translated_x * math.cos(angle_radians) - translated_y * math.sin(angle_radians)
        rotated_y = translated_x * math.sin(angle_radians) + translated_y * math.cos(angle_radians)
        new_x = rotated_x + origin[0]
        new_y = rotated_y + origin[1]
        rotated_shape.append((new_x, new_y))
    return rotated_shape

def transform_form(coordinates):
    print("1 - Translação")
    print("2 - Escala Uniforme")
    print("3 - Escala não Uniforme")
    print("4 - Rotação no Sentido Horário")
    print("5 - Rotação no Sentido Anti-Horário")
    response = input("Qual transformação geométrica? ")  

    if response == "1":
        print("Translação")
        dx = get_float_input("Informe a quantidade de translação no eixo X: ")
        dy = get_float_input("Informe a quantidade de translação no eixo Y: ")
        coordinates = translate_shape(coordinates, dx, dy)
        plot_form(coordinates, "Forma após Translação")
    elif response == "2":
        print("Escala Uniforme")
        scale_factor = get_float_input("Informe o fator de escala uniforme: ")
        coordinates = scale_uniformly(coordinates, scale_factor)
        plot_form(coordinates, "Forma após Escala Uniforme")
    elif response == "3":
        print("Escala não Uniforme")
        scale_x = get_float_input("Informe o fator de escala no eixo X: ")
        scale_y = get_float_input("Informe o fator de escala no eixo Y: ")
        coordinates = scale_nonuniformly(coordinates, scale_x, scale_y)
        plot_form(coordinates, "Forma após Escala não Uniforme")
    elif response == "4":
        print("Rotação no Sentido Horário")
        angle_degrees = get_float_input("Informe o ângulo de rotação (em graus): ")
        origin_x = get_float_input("Informe a coordenada x do ponto de origem da rotação: ")
        origin_y = get_float_input("Informe a coordenada y do ponto de origem da rotação: ")
        origin = (origin_x, origin_y)
        coordinates = rotate_clockwise(coordinates, angle_degrees, origin)
        plot_form(coordinates, "Forma após Rotação no Sentido Horário")
    elif response == "5":
        print("Rotação no Sentido Anti-Horário")
        angle_degrees = get_float_input("Informe o ângulo de rotação (em graus): ")
        origin_x = get_float_input("Informe a coordenada x do ponto de origem da rotação: ")
        origin_y = get_float_input("Informe a coordenada y do ponto de origem da rotação: ")
        origin = (origin_x, origin_y)
        coordinates = rotate_counterclockwise(coordinates, angle_degrees, origin)
        plot_form(coordinates, "Forma após Rotação no Sentido Anti-Horário")

    return coordinates


def main():
    forms = []
    i = 0

    canceled = False

    while not canceled:
        i += 1
        form_type = "Unknown"
        coordinates = []

        formType = input("Deseja gerar um quadrilátero ou um triângulo?")
        if formType.lower().startswith("tri"):
            coordinates = get_triangle()
            form_type = "Triangle"
        if formType.lower().startswith("quadr"):
            coordinates = get_quadrilateral()
            form_type = "Quadrilateral"
        
        response = ""

        if coordinates != []:
            forms.append([i, coordinates, form_type])
            
            response = input("Deseja transformar a forma geométrica? (s/n)")
            if response.lower() == 's':
                while not canceled:
                    new_coordinates = transform_form(coordinates)
                    i += 1
                    forms.append([i, new_coordinates, form_type])
                    
                    response = input("Deseja transformar novamente")
                    if response.lower() == "n":
                        canceled = True
        
        response = input("Deseja repetir? (s/n) ")
        if response.lower() == "n":
            canceled = True
        elif response.lower() == 's':
            canceled = False

if __name__ == "__main__":
    main()


