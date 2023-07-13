
def is_student_name_incorrect(username: str) -> bool:
    is_incorrect = True
    if (len(username.split()) == 3):
        is_incorrect = False
    return is_incorrect


def get_student_name(student: str, student_index: int) -> list:
    while (is_student_name_incorrect(student)):
        print("Вы ввели некорректные данные, пожалуйста проверьте и введите ещё раз ")
        student = input("Введите имя, фамилию и отчество студента ")
    return (student, student_index)


def get_student_subjects(student_index: int, student_subject_debt: dict):
    subject = input("Введите предметы, по которым у студента задолженность, для окончания оперции нажмите q ")
    student_subject_debt[student_index] = []
    while (subject != "q"):
        student_subject_debt[student_index].append(subject)
        subject = input("Введите предмет, по которым у студента задолженность, для окончания оперции нажмите q ")
    return student_subject_debt


def get_student_names_and_subjects() -> list:
    student = input("Введите имя, фамилию и отчество студента или введите q, если студенты закончились ")

    all_students = []
    subjects_to_pass = {}
    student_index = 1
    while (student != "q"):
        all_students.append(get_student_name(student, student_index))
        get_student_subjects(student_index, subjects_to_pass)
        student = input("Введите имя, фамилию и отчество студента или введите q, если студенты закончились ")
        student_index += 1
    return (all_students, subjects_to_pass)


def is_plus_or_minus(sign: str) -> str:
    while sign != "+" and sign != "-":
        print("Ваш ввод некорректный, введите + или - ")
        sign = input()
    return sign


def print_user_debt(students: list, subjects_debt: dict, number_of_retakes: int):
    all_student_passed_exam = True
    for student in students:
        if len(subjects_debt[student[1]]) != 0:
            all_student_passed_exam = False
            print(f"У студента {student[0]} после {number_of_retakes} остался долг по: ")
            for subject in subjects_debt[student[1]]:
                print(subject)
    if all_student_passed_exam:
        print("Нет никаких задолжностей, все студенты всё сдали")
        exit(0)


def is_user_pass_exams(students_and_subject_debt):
    students, subjects_debt = students_and_subject_debt
    for number_of_retakes in range(1, 4):
        for student in students:
            tmp_subjects = []
            for subject in subjects_debt[student[1]]:
                sign = is_plus_or_minus(input(f"Если студент {student[0]} сдал {subject} введите + иначе - "))
                if sign == "-":
                    tmp_subjects.append(subject)
            subjects_debt[student[1]] = tmp_subjects
        print_user_debt(students, subjects_debt, number_of_retakes)


def main():
    is_user_pass_exams(get_student_names_and_subjects())


if __name__ == "__main__":
    main()
