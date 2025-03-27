import math

def calculate_product_for_sum1(c, j):
    return (((49 * c ** 2) ** 4) / 14 + j ** 18)

def calculate_product_for_sum2(c, j, i, z):
    return ((c + 21 + 99 * j ** 2) ** 2 + 6 * math.exp(4) * i + 21 * z)

def compute_sum1(b, a):
    sum1 = 0
    for j in range(1, a + 1):
        product = 1
        for c in range(1, b + 1):
            product *= calculate_product_for_sum1(c, j)
        sum1 += product
    return sum1

def compute_sum2(b, m, n, z):
    sum2 = 0
    for i in range(1, n + 1):
        temp_sum = 0
        for c in range(1, m + 1):
            product = 0
            for j in range(1, b + 1):
                product += calculate_product_for_sum2(c, j, i, z)
            temp_sum += product
        sum2 += temp_sum
    return sum2

def main(b, a, m, n, z):
    sum1 = compute_sum1(b, a)
    sum2 = compute_sum2(b, m, n, z)
    return sum1 - sum2

if __name__ == '__main__':
    print("Результат:", main(2, 2, 2, 2, 1))
