import re

def total_salary(path):
    try:
        with open(path, "r", encoding='utf-8') as fh:
            lines = [el.strip() for el in fh.readlines()]
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return None, None
    except IOError:
        print(f"Помилка читання файлу за шляхом '{path}'.")
        return None, None

    try:
        salaries = [(re.search(r"\d+", el)).group() for el in lines]
        salaries = [int(salary) for salary in salaries]
    except AttributeError:
        print("Помилка в обробці рядків файлу.")
        return None, None

    sumary = sum(salaries)
    avg_salary = sumary // len(salaries) if salaries else 0

    return sumary, avg_salary


