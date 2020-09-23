from constants import (n,
                       a_y,
                       f,
                       )


def calculate_T_n(N: int, sum_insured: float, M: int, payout_amount: float) -> float:
    """
    :param N:Contracts concluded
    :param M:Number of payments
    :return:net tariff
    """
    q = M / N
    S = sum_insured / N
    S_b = payout_amount / M
    T_o = (S_b / S) * q
    T_p = 1.2 * T_o * a_y * ((1 - q) / (n * q)) ** 0.5
    T_n = T_o + T_p
    return T_n


def calculate_T_b(T_n: float) -> float:
    """
    :param T_n: net tariff
    :return:Gross tariff
    """
    T_b = (T_n * 100) / (100 - f)
    return T_b
