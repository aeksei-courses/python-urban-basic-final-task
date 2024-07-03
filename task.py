import csv
import logging
import math
from collections import defaultdict, namedtuple

logging.basicConfig(level=logging.INFO)


FloorBoundaries = namedtuple("FloorBoundaries", ["lowest", "highest"])
HOUSE_CLASSIFICATION_BY_FLOORS = {
    "Малоэтажный": FloorBoundaries(1, 5),
    "Среднеэтажный": FloorBoundaries(6, 16),
    "Многоэтажный": FloorBoundaries(17, math.inf),
}

NON_INT_FLOORS_ERROR_MESSAGE = "Количество этажей должно быть целым числом."
INCORRECT_FLOORS_NUMBER_ERROR_MESSAGE = "Количество этажей должно быть больше 0."
INCORRECT_FLOORS_BORDERS_ERROR_MESSAGE = "Неконсистентные границы классификации."


def read_file(filename: str) -> list[dict]:
    """Читает данные из CSV файла и преобразует их в список словарей.

    :param filename: Название файла, содержащего данные.
    :return: Список словарей с данными о домах.
    """
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        return [
            {
                "area_id": house["area_id"],
                "house_address": house["house_address"],
                "floor_count": int(house["floor_count"]),
                "heating_house_type": house["heating_house_type"],
                "heating_value": float(house["heating_value"]),
                "area_residential": float(house["area_residential"]),
                "population": int(house["population"]),
            }
            for house in csv_reader
        ]


def classify_house(floor_count: int) -> str:
    """Классифицирует дом на основе количества этажей.

    Проверяет, является ли количество этажей целым числом и положительным значением.
    Возвращает категорию дома в зависимости от количества этажей.

    :param floor_count: Количество этажей в доме.
    :return: Категория дома в виде строки:
    "Малоэтажный", "Среднеэтажный" или "Многоэтажный".
    """
    if not isinstance(floor_count, int):
        raise TypeError(NON_INT_FLOORS_ERROR_MESSAGE)

    if floor_count <= 0:
        raise ValueError(INCORRECT_FLOORS_NUMBER_ERROR_MESSAGE)

    for _type, boundaries in HOUSE_CLASSIFICATION_BY_FLOORS.items():
        if boundaries.lowest <= floor_count <= boundaries.highest:
            return _type

    raise ValueError(INCORRECT_FLOORS_BORDERS_ERROR_MESSAGE)


def get_classify_houses(houses: list[dict]) -> list[str]:
    """Классифицирует дома на основе количества этажей.

    :param houses: Список словарей с данными о домах.
    :return: Список категорий домов.
    """
    return [classify_house(house["floor_count"]) for house in houses]


def get_count_house_categories(categories: list[str]) -> dict[str, int]:
    """
    Подсчитывает количество домов в каждой категории.

    :param categories: Список категорий домов.
    :return: Словарь с количеством домов в каждой категории.
    """
    statistics = defaultdict(int)
    for category in categories:
        statistics[category] += 1

    return dict(statistics)


def min_area_residential(
    houses: list[dict],
) -> str:  # this function name should be a verb
    """Находит адрес дома с наименьшей жилой площадью на одного жильца.

    :param houses: Список словарей с данными о домах.
    :return: Адрес дома с наименьшим средним количеством квадратных
    метров жилой площади на одного жильца.
    """
    min_area_house = houses[0]
    min_area = min_area_house["area_residential"] / min_area_house["population"]
    for house in houses:
        residential_area = house["area_residential"] / house["population"]
        if residential_area < min_area:
            min_area_house = house

    return min_area_house["house_address"]


if __name__ == "__main__":
    houses = read_file("housing_data.csv")

    house_categories = get_classify_houses(houses)
    house_categories_statistics = get_count_house_categories(house_categories)

    min_residential_area_house = min_area_residential(houses)

    logging.info(house_categories_statistics)
    logging.info(min_residential_area_house)
