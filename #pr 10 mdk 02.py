import cmath
import random

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Все значения x являются решениями (бесконечное количество решений)"
            else:
                return "Нет решений"
        else:
            return f"Линейное уравнение, x = {-c/b}"
    else:
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
            root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
            return (root1.real, root2.real)
        elif discriminant == 0:
            root = -b / (2*a)
            return (root, root)
        else:
            root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
            root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
            return (root1, root2)

def generate_random_coefficients():
    a = random.uniform(-10, 10)
    b = random.uniform(-10, 10)
    c = random.uniform(-10, 10)
    return a, b, c

def format_result(result):
    if isinstance(result, str):
        return result
    elif isinstance(result, tuple):
        return f"X1={result[0]:.2f} X2={result[1]:.2f}"
    else:
        return str(result)

def run_tests(num_tests=10):
    print("Номер теста\tA\tB\tC\tОжидаемый результат\tЧто проверяется")
    for i in range(1, num_tests + 1):
        a, b, c = generate_random_coefficients()
        result = solve_quadratic(a, b, c)
        result_str = format_result(result)
        
        # Determine what is being checked based on coefficients and result
        if a == 0 and b == 0:
            description = "Неразрешимое уравнение"
        elif a == 0:
            description = "Неквадратное уравнение"
        elif isinstance(result, tuple):
            if all(isinstance(x, complex) for x in result):
                description = "Случай комплексных корней"
            else:
                description = "Случай вещественных корней"
        else:
            description = "Неразрешимое уравнение"
        
        print(f"{i}\t{a:.2f}\t{b:.2f}\t{c:.2f}\t{result_str}\t{description}")

run_tests()
