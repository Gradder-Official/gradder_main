from api.classes import Admin
from api.classes import Parent
from api.classes import Student
from api.classes import Teacher

# Converts the string to the Class type
TYPE_DICTIONARY = {
    "Teacher": Teacher,
    "Student": Student,
    "Parent": Parent,
    "Admin": Admin,
}
