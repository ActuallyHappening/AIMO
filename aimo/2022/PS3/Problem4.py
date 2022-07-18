def is_abundant(n):
    fctr_sum = sum([fctr for fctr in range(1, n) if n % fctr == 0])
    return fctr_sum > n

print("999 abudnat: " + str(is_abundant(999)))

largest = 0
for i in range(1, 1001, 2):
  # print(i)
  if is_abundant(i) and i > largest:
    largest = i

print("PYTHON IS SO EASY: " + str(largest))