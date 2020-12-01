# NOTE: the order is important to avoid the circular imports
from .calendar_event import CalendarEvent
from .schoolconfig import SchoolConfig
from .user import User

from .submission import Submission
from .assignment import Assignment
from .course import Course

from .student import Student
from .parent import Parent
from .teacher import Teacher
from .admin import Admin
