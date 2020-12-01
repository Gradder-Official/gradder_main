from api.classes import Admin, Parent, Student, Teacher

# Converts the string to the Class type
TYPE_DICTIONARY = {
    "Teacher": Teacher,
    "Student": Student,
    "Parent": Parent,
    "Admin": Admin,
}
