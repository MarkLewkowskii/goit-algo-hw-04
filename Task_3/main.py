from structure_script import show_structure
from pathlib import Path

def main():
   path = Path(input("Введіть шлях(path):"))
   return(show_structure(path))



if __name__ == '__main__':
   main()