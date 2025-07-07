import time


class TutorNotAvailable(RuntimeError):
    pass


class StudentNotAvailable(RuntimeError):
    pass

class UserNotFound(RuntimeError):
    pass
class User:
    def __init__(self, id: int, role: str, created_at: float, points: int):
        self.id = id
        self.role = role
        self.created_at = created_at
        self.points = points
        

class Appointment:
    def __init__(self, student: int, tutor: int, start_time: float, end_time: float, topic: str):
        self.student = student  
        self.tutor = tutor
        self.start_time = start_time
        self.end_time = end_time
        self.topic = topic


class Assignment:
    def __init__(self, student: int, tutor:  int, start_time: float, due: float, topic: str):
        self.student = student
        self.tutor = tutor
        self.start_time = start_time
        self.due = due
        self.topic = topic


class Exam:
    def __init__(self, student: int, tutor: int, start_time: float, end_time: float, topic: str):
        self.student = student
        self.tutor = tutor
        self.start_time = start_time
        self.end_time = end_time
        self.topic = topic


class AvailableTimes:
    def __init__(self, tutor: int, start_time: float, end_time: float):
        self.tutor = tutor
        self.start_time = start_time
        self.end_time = end_time
   
     
def query_appointments(student: int | None = None, tutor: int | None = None, start_time: float = time.time()) -> list[Appointment]:
    if student is not None or tutor is not None:
        appointments: list[Appointment] = []  # TODO Query Appointments
        return appointments
    raise ValueError("Either student or tutor must be a valid ID.")


def query_assignments(student: int | None = None, tutor: int | None = None, due: float = time.time()) -> list[Assignment]:
    if student is not None or tutor is not None:
        assignments: list[Assignment] = []  # TODO Query Assignments
        return assignments
    raise ValueError("Either student or tutor must be a valid ID.")


def query_exams(student: int | None = None, tutor: int | None = None, start_time: float = time.time()) -> list[Exam]:
    if student is not None or tutor is not None:
        exams: list[Exam] = []  # TODO Query Exams
        return exams
    raise ValueError("Either student or tutor must be a valid ID.")


def query_available_times(tutor: int, start_time: float = time.time()) -> list[AvailableTimes]:
    available_times: list[AvailableTimes] = []  # TODO Query available times
    return available_times
    

def query_user(id: int) -> User:
    users: list[User] = []  # TODO Query user
    try:
        return users[0]
    except IndexError:
        raise UserNotFound("That user does not exist.") 


def book_appointment(student: int, tutor: int, start_time: float, end_time: float) -> None:
    query_user(tutor)
    query_user(student)
    available_times = query_available_times(tutor, 0)
    available_times_allowed = False
    for available_time in available_times:
        if start_time >= available_time.start_time and end_time <= available_time.end_time:
            available_times_allowed = True
    if available_times_allowed == False:
        raise TutorNotAvailable("The tutor is not available at that point in time.")
    appointments = query_appointments(tutor, 0)
    appointment_allowed = False
    for appointment in appointments:
        if start_time >= appointment.start_time and end_time <= appointment.end_time:
            appointment_allowed = True
    if appointment_allowed == False:
        raise TutorNotAvailable("The tutor already has an appointment at that point in time.")
    appointments = query_appointments(student, 0)
    appointment_allowed = False
    for appointment in appointments:
        if start_time >= appointment.start_time and end_time <= appointment.end_time:
            appointment_allowed = True
    if appointment_allowed == False:
        raise StudentNotAvailable("The student already has an appointment at that point in time.")
    # TODO Appointment booking