class Bank:
    """
    Bank class that automates transactions for a bank with multiple accounts.

    Each account is numbered from 1 to n. The initial balances are provided in a 0-indexed list `balance`,
    where the (i+1)th account has an initial balance of balance[i].

    Supported transactions:
        - Transfer: Move funds from one account to another.
        - Deposit: Add funds to a specific account.
        - Withdraw: Remove funds from a specific account.

    Transaction validity:
        - Account numbers must be between 1 and n (inclusive).
        - Withdrawal or transfer amounts cannot exceed the source account's balance.

    Methods
    -------
    __init__(balance: List[int]):
        Initialize the bank with a list of initial balances.

    transfer(account1: int, account2: int, money: int) -> bool:
        Transfer `money` from `account1` to `account2`.
        Returns True if successful, False otherwise.

    deposit(account: int, money: int) -> bool:
        Deposit `money` into `account`.
        Returns True if successful, False otherwise.

    withdraw(account: int, money: int) -> bool:
        Withdraw `money` from `account`.
        Returns True if successful, False otherwise.

    LeetCode: Beats 97.41% of submissions
    """

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            account1 <= len(self.balance)
            and account2 <= len(self.balance)
            and self.balance[account1 - 1] >= money
        ):
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money

            return True

        return False

    def deposit(self, account: int, money: int) -> bool:
        if account <= len(self.balance):
            self.balance[account - 1] += money

            return True

        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account <= len(self.balance) and self.balance[account - 1] >= money:
            self.balance[account - 1] -= money

            return True

        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
