from colorama import Fore


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return Fore.RED + str(e)
        except KeyError:
            return Fore.RED + "Not found."
        except IndexError:
            return Fore.RED + "Not enough arguments."
        except Exception as e:
            return Fore.RED + f"Error: {e}"
    return wrapper