
import subprocess
import os


def run_test(test_name, input_data, expected_total=None):
    # Записываем входные данные
    with open("in.txt", "w") as f:
        f.write(input_data)

    # Запускаем тестируемую программу
    result = subprocess.run(
        ["python", "solution.py"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"{test_name}: ОШИБКА")
        print(result.stderr)
        return

    # Читаем результат
    with open("out.txt", "r") as f:
        output = f.read().strip().splitlines()

    # Проверяем количество строк
    n = int(input_data.split()[0])

    if len(output) != n + 1:
        print(f"{test_name}: ОШИБКА")
        print("Неверное количество строк")
        return

    # Проверяем вес дерева
    total = int(output[-1])

    if expected_total is not None and total != expected_total:
        print(f"{test_name}: ОШИБКА")
        print(f"Ожидалось: {expected_total}")
        print(f"Получено: {total}")
        return

    print(f"{test_name}: OK")
    print("Результат:")
    print("\n".join(output))
    print()


# Тест 1: одна вершина
run_test(
    "Тест 1",
    """1
0""",
    0
)

# Тест 2: две вершины
run_test(
    "Тест 2",
    """2
0 5
5 0""",
    5
)

# Тест 3: три вершины
run_test(
    "Тест 3",
    """3
0 1 3
1 0 2
3 2 0""",
    3
)

# Тест 4: четыре вершины
run_test(
    "Тест 4",
    """4
0 1 4 3
1 0 2 5
4 2 0 6
3 5 6 0""",
    6
)

# Тест 5: все рёбра имеют одинаковый вес
run_test(
    "Тест 5",
    """3
0 2 2
2 0 2
2 2 0""",
    4
)
