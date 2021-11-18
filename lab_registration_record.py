# course: Object-oriented programming, year 2, semester 1
# academic year: 2021-22
# author: B. Schoen-Phelan
# date: 18-11-2020
# purpose: An exercise to get familiar with composition


class Student:
    """
    INSERT YOUR DOCSTRING INFORMATION HERE
    """

    def __init__(self, study_type, f_name, l_name):
        # YOUR CODE GOES HERE
        pass

    # YOUR CODE GOES HERE



class RegistrationData:
    """
    INSERT YOUR DOCSTRING INFORMATION HERE
    """
    def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
        # YOUR CODE GOES HERE
        pass

    # YOUR CODE GOES HERE



# using the class
# NOTE: THIS CODE BELOW WILL NOT WORK YET AS __YOU__ NEED TO IMPLEMENT WHAT
# MAKES IT POSSIBLE TO RUN THE BELOW CODE!!!!
r = RegistrationData("8 Grangegorman Road Lower, Dublin 1, Ireland", 1500,
                     Student.POSTGRADUATE, "Bianca", "Phelan")
r.display_student_data()
r.student_id_property="C12345"
r.display_student_data()
for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
    r.student_object.courses = course

r.display_student_data()

# print(RegistrationData.__doc__)
