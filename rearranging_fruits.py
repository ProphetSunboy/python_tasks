from collections import Counter


def load_numbers_from_file(filename):
    """
    Загружает список чисел из файла.

    Аргументы:
        filename (str): Имя файла.

    Возвращает:
        list: Список чисел, или None, если произошла ошибка.
    """
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            numbers = []
            for line in lines:
                try:
                    numbers += map(int, line.rstrip("\n").split(", "))
                except ValueError:
                    print(
                        f"Ошибка: Невозможно преобразовать строку '{line.strip()}' в число."
                    )
                    return None
            return numbers
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        """
        Calculates the minimum cost to make two fruit baskets equal by swapping fruits.

        You are given two lists, basket1 and basket2, each containing n integers representing the cost of fruits in each basket.
        You can swap any fruit from basket1 with any fruit from basket2 any number of times.
        The cost of each swap is min(basket1[i], basket2[j]) for the swapped fruits.

        Two baskets are considered equal if, after sorting, their contents are identical.

        Args:
            basket1 (list[int]): The list of fruit costs in the first basket.
            basket2 (list[int]): The list of fruit costs in the second basket.

        Returns:
            int: The minimum total cost to make both baskets equal, or -1 if it is impossible.

        Example:
            >>> minCost([4, 2, 2, 2], [1, 4, 1, 2])
            1

        Time complexity: O(n log n), where n is the length of the baskets.
        Space complexity: O(n).
        """
        c1 = Counter(basket1)
        c2 = Counter(basket2)
        min_cost = 0
        min_fruit_cost = min(min(basket1), min(basket2))

        c3 = c1 + c2

        for freq in c3.values():
            if freq % 2:
                return -1

        b1_diff = sorted(c1 - c2, reverse=True)
        b2_diff = sorted(c2 - c1)
        i, j = 0, 0

        while c1 != c2:
            diff_j = (c2[b2_diff[j]] - c1[b2_diff[j]]) // 2
            diff_i = (c1[b1_diff[i]] - c2[b1_diff[i]]) // 2

            min_diff = min(diff_j, diff_i)
            c2[b1_diff[i]] += min_diff
            c1[b1_diff[i]] -= min_diff
            c2[b2_diff[j]] -= min_diff
            c1[b2_diff[j]] += min_diff
            if min_fruit_cost * 2 < min(b1_diff[i], b2_diff[j]):
                min_cost += min_fruit_cost * 2 * min_diff
            else:
                min_cost += min(b1_diff[i], b2_diff[j]) * min_diff

            if c1[b2_diff[j]] != c2[b2_diff[j]]:
                i += 1
            elif c1[b1_diff[i]] != c2[b1_diff[i]]:
                j += 1
            else:
                i += 1
                j += 1

        return min_cost
