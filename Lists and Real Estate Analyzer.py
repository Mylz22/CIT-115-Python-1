def getFloatInput(prompt):
    while True:
        try:
            user_input = input(prompt)
            value = float(user_input)

            if value <= 0:
                print("Error: Value must be positive and non-zero.")
                continue

            return value
        except ValueError:
            print("Error: Please enter a valid number.")

def getMedian(sales):
    sales.sort()
    n = len(sales)

    if n % 2 == 1:
        return sales[n//2]
    else:
        middle1 = sales[n//2-1]
        middle2 = sales[n//2]
        return(middle1 + middle2) / 2

def main():
    sales_list = []

    while True:
        fSalesPrice = getFloatInput("Enter property sales value: ")
        sales_list.append(fSalesPrice)

        while True:
            user_choice = input("Enter another value Y or N: ").lower()
            if user_choice == 'y':
                break
            elif user_choice == 'n':
                break
            else:
                print("Invalid input. Please enter Y or N.")

        if user_choice == 'n':
            break

    sales_list.sort()

    print("\nSorted Property Sales Values:")
    for sale in sales_list:
        print(f"${sale:,.2f}")

    min_value = sales_list[0]
    max_value = sales_list[-1]
    total = sum(sales_list)
    average = total / len(sales_list)
    commission = total * 0.03
    median = getMedian(sales_list)

    print(f"\nMinimum value: ${min_value:,.2f}")
    print(f"Maximum value: ${max_value:,.2f}")
    print(f"Total value: ${total:,.2f}")
    print(f"Average value: ${average:,.2f}")
    print(f"Median value: ${median:,.2f}")
    print(f"Commission (3% of total): ${commission:,.2f}")

    if __name__ == "__main__":
        main()





