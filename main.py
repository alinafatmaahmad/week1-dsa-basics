
# Week 1: Data Structures and Algorithms
# Exercise T024

# --------------------------------
# 1. SEARCH
# --------------------------------

def search_value(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index

    return -1


# --------------------------------
# 2. DEDUPLICATION
# --------------------------------

def remove_duplicates(numbers):
    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    return unique_numbers


# --------------------------------
# 3. FREQUENCY COUNTING
# --------------------------------

def count_frequency(numbers):
    frequency = {}

    for number in numbers:
        if number in frequency:
            frequency[number] = frequency[number] + 1
        else:
            frequency[number] = 1

    return frequency


# --------------------------------
# 4. PAGINATION
# --------------------------------

def get_page(items, page_number, page_size):
    if page_number < 1 or page_size < 1:
        return []

    start = (page_number - 1) * page_size
    end = start + page_size

    return items[start:end]


# --------------------------------
# 5. EFFICIENT LOOKUP
# --------------------------------

def create_lookup(students):
    student_lookup = {}

    for student in students:
        student_id = student["id"]
        student_lookup[student_id] = student

    return student_lookup


def find_student(student_lookup, student_id):
    return student_lookup.get(student_id)


# --------------------------------
# TEST ALL FIVE SOLUTIONS
# --------------------------------

if __name__ == "__main__":

    print("1. SEARCH")

    numbers = [10, 20, 30, 40, 50]

    print("Position of 30:", search_value(numbers, 30))
    print("Position of 99:", search_value(numbers, 99))
    print("Empty list:", search_value([], 10))


    print("\n2. DEDUPLICATION")

    numbers = [10, 20, 10, 30, 20, 40]

    print("Original list:", numbers)
    print("After removing duplicates:", remove_duplicates(numbers))
    print("Empty list:", remove_duplicates([]))


    print("\n3. FREQUENCY COUNTING")

    numbers = [10, 20, 10, 30, 20, 10]

    print("Frequency:", count_frequency(numbers))
    print("Empty list:", count_frequency([]))


    print("\n4. PAGINATION")

    students = ["Aman", "Alina", "Anam", "Rahul", "Sara"]

    print("Page 1:", get_page(students, 1, 2))
    print("Page 2:", get_page(students, 2, 2))
    print("Page 3:", get_page(students, 3, 2))
    print("Invalid page:", get_page(students, 0, 2))
    print("Page beyond data:", get_page(students, 10, 2))


    print("\n5. EFFICIENT LOOKUP")

    students = [
        {"id": 101, "name": "Aman"},
        {"id": 102, "name": "Alina"},
        {"id": 103, "name": "Anam"}
    ]

    student_lookup = create_lookup(students)

    print("Student 102:", find_student(student_lookup, 102))
    print("Student 999:", find_student(student_lookup, 999))
    print("Empty lookup:", find_student({}, 101))
