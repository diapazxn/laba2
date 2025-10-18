def to_dict_decorator(func):
    """
    Декоратор, який перетворює результат функції у словник.
    Якщо результат — не ітерабельний об’єкт, поміщає його у словник із ключем 'result'.
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        # Якщо результат уже словник просто повертається
        if isinstance(result, dict):
            return result

        # Результат список або кортеж, робиться словник із індексами
        elif isinstance(result, (list, tuple, set)):
            return {f"item_{i}": value for i, value in enumerate(result)}

        # Результат число,рядок
        else:
            return {"result": result}

    return wrapper
