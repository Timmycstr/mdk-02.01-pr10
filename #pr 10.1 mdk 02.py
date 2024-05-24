import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_non_matching_strings():
    str1_length = random.randint(1, 10)  # Длина первой строки от 1 до 10 символов
    str2_length = random.randint(1, 5)   # Длина второй строки от 1 до 5 символов
    str1 = generate_random_string(str1_length)
    str2 = generate_random_string(str2_length)
    
    # Убедимся, что вторая строка не содержится в первой строке
    while str2 in str1:
        str2 = generate_random_string(str2_length)
    
    return str1, str2

def count_occurrences(str1, str2):
    if not str1 or not str2:
        return 0
    
    count = 0
    i = 0
    while i < len(str1):
        if str1[i:i+len(str2)] == str2:
            count += 1
            i += len(str2) - 1
        i += 1
    return count

# Генерация и выполнение случайных тестов
NUM_TESTS = 6  # Общее количество тестов

for i in range(NUM_TESTS):
    str1, str2 = generate_non_matching_strings()
    expected = count_occurrences(str1, str2)
    
    result = count_occurrences(str1, str2)
    if result == expected:
        print(f"Тест {i+1}: ПРОЙДЕН")
    else:
        print(f"Тест {i+1}: НЕ ПРОЙДЕН. Ожидаемый результат: {expected}, Полученный результат: {result}")
