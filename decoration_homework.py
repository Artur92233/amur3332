from typing import Callable


def master(func: Callable) -> Callable:
    def subordinate(*args, **kwargs):
        # -----------------------------------------
        # before execution

        # -----------------------------------------

        result = func(*args, **kwargs)  # must be here!!!!!!!!!!!!!!!

        # -----------------------------------------
        # after execution

        if type(result) == int:
            result += 10
        # -----------------------------------------

        return result

    return subordinate  # no round brackets !!!!!!!!!!!!!


@master
def has_summ_int(number_first: float | int, number_second: float | int) -> float | int:
    summ = number_first + number_second
    return summ


result = has_summ_int(2.5, 3)
pass
