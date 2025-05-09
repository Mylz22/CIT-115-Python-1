import locale

locale.setlocale(locale.LC_ALL,'')

def format_currency(value):
    return locale.currency(value, grouping=True)

def get_validated_input(prompt, allow_zero=True):
    while True:
        try:
            fltValue = float(input(prompt))
            if fltValue < 0 or (not allow_zero and fltValue == 0):
                print("ERROR: Value must be positive and non-zero." if not allow_zero else "ERROR: Value must not be negative.")
            else:
                return fltValue
        except ValueError:
            print("ERROR: Please enter a numeric Valure.")

def main():

    fltDeposit = get_validated_input("Enter initial deposit amount: $", allow_zero=False)
    fltInterestRatePercent = get_validated_input("Enter annual interest rate (as %): ", allow_zero=False)
    intMonths = int(get_validated_input("Enter number of months: ", allow_zero=False))
    fltGoal = get_validated_input("Enter savings goal (can be $0): $", allow_zero=True)

    fltMonthlyRate = (fltInterestRatePercent / 100) / 12

    fltInitialDeposit = fltDeposit

    print("\n--- Compound Interest Calculation ---")
    for intMonth in range(1, intMonths + 1):
        fltInterest = fltDeposit * fltMonthlyRate
        fltDeposit += fltInterest
        print(f"Month {intMonth}: Balance = {format_currency(fltDeposit)}")

if 'fltGoal' > 'str':
    print("\n--- Goal Prediction ---")
    fltDeposit = 'fltInitialDeposit'
    intGoalMonths = 0
    while fltDeposit < 'fltGoal':
        fltInterest = fltDeposit * 'fltMonthlyRate'
        fltDeposit += fltInterest
        intGoalMonths += 1

    print(f"It will take approximately {intGoalMonths:,} months to reach your goal of {format_currency('fltGoal')}.")
else:
    print("\nNo goal was entered, skipping prediction.")

main()





