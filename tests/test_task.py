import unittest


class TestBaseCase(unittest.TestCase):
    def test_min_area_residential(self):
        try:
            from task import min_area_residential
        except ImportError:
            raise AssertionError(
                'Проверьте, что объявлена функция `min_area_residential`'
            )

        houses = [
            {
                "house_address": "house_address_1",
                "area_residential": 10,
                "population": 100
            },
            {
                "house_address": "house_address_2",
                "area_residential": 5,
                "population": 100
            },
            {
                "house_address": "house_address_3",
                "area_residential": 20,
                "population": 100
            },
        ]
        expected_result = "house_address_2"
        actual_result = min_area_residential(houses)

        assert isinstance(actual_result, str), (
            "Убедитесь, что функция `min_area_residential` возвращает нужный тип данных."
        )

        assert actual_result == expected_result, (
            "Убедитесь, что функция `min_area_residential` верно находит адрес дома "
            "с минимальным средним количеством квадратным метров жилой площади на одного жильца."
        )

    def test_classify_house(self):
        try:
            from task import classify_house
        except ImportError:
            raise AssertionError(
                'Проверьте, что объявлена функция `classify_house`'
            )

        params = [
            (1, "Малоэтажный"),
            (5, "Малоэтажный"),
            (6, "Среднеэтажный"),
            (16, "Среднеэтажный"),
            (17, "Многоэтажный"),
        ]
        for floor, floot_type in params:
            with self.subTest(floor=floor, floot_type=floot_type):
                actual_result = classify_house(floor)

                assert isinstance(actual_result, str), (
                    "Убедитесь, что функция `classify_house` возвращает нужный тип данных."
                )

                expected_result = floot_type
                assert actual_result == expected_result, (
                    "Убедитесь, что функция `classify_house` верно классифицирует дом по количеству этажей в нём."
                )

    def test_invalid_type(self):
        try:
            from task import classify_house
        except ImportError:
            raise AssertionError(
                'Проверьте, что объявлена функция `classify_house`'
            )

        invalid_values = [1.5, "2", [], {}]

        for value in invalid_values:
            with self.subTest(value=value):
                with self.assertRaises(TypeError) as context:
                    classify_house(value)

                assert str(context.exception), "Ожидалось исключение `TypeError` с не пустым сообщением."

    def test_invalid_value(self):
        try:
            from task import classify_house
        except ImportError:
            raise AssertionError(
                'Проверьте, что объявлена функция `classify_house`'
            )

        invalid_values = [0, -5]

        for value in invalid_values:
            with self.subTest(value=value):
                with self.assertRaises(ValueError) as context:
                    classify_house(value)

                assert str(context.exception), "Ожидалось исключение `ValueError` с не пустым сообщением."

    def test_get_classify_houses(self):
        try:
            from task import get_classify_houses
        except ImportError:
            raise AssertionError(
                'Проверьте, что объявлена функция `get_classify_houses`'
            )
        test_cases = [
            ([
                 {"floor_count": 1},
                 {"floor_count": 3},
                 {"floor_count": 5},
                 {"floor_count": 10},
             ], ["Малоэтажный", "Малоэтажный", "Малоэтажный", "Среднеэтажный"]),
            ([], []),
            ([
                 {"floor_count": 2},
                 {"floor_count": 8},
                 {"floor_count": 12},
                 {"floor_count": 20},
             ], ["Малоэтажный", "Среднеэтажный", "Среднеэтажный", "Многоэтажный"]),
            ([
                 {"floor_count": 1},
                 {"floor_count": 1},
                 {"floor_count": 1},
             ], ["Малоэтажный", "Малоэтажный", "Малоэтажный"]),
        ]

        for houses, expected_result in test_cases:
            with self.subTest(houses=houses):
                actual_result = get_classify_houses(houses)

                assert isinstance(actual_result, list), (
                    "Убедитесь, что функция `classify_house` возвращает нужный тип данных."
                )

                assert actual_result == expected_result, (
                    f"Убедитесь, что функция `get_classify_houses` корректно классифицирует дома "
                    f"на основе количества этажей."
                )

    def test_get_count_house_categories(self):
        try:
            from task import get_count_house_categories
        except ImportError:
            raise AssertionError(
                'Проверьте, что объявлена функция `get_count_house_categories`'
            )

        test_cases = [
            (["A", "B", "A", "C", "B", "A"], {"A": 3, "B": 2, "C": 1}),
            ([], {}),
            (["A", "A", "A", "A"], {"A": 4}),
            (["A", "B", "C", "D"], {"A": 1, "B": 1, "C": 1, "D": 1}),
            (["A", "B", "C", "A", "D", "E", "C", "B", "E"], {"A": 2, "B": 2, "C": 2, "D": 1, "E": 2})
        ]

        for categories, expected_result in test_cases:
            with self.subTest(categories=categories):
                actual_result = get_count_house_categories(categories)
                assert isinstance(actual_result, dict), (
                    "Убедитесь, что функция `get_count_house_categories` возвращает нужный тип данных."
                )
                assert actual_result == expected_result, (
                    f"Убедитесь, что функция `get_count_house_categories` корректно подсчитывает количество домов "
                    f"в каждой категории."
                )
