from decorator import to_dict_decorator

@to_dict_decorator
def get_numbers():
    return [10, 20, 30]

@to_dict_decorator
def get_name():
    return "Ivan"

@to_dict_decorator
def get_user_info():
    return {"name": "Ivan", "age": 17}

@to_dict_decorator
def get_tuple():
    return (1, 2, 3, 4)

if __name__ == "__main__":
    print("Список", get_numbers())
    print("Рядок", get_name())
    print("Словник", get_user_info())
    print("Кортеж", get_tuple())
