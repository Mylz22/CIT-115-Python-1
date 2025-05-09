str_name = input("Enter the students name: ")

try:
    int_score1 = int(input("Enter first test score (whole number): "))
    int_score2 = int(input("Enter second test score (whole number): "))
    int_score3 = int(input("Enter third test score(whole number): "))
    int_score4 = int(input("Enter fourth test score (whole number): "))
except ValueError:
    print("Invalid input. Please enter whole numbers only.")
    exit()

if int_score1 < 0 or int_score2 < 0 or int_score3 < 0 or int_score4 < 0:
    print("Test scores must be greater than 0.")
    exit()

str_dropLowest = input("Drop the lowest grade? (Y/N): ").upper()

if str_dropLowest not in  ('Y', 'N'):
    print("Enter Y or N to Drop the Lowest Grade.")
    exit()

if str_dropLowest == 'Y':
    if int_score1 <= int_score2 and int_score1 <= int_score3 and int_score1 <= int_score4:
        flt_average = (int_score2 + int_score3 + int_score4) / 3
    elif int_score2 <= int_score1 and int_score2 <= int_score3 and int_score2 <= int_score4:
        flt_average = (int_score1 + int_score3 + int_score4) / 3
    elif int_score3 <= int_score1 and int_score3 <= int_score2 and int_score3 <= int_score4:
        flt_average = (int_score1 + int_score2 + int_score4) / 3
    else:
        flt_average = (int_score1 + int_score2 + int_score3) / 3
else:
    flt_average = (int_score1 + int_score2 + int_score3) / 3

if flt_average >= 97.0:
    str_grade = "A+"
elif flt_average >= 94.0:
    str_grade = "A"
elif flt_average >= 90.0:
    str_grade = "A-"
elif flt_average >= 87.0:
    str_grade = "B+"
elif flt_average >= 84.0:
    str_grade = "B"
elif flt_average >= 80.0:
    str_grade = "B-"
elif flt_average >= 77.0:
    str_grade = "C+"
elif flt_average >= 74.0:
    str_grade = "C"
elif flt_average >= 70.0:
    str_grade = "C-"
elif flt_average >= 67.0:
    str_grade = "D+"
elif flt_average >= 64.0:
    str_grade = "D"
elif flt_average >= 60.0:
    str_grade = "D-"
else:
    str_grade = "F"

print(f"student: {str_name}")
print(f"Final Average: {flt_average:.1f}")
print(f"Letter Grade: {str_grade}")


