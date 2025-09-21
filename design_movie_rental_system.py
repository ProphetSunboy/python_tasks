import bisect
from typing import List, Tuple
from collections import defaultdict


class MovieRentingSystem:
    """
    MovieRentingSystem manages a movie rental company with n shops, supporting searching,
    renting, returning, and reporting of movies.

    Each movie is represented in the input as entries[i] = [shop[i], movie[i], price[i]],
    indicating that shop[i] has a copy of movie[i] available for rent at price[i].
    Each shop carries at most one copy of a given movie.

    Supported operations:

    - search(movie: int) -> List[int]:
        Returns up to 5 shop indices with an unrented copy of the specified movie,
        sorted by lowest price, then by shop index.
        Returns an empty list if no unrented copy is available.

    - rent(shop: int, movie: int) -> None:
        Rents an unrented copy of the specified movie from the given shop.

    - drop(shop: int, movie: int) -> None:
        Returns a previously rented movie to the specified shop.

    - report() -> List[List[int]]:
        Returns up to 5 currently rented movies as [shop, movie] pairs, sorted by
        lowest price, then by shop index, then by movie index.
        Returns an empty list if no movies are currently rented.
    """

    def __init__(self, n: int, entries: List[List[int]]):

        self.price_map = {}
        self.available = defaultdict(list)
        self.rented = []

        self.in_rented = {}

        for shop, movie, price in entries:
            self.price_map[(shop, movie)] = price
            bisect.insort(self.available[movie], (price, shop))

    def search(self, movie: int) -> List[int]:
        res = []
        arr = self.available.get(movie, [])
        for price, shop in arr[:5]:
            res.append(shop)
        return res

    def rent(self, shop: int, movie: int) -> None:

        price = self.price_map[(shop, movie)]

        arr = self.available[movie]
        idx = bisect.bisect_left(arr, (price, shop))

        if idx < len(arr) and arr[idx] == (price, shop):
            arr.pop(idx)
        else:
            for j in range(len(arr)):
                if arr[j] == (price, shop):
                    arr.pop(j)
                    break

        tup = (price, shop, movie)
        bisect.insort(self.rented, tup)
        self.in_rented[(shop, movie)] = tup

    def drop(self, shop: int, movie: int) -> None:
        price = self.price_map[(shop, movie)]
        tup = (price, shop, movie)

        existing = self.in_rented.get((shop, movie))
        if existing is not None:

            idx = bisect.bisect_left(self.rented, existing)

            if idx < len(self.rented) and self.rented[idx] == existing:
                self.rented.pop(idx)
            else:
                for j in range(len(self.rented)):
                    if self.rented[j] == existing:
                        self.rented.pop(j)
                        break
            del self.in_rented[(shop, movie)]

        bisect.insort(self.available[movie], (price, shop))

    def report(self) -> List[List[int]]:
        res = []
        for price, shop, movie in self.rented[:5]:
            res.append([shop, movie])
        return res
