ALL_COMAND = ["hello","add" ,"change" ,"phone" ,"show all" ,"good bye" ,"close" ,"exit"]
EXIT_COMAND = ALL_COMAND[5:]
data = {}

def input_error(func):
    def inner(*x, **y):
        try:
            result = func(*x, **y)
            return result
        except KeyError as e:
            return str(e.args[0])
        except ValueError as e:
            return str(e.args[0])
        except IndexError as e:
            return str(e.args[0])
    return inner


def hello():
    return "How can I help you?"


@input_error
def show_all():
    global data

    if data == {}:
        raise IndexError("the contact list is empty")
    else:
        result = ''
        for name, contact in data.items():
            result += f"{name}: {contact}\n"
        return result[:-1]
        

@input_error
def change(user_input_split):
    global data

    if data == {}:
        raise IndexError("the contact list is empty")
    if len(user_input_split) != 3:
        raise ValueError(f"you have entered the wrong number of values {len(user_input_split)} and 3rd value is required")
    else:
        if user_input_split[1] in data:
            data[user_input_split[1]] = user_input_split[2]
            return f"Phone number for {user_input_split[1]} has been changed to {user_input_split[2]}."
        else:
            raise KeyError("this name does not exist in the contact list")


@input_error
def phone(user_input_split):
    global data

    if data == {}:
        raise IndexError("the contact list is empty")
    if len(user_input_split) != 2:
        raise ValueError(f"you have entered the wrong number of {len(user_input_split)} values and a 2nd value is required")
    else:
        if user_input_split[1] in data:
            return f"Phone number: {data[user_input_split[1]]}."
        else:
            raise KeyError("this name does not exist in the contact list")


@input_error
def add(user_input_split):
    global data

    if data is None:
        data = {}
    if len(user_input_split) == 3:
        name = user_input_split[1]
        contact = user_input_split[2]
        if name not in data:
            data[name] = contact
            return f"name: {name}, and contact: {data[name]} add in contact list"
        else:
            raise KeyError(f"this name {name} already exists in the contact list")
    else:
        raise ValueError(f"you have entered the wrong number of values {len(user_input_split)} and 3rd value is required")


if __name__=="__main__":
    while True:
        try:
            user_input = str(input('Enter the command: ')).lower()
            user_input_split = user_input.split()
        except Exception as e:
            print('Error', str(e))
        
        if user_input == 'hello':
                print(hello())

        if user_input == 'show all':
                print(show_all())
                        
        if user_input_split[0] == "add":
            print(add(user_input_split))

        if user_input_split[0] == "change":
            print(change(user_input_split))

        if user_input_split[0] == "phone":
            print(phone(user_input_split))

        if user_input in EXIT_COMAND:
                print("Good bye!")
                break
        
        if user_input_split[0] not in ALL_COMAND and user_input not in ALL_COMAND:
            print(f"a list of commands that can be used:\n{', '.join(ALL_COMAND[:-2])} or {ALL_COMAND[-1]}")