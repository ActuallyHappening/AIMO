def find_hypotenuse(a, b):
    """Return the hypotenuse of a right triangle"""
    return (a**2 + b**2)**0.5

def is_one_side_length_equal_to_hypotenuse_digits_reversed(a, hypot):
    """Return True if one side is equal to the hypotenuse digits reversed"""
    return str(a) == str(int(hypot))[::-1]

is_one_side = is_one_side_length_equal_to_hypotenuse_digits_reversed

def main():
  for ab in range(10, 100):
    for bc in range(10, 100):
      ca = find_hypotenuse(ab, bc)
      if round(ca) != ca: continue
      # print("ab: " + str(ab) + " bc: " + str(bc) + " ca: " + str(ca))
      if is_one_side(ab, ca) or is_one_side(bc, ca):
        print("REVERSED! ", ab, bc, ca)


if __name__ == "__main__":
  main()