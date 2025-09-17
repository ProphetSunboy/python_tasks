class FoodRatings:
    """
    FoodRatings System

    A class to manage food items, their cuisines, and ratings, supporting efficient
    rating updates and queries for the highest-rated food per cuisine.

    Features:
        - Modify the rating of a food item.
        - Retrieve the highest-rated food for a given cuisine (lexicographically smallest name in case of ties).

    Methods:
        __init__(foods: List[str], cuisines: List[str], ratings: List[int])
            Initializes the system with lists of food names, their corresponding cuisines, and initial ratings.

        changeRating(food: str, newRating: int) -> None
            Updates the rating of the specified food item.

        highestRated(cuisine: str) -> str
            Returns the name of the highest-rated food for the given cuisine.
            If multiple foods have the same highest rating, returns the lexicographically smallest name.

    Example:
        >>> foods = ["sushi", "pizza", "burger"]
        >>> cuisines = ["japanese", "italian", "american"]
        >>> ratings = [5, 7, 7]
        >>> fr = FoodRatings(foods, cuisines, ratings)
        >>> fr.highestRated("italian")
        'pizza'
        >>> fr.changeRating("sushi", 10)
        >>> fr.highestRated("japanese")
        'sushi'

    Time Complexity:
        - Initialization: O(n)
        - changeRating: O(1)
        - highestRated: O(m), where m is the number of foods in the queried cuisine
    """

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {}
        for i in range(len(foods)):
            self.foods[foods[i]] = ratings[i]

        self.cuisines = {}
        for i in range(len(cuisines)):
            self.cuisines[cuisines[i]] = self.cuisines.get(cuisines[i], []) + [foods[i]]

    def changeRating(self, food: str, newRating: int) -> None:
        self.foods[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        highest_rated = 0
        highest_c = ""
        for c in self.cuisines[cuisine]:
            if self.foods[c] > highest_rated:
                highest_rated = self.foods[c]
                highest_c = c
            elif self.foods[c] == highest_rated and c < highest_c:
                highest_c = c

        return highest_c


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
