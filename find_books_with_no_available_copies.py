import pandas as pd


def find_books_with_no_available_copies(
    library_books: pd.DataFrame, borrowing_records: pd.DataFrame
) -> pd.DataFrame:
    """
    Finds all books that are currently borrowed (not returned) and have zero
    copies available in the library.

    Tables:
        library_books:
            - book_id (int): Unique identifier for the book.
            - title (str): Title of the book.
            - author (str): Author of the book.
            - genre (str): Genre of the book.
            - publication_year (int): Year the book was published.
            - total_copies (int): Total number of copies owned by the library.

        borrowing_records:
            - record_id (int): Unique identifier for the borrowing transaction.
            - book_id (int): The ID of the borrowed book.
            - borrower_name (str): Name of the borrower.
            - borrow_date (date): Date when the book was borrowed.
            - return_date (date): Date when the book was returned (NULL if not returned).

    A book is considered currently borrowed if it has at least one borrowing
    record with a NULL return_date. The function returns books that have all
    their copies currently borrowed (i.e., zero available in the library).

    The resulting DataFrame is ordered by current borrowers in descending
    order, and then by book title in ascending order.

    Args:
        library_books (pd.DataFrame): DataFrame of library books.
        borrowing_records (pd.DataFrame): DataFrame of borrowing records.

    Returns:
        pd.DataFrame: Books with zero available copies, sorted as specified.

    Example:
            Input:

            library_books table:

            +---------+------------------------+------------------+----------+------------------+--------------+
            | book_id | title                  | author           | genre    | publication_year | total_copies |
            +---------+------------------------+------------------+----------+------------------+--------------+
            | 1       | The Great Gatsby       | F. Scott         | Fiction  | 1925             | 3            |
            | 2       | To Kill a Mockingbird  | Harper Lee       | Fiction  | 1960             | 3            |
            | 3       | 1984                   | George Orwell    | Dystopian| 1949             | 1            |
            | 4       | Pride and Prejudice    | Jane Austen      | Romance  | 1813             | 2            |
            | 5       | The Catcher in the Rye | J.D. Salinger    | Fiction  | 1951             | 1            |
            | 6       | Brave New World        | Aldous Huxley    | Dystopian| 1932             | 4            |
            +---------+------------------------+------------------+----------+------------------+--------------+
            borrowing_records table:

            +-----------+---------+---------------+-------------+-------------+
            | record_id | book_id | borrower_name | borrow_date | return_date |
            +-----------+---------+---------------+-------------+-------------+
            | 1         | 1       | Alice Smith   | 2024-01-15  | NULL        |
            | 2         | 1       | Bob Johnson   | 2024-01-20  | NULL        |
            | 3         | 2       | Carol White   | 2024-01-10  | 2024-01-25  |
            | 4         | 3       | David Brown   | 2024-02-01  | NULL        |
            | 5         | 4       | Emma Wilson   | 2024-01-05  | NULL        |
            | 6         | 5       | Frank Davis   | 2024-01-18  | 2024-02-10  |
            | 7         | 1       | Grace Miller  | 2024-02-05  | NULL        |
            | 8         | 6       | Henry Taylor  | 2024-01-12  | NULL        |
            | 9         | 2       | Ivan Clark    | 2024-02-12  | NULL        |
            | 10        | 2       | Jane Adams    | 2024-02-15  | NULL        |
            +-----------+---------+---------------+-------------+-------------+
            Output:

            +---------+------------------+---------------+-----------+------------------+-------------------+
            | book_id | title            | author        | genre     | publication_year | current_borrowers |
            +---------+------------------+---------------+-----------+------------------+-------------------+
            | 1       | The Great Gatsby | F. Scott      | Fiction   | 1925             | 3                 |
            | 3       | 1984             | George Orwell | Dystopian | 1949             | 1                 |
            +---------+------------------+---------------+-----------+------------------+-------------------+

    Time Complexity: O(m + k), where m is the number of borrow records and k is the number of books.
    Space Complexity: O(k), for intermediate groupings and merge results.

    LeetCode: Beats 95.98% of submissions
    """
    books_grouped = borrowing_records[["book_id", "return_date"]].groupby("book_id")
    borrowed_books = (
        (books_grouped.size() - books_grouped["return_date"].count())
        .reset_index()
        .rename(columns={0: "current_borrowers"})
    )
    merged_df = library_books.merge(borrowed_books)
    return (
        merged_df[merged_df["total_copies"] == merged_df["current_borrowers"]]
        .drop("total_copies", axis=1)
        .sort_values(by=["current_borrowers", "title"], ascending=[False, True])
    )
