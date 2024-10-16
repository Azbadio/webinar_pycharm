from fibonacci import fib
from duration import duration


@duration
def main_simple(n: int) -> int:
    return fib(n)


if __name__ == "__main__":
    n = 35
    print(main_simple(n))
