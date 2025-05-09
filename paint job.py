import math

def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("please enter a positive, non-zero number.")
            else:
                return value
        except ValueError:
            print("invalid input. Please enter a valid number.")

def getGallonsOfPaint(squareFeet, feetPerGallon):
    return math.ceil(squareFeet / feetPerGallon)

def getLaborHours(laborHoursPerGallon, totalGallons):
    return laborHoursPerGallon * totalGallons

def getLaborCost(laborHours, laborChargePerHour):
    return laborHours * laborChargePerHour

def getPaintCost(totalGallons, paintPrice):
    return totalGallons * paintPrice

def getSalesTax(state):
    state_tax = {
        "CT": 0.06,
        "MA": 0.0625,
        "ME": 0.085,
        "NH": 0.0,
        "RI": 0.07,
        "VT": 0.06
    }
    return state_tax.get(state.upper(),0.0)

def showCostEstimate(squareFeet, paintPrice, feetPerGallon, laborHoursPerGallon, laborChargePerHour, state, lastName):
    totalGallons = getGallonsOfPaint(squareFeet, feetPerGallon)
    laborHours = getLaborHours(laborHoursPerGallon, totalGallons)
    laborCost = getLaborCost(laborHours, laborChargePerHour)
    paintCost = getPaintCost(totalGallons, paintPrice)
    salesTax= getSalesTax(state)

    totalCost = laborCost + paintCost
    totalWithTax = totalCost * (1 + salesTax)

    print(f"Customer: {lastName}")
    print(f"State: {state}")
    print(f"Square feet of wall: {squareFeet}")
    print(f"Paint price: {paintPrice}")
    print(f"Feet per Gallon: {feetPerGallon}")
    print(f"Labor Hours per Gallon: {laborHoursPerGallon}")
    print(f"Labor Charge per Hour: {laborChargePerHour}")
    print(f"Total Gallons of Paint: {totalGallons}")
    print(f"Total Labor Hours: {laborHours}")
    print(f"Labor Cost: {laborCost}")
    print(f"Paint Cost: {paintCost}")
    print(f"Sales Tax: {salesTax * 100}%")
    print(f"Total Cost with Tax: {totalWithTax}")

    with open(f"{lastName}_PaintJobOutput.txt", "w") as file:
        file.write(f"Customer: {lastName}\n")
        file.write(f"State: {state}\n")
        file.write(f"Square Feet of Wall: {squareFeet}\n")
        file.write(f"Paint Price: {paintPrice}\n")
        file.write(f"Feet per Gallon: {feetPerGallon}\n")
        file.write(f"Labor Hours per Gallon: {laborHoursPerGallon}\n")
        file.write(f"Labor Charge per Gallon: {laborChargePerHour}\n")
        file.write(f"Total Gallons of Paint: {totalGallons}\n")
        file.write(f"Total Labor Hours: {laborHours}\n")
        file.write(f"Labor Cost: {laborCost}\n")
        file.write(f"Paint Cost: {paintCost}\n")
        file.write(f"Sales Tax: {salesTax * 100}%\n")
        file.write(f"Total Cost with Tax: {totalWithTax}\n")

def main ():
    squareFeet = getFloatInput("Enter the Square Feet of the Wall:")
    paintPrice =  getFloatInput("Enter the Paint Price:")
    feetPerGallon = getFloatInput("Enter the Feet per Gallon of Paint:")
    laborHoursPerGallon = getFloatInput("Enter the Labor Hours per Gallon:")
    laborChargePerHour = getFloatInput("Enter the Labor Charge per Hour:")

    state = input("Enter the state of the job (CT,MA,ME,NH,RI,VT: ").strip()
    lastName = input("Enter the customers last name:").strip()

    showCostEstimate(squareFeet, paintPrice, feetPerGallon, laborHoursPerGallon, laborChargePerHour, state, lastName)

    if __name__ == "__main__":
        main()