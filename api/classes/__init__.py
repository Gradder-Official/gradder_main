# NOTE: the order is important to avoid the circular imports
from .user import User

from .submission import Submission
from .assignment import Assignment
from .course import Course

from .admin import Admin
from .student import Student
from .parent import Parent
from .teacher import Teacher