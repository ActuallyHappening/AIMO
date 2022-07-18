def find_all_for_second_const_number(number):
    """Return all numbers assuming 3^n - 3^number"""
    total_list = []
    right_hand_side = 3**number
    for i in range(0, 7):
        left_hand_side = 3**i
        newNum = left_hand_side - right_hand_side
        if newNum <= 0: continue
        total_list.append(newNum)
    print("Total list with index 3^ n - 3^" + str(number) + ": " + str(total_list))
    return total_list

def main():
    """Main function"""
    grand_total = set()
    for i in range(0, 7):
        for num in find_all_for_second_const_number(i):
          grand_total.add(num)
    grand_total = list(grand_total)
    grand_total.sort()
    print("Grand total: " + str(grand_total))
    print("Grand total len:" + str(len(grand_total)))

if __name__ == "__main__":
  main()