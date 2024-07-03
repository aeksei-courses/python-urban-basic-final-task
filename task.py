import csv


def read_file(filename: str) -> list[dict]:
    """Читает данные из CSV файла и преобразует их в список словарей.

    :param filename: Название файла, содержащего данные.
    :return: Список словарей с данными о домах.
    """
    houses_list = []
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["floor_count"] = int(row["floor_count"])
            row["population"] = int(row["population"])
            row["heating_value"] = float(row["heating_value"])
            row["area_residential"] = float(row["area_residential"])
            houses_list.append(row)
    return houses_list


def classify_house(floor_count: int) -> str:
    """Классифицирует дом на основе количества этажей.

    Проверяет, является ли количество этажей целым числом и положительным значением.
    Возвращает категорию дома в зависимости от количества этажей.

    :param floor_count: Количество этажей в доме.
    :return: Категория дома в виде строки: "Малоэтажный", "Среднеэтажный" или "Многоэтажный".
    """
    classification = None
    min_floor_count = 0
    start_maloetaznyi = 1
    end_maloetaznyi = 5
    start_sredneetaznyi = 6
    end_sredneetaznyi = 16
    errortype = "Количество этажей должно быть целым числом"
    errorvalue = "Количество этажей не может быть отрицательным"
    if not isinstance(floor_count, int):
        raise TypeError(errortype)
    if floor_count < min_floor_count:
        raise ValueError(errorvalue)
    if start_maloetaznyi <= floor_count <= end_maloetaznyi:
        classification = "Малоэтажный"
    elif start_sredneetaznyi <= floor_count <= end_sredneetaznyi:
        classification = "Среднеэтажный"
    elif floor_count > end_sredneetaznyi:
        classification = "Многоэтажный"
    return classification


def get_classify_houses(houses: list[dict]) -> list[str]:
    """Классифицирует дома на основе количества этажей.

    :param houses: Список словарей с данными о домах.
    :return: Список категорий домов.
    """
    return [classify_house(house["floor_count"]) for house in houses]


def get_count_house_categories(categories: list[str]) -> dict[str, int]:
    """Подсчитывает количество домов в каждой категории.

    :param categories: Список категорий домов.
    :return: Словарь с количеством домов в каждой категории.
    """
    categories_set = set(categories)
    categories_count = {}
    for category in categories_set:
        categories_count[category] = categories.count(category)
    return categories_count


def min_area_residential(houses: list[dict]) -> str:
    """Находит адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.

    :param houses: Список словарей с данными о домах.
    :return: Адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.
    """
    select_list = houses[0]  # Выбираем первую запись в качестве референса
    min_floor_area = select_list["area_residential"] / select_list["population"]  # Получаем её площадь на жильца
    address = select_list["house_address"]  # Получаем её адрес
    for house in houses:
        if house["area_residential"] / house["population"] < min_floor_area:
            min_floor_area = house["area_residential"] / house["population"]
            address = house["house_address"]
    return address
