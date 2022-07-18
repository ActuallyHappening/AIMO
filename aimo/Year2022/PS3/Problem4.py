def is_abundant(n):
    fctr_sum = sum([fctr for fctr in range(1, n) if n % fctr == 0])
    return fctr_sum > n

# print("999 abudnat: " + str(is_abundant(999)))


def main():
  largest = 0
  for i in range(1, 1001, 2):
    # print(i)
    if is_abundant(i) and i > largest:
      largest = i
  print(f"Answer (Largest): {largest}")


if __name__ == "__main__":
  main()