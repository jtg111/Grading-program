from PyQt5.QtWidgets import *
from Grading import *

class Controller(QMainWindow, Ui_MainWindow):
    """
    A class that takes in and calculates the scores for a specified amount of students.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor that imports data and sets up the ui for the grading program.
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        #Hiding elements
        hidden = [self.scores_entry, self.scores_entry_label, self.error_thing, self.grade_output]

        for i in hidden:
            i.setVisible(False)

        # Connecting buttons to functions
        self.close_button.clicked.connect(lambda: self.close())
        self.next_button.clicked.connect(lambda: self.next())
        self.submit_button.clicked.connect(lambda: self.submit())
        self.clear_button.clicked.connect(lambda: self.clear())


    def next(self):
        """
        The next function verifies that the number being entered in the total students entry is in fact an integer and
        not greater than 5. I will also allow for the program to unhide the scores entry box.
        :return: Does not return anytihng. Mainly used for validation
        """
        try:
            # Grabbing value from entry
            total_students = int(self.num_students_entry.text())
            if isinstance(int(self.num_students_entry.text()), int) is True:
                if int(self.num_students_entry.text()) <= 5:

                    # Making sure elements are visible
                    self.error_thing.setVisible(False)
                    self.scores_entry.setVisible(True)
                    self.scores_entry_label.setVisible(True)

                    # Changing label to match the amount of students entered
                    self.scores_entry_label.setText("Enter "+str(total_students)+" score(s). Separate with space."
                                                                                " Press submit when done")
                else:
                    # Showing error if number of students is greater than 5
                    self.error_thing.setText("Max students is 5.")
                    self.error_thing.setVisible(True)
                    raise TypeError
        except ValueError:
            # Showing error if thing entered is not an integer value
            self.error_thing.setText("Total students must be integer value.")
            self.error_thing.setVisible(True)
        except TypeError as e:
            pass

    def submit(self):
        """
        Submit function is where all the data entered is processed and outputs the final scores.
        :return: Does not return anything as final grades are output in a Qlabel box
        """
        # Setting up variables
        students = int(self.num_students_entry.text())
        scores = (self.scores_entry.text()).split()
        score_list = [int(i) for i in scores]
        self.grade_output.setText("")

        # Final grading process, using modified functions from past lab.
        while True:
            if len(score_list) == students:
                new_list = self.l_modifier(score_list, students)
                self.grader(new_list)
                break
            elif len(score_list) < students:
                scores = (input("Enter " + str(students) + " score(s): ")).split()
                score_list = [int(i) for i in scores]
                new_list = self.l_modifier(score_list, students)
                self.grader(new_list)
                break
            elif len(score_list) > students:
                new_list = self.l_modifier(score_list, students)
                new_list = new_list[:students]
                self.grader(new_list)
                break
            else:
                " "
        self.grade_output.setVisible(True)

    def grader(self, list_of_scores):
        """
        This function is what calculates the grades for each of the scores entered through a list.
        :param list_of_scores: Is created within the submit function and input here.
        :return: Does not return anything.
        """
        # Grabbing the highest score and calculating the final letter grade.
        best = max(list_of_scores)
        for count, i in enumerate(list_of_scores):
            if i >= (best - 10):
                grade = "A"
            elif i >= (best - 20):
                grade = "B"
            elif i >= (best - 30):
                grade = "C"
            elif i >= (best - 40):
                grade = "D"
            else:
                grade = "F"
            text = "Student {} score is {} and grade is {}.".format(count + 1, i, grade)
            current_text = self.grade_output.text()
            self.grade_output.setText(current_text + "\n" + text)

    def l_modifier(self, a_list, number_of_students):
        """
        Checks and modifies list of students if that list turns out to be long than the total number of students.
        :param a_list: The list being checked
        :param number_of_students: The total number of students.
        :return:
        """
        if len(a_list) != number_of_students:
            a_list = a_list[:number_of_students]
            return a_list
        else:
            return a_list

    def clear(self):
        """
        Function that clears the entire program and resets the program to the start.
        """
        hidden = [self.scores_entry, self.scores_entry_label, self.error_thing, self.grade_output]

        for i in hidden:
            i.setVisible(False)

        self.scores_entry_label.clear()
        self.num_students_entry.clear()
        self.scores_entry.clear()
