from pathlib import Path
from make_a_magic import get_cats_info

def main():
    cats_path = Path("Task_2\cat_info.txt")
    cats_info = get_cats_info(cats_path)
    print(cats_info)


if __name__ == "__main__":
    main()