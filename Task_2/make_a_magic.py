
def get_cats_info(path):
    future_answer=[]
    keys = ["id", "name", "age"]
    try:
        with open(path, "r", encoding='utf-8') as fh:
            for line in fh:
                line = line.strip()
                values = line.split(",")
                eachcat_dict = {keys[i]: values[i] for i in range(len(keys))}
                future_answer.append(eachcat_dict)
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return []
    except IOError:
        print(f"Помилка читання файлу за шляхом '{path}'.")
        return []

    return future_answer