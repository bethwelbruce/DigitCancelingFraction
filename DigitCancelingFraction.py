n, d = map(int, input().split())

num_sum = 0
den_sum = 0

for num in range(10**(n-1), 10**n):
    for den in range(num+1, 10**n):
        num_str = str(num)
        den_str = str(den)
        common_digits = set(num_str) & set(den_str)
        if len(common_digits) == d and common_digits != {'0'}:
            reduced_num = int(num_str.replace(list(common_digits)[0], '', d))
            reduced_den = int(den_str.replace(list(common_digits)[0], '', d))
            if reduced_den != 0 and num/den == reduced_num/reduced_den:
                num_sum += num
                den_sum += den

print(num_sum, den_sum)