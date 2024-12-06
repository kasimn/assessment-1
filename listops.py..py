numbers = {34, 18, 56, 25, 76, 8, 13, 22, 34, 46}

def print_list():
    print("the list is:" , numbers)

def print_sum():
    total_sum = sum(numbers)
    print ("the sum of all elementsin the list is:", total_sum)

def print_largest_and_smallest():
    largest = max (numbers)
    smallest = min (numbers)
    print("the largest elementis:", largest)
    print ("the smallest element is:", smallest)

    
def main():
    print_list()
    print_sum()
    print_largest_and_smallest()


if __name__=="__main__":
    main()

    
