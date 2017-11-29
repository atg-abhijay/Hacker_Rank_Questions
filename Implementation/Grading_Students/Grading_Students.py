def solve(grades):
    # Complete this function
    rounded_grades = []
    for grade in grades:
        diff = 5 - (grade%5)
        if grade < 38 or diff > 2:
            rounded_grades.append(grade)
        else:
            rounded_grades.append(grade + diff)

    return rounded_grades


def main():
    n = int(raw_input().strip())
    grades = []
    grades_i = 0
    for grades_i in xrange(n):
        grades_t = int(raw_input().strip())
        grades.append(grades_t)
    result = solve(grades)
    print "\n".join(map(str, result))

main()
