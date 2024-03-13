def student_avg():
    # Assuming you provide input data directly here
    n = int(input("Enter the number of students: "))
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter the student name for average calculation: ")
    average_score = 0
    for key, value in student_marks.items():
        if key == query_name:
            average_score = sum(value) / len(value)
            break  # Exit the loop once we find the student's scores
    print("{:.02f}".format(average_score))  # Print the average score






