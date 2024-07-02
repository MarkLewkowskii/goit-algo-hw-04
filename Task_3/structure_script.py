from pathlib import Path
from colorama import Fore

def folders(some_path: Path, indent_char: str = '··', current_indent: str = '|') -> None:
    try:
        items = sorted(some_path.glob('*'))  # Sort items for consistent order
        for item in items:
            if item.is_file():
                print("|" + current_indent + f"{Fore.YELLOW}{item.name}{Fore.RESET}")
            elif item.is_dir():
                print("|" + current_indent + f"{Fore.BLUE}{item.name}{Fore.RESET}")
                folders(item, indent_char, current_indent + indent_char)  # Increase indentation for subdirectories
    except Exception as e:
        print(f"An error occurred while listing items: {e}")

def show_structure(path: Path, indent_char: str = '··') -> None:
    if path.exists():
        if path.is_dir():
            print(f"·{Fore.BLUE}{path.name}{Fore.RESET}")
            folders(path, indent_char, indent_char)  # Start with an initial indentation for child items
        else:
            print(f"·{Fore.YELLOW}{path.name}{Fore.RESET}")
    else:
        print(f"{path.absolute()} does not exist.")