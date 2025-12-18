def result_details():
    number_of_courses = int(input("Enter number of courses (at least 4): "))

    while number_of_courses < 4:
        print("You must enter at least 4 courses.")
        number_of_courses = int(input("Enter number of courses (at least 4): "))

    total_score = 0

    for i in range(number_of_courses):
        course_code = input("Enter course code: ")
        section = input("Enter section: ")
        score = int(input("Enter fictitious score: "))

        total_score += score

    average = total_score / number_of_courses
    print("Average Score:", average)
    return average


# Function call
result_details()
