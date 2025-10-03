# File name: nested_if_else_example.py

# Program to determine student performance based on marks

marks = int(input("Enter your marks (0 - 100): "))

if marks >= 0 and marks <= 100:
    if marks >= 50:
        if marks >= 70:
            if marks >= 90:
                print("Grade: A (Excellent 👏)")
            else:
                print("Grade: B (Good 😊)")
        else:
            print("Grade: C (Average 🙂)")
    else:
        if marks >= 30:
            print("Grade: D (Needs Improvement 😕)")
        else:
            print("Grade: F (Fail ❌)")
else:
    print("Invalid marks entered. Please enter a number between 0 and 100.")

