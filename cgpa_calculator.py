def calculate_cgpa(grades, credits):
    total_points = 0
    total_credits = 0

    for grade, credit in zip(grades, credits):
        total_points += grade * credit
        total_credits += credit

    cgpa = total_points / total_credits
    return cgpa

def main():
    num_subjects = int(input("Enter the number of subjects: "))
    grades = []
    credits = []

    for _ in range(num_subjects):
        grade = float(input("Enter the grade for subject: "))
        credit = float(input("Enter the credit for subject: "))
        grades.append(grade)
        credits.append(credit)

    cgpa = calculate_cgpa(grades, credits)
    print(f"Your CGPA is: {cgpa:.2f}")

if __name__ == "__main__":
    main()
