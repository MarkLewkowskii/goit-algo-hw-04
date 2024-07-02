from pathlib import Path
from calculate_salary import total_salary
def main():
    path = Path("C:\My_repo\Home_works\goit-algo-hw-04\Task_1\salary_file.txt")
    total, average = total_salary(path)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()