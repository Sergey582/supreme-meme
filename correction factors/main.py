from constants import path_to_dir
from fetcher import get_all_data
from calculate import calculate_T_b, calculate_T_n


def main():
    T_b_coefficients = []
    T_n_coefficients = []
    mas_info = get_all_data(path_to_dir)
    for column_data in mas_info:
        T_n = calculate_T_n(*column_data)
        T_b = calculate_T_b(T_n)
        T_b_coefficients.append(T_b)
        T_n_coefficients.append(T_n)
    results = []
    print("-"*100)
    print("Net tariff: ")
    print(T_n_coefficients)
    print("-"*100)
    print("Gross tariff: ")
    print(T_b_coefficients)
    print("-"*100)
    for index in range(len(T_b_coefficients) - 1):
        results.append(T_b_coefficients[index] / T_b_coefficients[index + 1])
    print("Correction coefficients:")
    print(results)
    print("-"*100)


if __name__ == '__main__':
    main()
