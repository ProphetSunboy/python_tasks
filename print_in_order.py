class Foo:
    """
    Foo ensures the methods first(), second(), and third() are executed in order,
    even when called from different threads.

    Usage:
        - Thread A calls first()
        - Thread B calls second()
        - Thread C calls third()
        All threads may start in any order, but 'first' must print before 'second', and 'second' before 'third'.

    Synchronization Mechanism:
        threading.Event objects are used to signal task completion and enforce order.

    Example:
        foo = Foo()
        t1 = Thread(target=foo.first, args=(printFirst,))
        t2 = Thread(target=foo.second, args=(printSecond,))
        t3 = Thread(target=foo.third, args=(printThird,))
        t2.start(); t3.start(); t1.start();

        Output: firstsecondthird

    This class helps solve concurrency problems where thread execution order must be guaranteed.

    LeetCode: Beats 90.61% of submissions
    """

    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst: "Callable[[], None]") -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_done.set()

    def second(self, printSecond: "Callable[[], None]") -> None:

        # printSecond() outputs "second". Do not change or remove this line.
        self.first_done.wait()
        printSecond()
        self.second_done.set()

    def third(self, printThird: "Callable[[], None]") -> None:

        # printThird() outputs "third". Do not change or remove this line.
        self.second_done.wait()
        printThird()
