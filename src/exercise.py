def main():
    #write your code below this line
    numbers = [1,3,10,-1,5,0]

    print("The numbers in the range [0, 5]")
    print_numbers_in_range(numbers, 0, 5)

def print_numbers_in_range(numbers, lower_limit, upper_limit):
    for number in numbers:
        if number >= lower_limit and number <= upper_limit:
            print(number)

if __name__ == '__main__':
    main()
