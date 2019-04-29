digits = '73167176531330624919225119674426574742355349194934'
k = 6

n = len(digits)
max_product = 0

for i in range(n - k + 1):
    window = digits[i:i+k]
    product = 1
    for value in window:
        product *= int(value)
    if product > max_product:
        max_product = product

max_product
