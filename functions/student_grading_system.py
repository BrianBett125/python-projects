import statistics

# --- Function 1: Data validation ---
def validate_scores(scores):
    """Ensure all scores are between 0 and 100."""
    return all(0 <= score <= 100 for score in scores)

# --- Function 2: Calculate grade based on score ---
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# --- Function 3: Assign grades for all students ---
def assign_grades(students):
    """
    students: dict with name -> list of scores
    returns dict with name -> (average, grade)
    """
    results = {}
    for name, scores in students.items():
        if not validate_scores(scores):
            raise ValueError(f"Invalid scores for {name}")
        
        avg = statistics.mean(scores)
        grade = get_grade(avg)
        results[name] = (avg, grade)
    return results

# --- Function 4: Recursive function to calculate GPA (simplified) ---
def calculate_gpa(grades, index=0, total=0):
    """Recursively compute GPA where A=4, B=3, C=2, D=1, F=0"""
    grade_map = {"A":4, "B":3, "C":2, "D":1, "F":0}
    
    if index == len(grades):  # base case
        return total / len(grades) if grades else 0
    
    return calculate_gpa(grades, index+1, total + grade_map[grades[index]])

# --- Function 5: Higher-order function (takes a function as argument) ---
def summarize(results, func):
    """Apply a function (like max, min) to student averages"""
    return func([(name, avg) for name, (avg, _) in results.items()], key=lambda x: x[1])

# --- MAIN PROGRAM ---
if __name__ == "__main__":
    students = {
        "Alice": [95, 92, 88],
        "Bob": [70, 65, 72],
        "Charlie": [100, 100, 98],
        "Diana": [55, 60, 58]
    }

    results = assign_grades(students)

    for student, (avg, grade) in results.items():
        print(f"{student}: Average={avg:.2f}, Grade={grade}")

    # Extract all grades
    grade_list = [grade for _, (_, grade) in results.items()]
    print("\nClass GPA:", round(calculate_gpa(grade_list), 2))

    # Find top student using higher-order function
    top_student = summarize(results, max)
    print("Top Student:", top_student)

