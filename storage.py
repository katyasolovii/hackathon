_storage = {}
_last_error = 0

ERRORS = {0: "",
          1: "Змінна вже є у пам'яті",
          2: "Змінна не існує",
          3: "Змінна невизначена"}


def add(variable):
    """
    Функція додає змінну у память.
    Якщо така змінна вже існує, то встановлює помилку
    :param variable: змінна
    :return: None
    """
    global _last_error                                                          
    if variable in _storage:
        _last_error = 1
        return
    else:
        _storage[variable] = None
        _last_error = 0
        return


def is_in(variable):
    """ 
    Функція перевіряє, чи є змінна у пам'яті.
    :param variable: змінна
    :return: булівське значенна (True, якщо є)
    """
    global _last_error
    _last_error = 0
    return variable in _storage.keys()


def get(variable):
    """ 
    Функція повертає значення змінної.
    Якщо така змінна не існує або невизначена (==None),
    то встановлює відповідну помилку
    :param variable: змінна
    :return: значення змінної
    """
    global _last_error
    if variable not in _storage.keys():
        _last_error = 2
        return
    x = _storage[variable]
    if x is None:
        _last_error = 3
        return
    _last_error = 0
    return x


def set(variable, value):
    """
    Функція встановлює значення змінної
    Якщо змінна не існує, повертає помилку
    :param variable: змінна
    :param value: нове значення
    :return: None
    """
    global _last_error
    if variable not in _storage.keys():
        _last_error = 2
        return
    _last_error = 0
    _storage[variable] = value
    return


def input_var(variable):
    """
    Функція здійснює введення з клавіатури та встановлення значення змінної
    Якщо змінна не існує, повертає помилку
    :param variable: змінна
    :return: None
    """
    global _last_error
    if variable not in _storage.keys():
        _last_error = 2
        return
    _last_error = 0
    _storage[variable] = float(input(f"Введіть значення ({variable}): "))
    return


def input_all():
    """
    Функція здійснює введення з клавіатури та встановлення значення
    усіх змінних з пам'яті
    :return: None
    """
    global _last_error
    _last_error = 0
    for el in _storage:
        _storage[el] = int(input(f"Введіть значення ({el}): "))
    return None


def clear():
    """
    Функція видаляє усі змінні з пам'яті.
    :return: None
    """
    global _storage, _last_error
    _last_error = 0
    _storage = {}
    return


def get_last_error():
    """
    Функція повертає код останньої помилки code
    Для виведення повідомлення треба взяти
    storage.ERRORS[code]

    :return: код останньої помилки
    """
    global _last_error
    return _last_error


if __name__ == "__main__":
    add("a")
    assert get_last_error() == 0
    add("a")
    assert get_last_error() == 1
    c = get("a")
    assert c == None and get_last_error() == 3
    c = get("b")
    assert c == None and get_last_error() == 2
    set("a", 1)
    assert get_last_error() == 0
    c = get("a")
    assert c == 1 and get_last_error() == 0
    set("b", 2)
    assert get_last_error() == 2
    add("x")
    assert get_last_error() == 0
    input_var("x")      # ввести значення x = 2
    assert get_last_error() == 0
    f = get("x")
    assert f == 2 and get_last_error() == 0
    clear()
    assert get_last_error() == 0
    add("a")
    assert get_last_error() == 0
    add("d")
    assert get_last_error() == 0
    input_all()  # ввести значення a = 3, d = 4
    assert get_last_error() == 0
    c = get("a")
    assert c == 3 and get_last_error() == 0
    f = get("d")
    assert f == 4 and get_last_error() == 0
    assert is_in("a")
    assert get_last_error() == 0

    assert not is_in("_asda") and get_last_error() == 0

    print("Success = True")
