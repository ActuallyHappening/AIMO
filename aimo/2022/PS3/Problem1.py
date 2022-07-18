def f(val):
  return [(i, int(val / i)) for i in range(1, int(val**0.5)+1) if val % i == 0]


def are_factors_ok(val):
  factors = f(val)
  for factor_pair in factors:
    if "0" not in str(int(factor_pair[0])) and "0" not in str(int(factor_pair[1])):
      return False
  return True

def main():
  for i in range(1, 10):
    j = 10**i
    if are_factors_ok(j):
      print(f"10^{i} or {j} works! factors are: {f(j)}")

if __name__ == "__main__":
  main()