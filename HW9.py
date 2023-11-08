def input_error(func):
    def inner(n):
        try:
            return func(n)
        except KeyError:
            return f"{RED}Contact not found.{RESET}"
        except ValueError:
            return f"{RED}Enter user name and phone number separated by space.{RESET}"
        except IndexError:
            return f"{RED}Enter a valid command.{RESET}"
    return inner


def hello_c() -> str:
    return f"{BLUE}How can I help you?{RESET}"


@input_error
def add_c(input_command: str) -> str:  # Додає в словник
    _, name, phone = input_command.split(" ", maxsplit=2)
    name = name.capitalize()
    PHONE_DIRECTORY[name] = phone
    return f"{GREEN}Contact {name} with phone number {phone} has been added.{RESET}"


@input_error
def change_c(input_command: str) -> str:  # Замінює дані в словнику
    _, name, phone = input_command.split(" ", maxsplit=2)
    name = name.capitalize()
    _ = PHONE_DIRECTORY[name]
    PHONE_DIRECTORY[name] = phone
    return f"{GREEN}Phone number for {name} has been updated to {phone}.{RESET}"


@input_error
def phone_c(input_command: str) -> str:  # Повертає номер по імені
    _, name = input_command.split(" ", maxsplit=1)
    name = name.capitalize()
    return f"{GREEN}The phone number for {name} is {PHONE_DIRECTORY[name]}.{RESET}"


def show_all_c() -> str:  # Виводить всі збережені контакти
    if not PHONE_DIRECTORY:
        return f"{RED}The phone directory is empty.{RESET}"
    else:
        all_contacts = f"{GREEN}Phone Directory:\n{RESET}"
        count = 0
    for name, phone in PHONE_DIRECTORY.items():
        count += 1
        all_contacts += f"{GREEN}{count}| {name} {phone}\n{RESET}"
    return all_contacts


RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = "\033[0m"

PHONE_DIRECTORY = {}

COMMAND_DICT = {
    'hello': hello_c,
    'add': add_c,
    'change': change_c,
    'phone': phone_c,
    'show all': show_all_c,
}


@input_error
def get_handler(input_command: str) -> list:
    if input_command.startswith('show all'):
        return COMMAND_DICT['show all']()
    if input_command.startswith('hello'):
        return COMMAND_DICT['hello']()
    command = input_command.split(" ")
    _ = command[1]
    return COMMAND_DICT[command[0]](input_command)


def main():
    while True:
        input_command = input(
            f"{BLUE}I'm listening>>> {RESET}").strip().lower()
        if input_command == "good bye" or input_command == "close" or input_command == "exit" or input_command == '.':
            print(f"{BLUE}Good bye!{RESET}")
            break
        elif input_command.startswith(('hello', 'add', 'change', 'phone', 'show all')):
            print(get_handler(input_command))
        else:
            print(f"{BLUE}I don't understand. Try again.{RESET}")


if __name__ == '__main__':
    main()
