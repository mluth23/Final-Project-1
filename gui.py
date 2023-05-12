from tkinter import *
import csv

class gui:
    def __init__(self, window) -> None:
        """
        Function to create GUI window
        :param window: created in main
        """
        self.window = window

        # Radio buttons
        self.frame_num_class = Frame(self.window)
        self.label_operation = Label(self.frame_num_class, text='Classes\t')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_one_class = Radiobutton(self.frame_num_class, text='1', variable=self.radio_1, value=1, command=self.get_num_classes)
        self.radio_two_class = Radiobutton(self.frame_num_class, text='2', variable=self.radio_1, value=2, command=self.get_num_classes)
        self.radio_three_class = Radiobutton(self.frame_num_class, text='3', variable=self.radio_1, value=3, command=self.get_num_classes)
        self.radio_four_class = Radiobutton(self.frame_num_class, text='4', variable=self.radio_1, value=4, command=self.get_num_classes)
        self.label_operation.pack(side='left', padx=5)
        self.radio_one_class.pack(side='left')
        self.radio_two_class.pack(side='left')
        self.radio_three_class.pack(side='left')
        self.radio_four_class.pack(side='left')
        self.frame_num_class.pack(anchor='w', pady=10)

        # name
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name)
        self.entry_name = Entry(self.frame_name)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', pady=10)
        self.entry_name.forget()

        # score 1
        self.frame_score_1 = Frame(self.window)
        self.label_score_1 = Label(self.frame_score_1)
        self.entry_score_1 = Entry(self.frame_score_1)
        self.label_score_1.pack(padx=5, side='left')
        self.entry_score_1.pack(padx=5, side='left')
        self.frame_score_1.pack(anchor='w', pady=10)
        self.entry_score_1.forget()

        # score 2
        self.frame_score_2 = Frame(self.window)
        self.label_score_2 = Label(self.frame_score_2)
        self.entry_score_2 = Entry(self.frame_score_2)
        self.label_score_2.pack(padx=5, side='left')
        self.entry_score_2.pack(padx=5, side='left')
        self.frame_score_2.pack(anchor='w', pady=10)
        self.entry_score_2.forget()

        # Score 3
        self.frame_score_3 = Frame(self.window)
        self.label_score_3 = Label(self.frame_score_3)
        self.entry_score_3 = Entry(self.frame_score_3)
        self.label_score_3.pack(padx=5, side='left')
        self.entry_score_3.pack(padx=5, side='left')
        self.frame_score_3.pack(anchor='w', pady=10)
        self.entry_score_3.forget()

        # Score 4
        self.frame_score_4 = Frame(self.window)
        self.label_score_4 = Label(self.frame_score_4)
        self.entry_score_4 = Entry(self.frame_score_4)
        self.label_score_4.pack(padx=5, side='left')
        self.entry_score_4.pack(padx=5, side='left')
        self.frame_score_4.pack(anchor='w', pady=10)
        self.entry_score_4.forget()

        # Display
        self.frame_display = Frame(self.window)
        self.label_display = Label(self.frame_display, text='')
        self.label_display.pack(anchor='w', side='bottom')
        self.frame_display.pack(anchor='w', pady=10)

        # Save button
        self.button_save = Button(self.window, text='CALCULATE', command=self.clicked)
        self.button_save.pack(side='bottom', pady=10)

    def calculate_gpa(self, classes: int, scores: list) -> float:
        """
        Function: to calculate the gpa of the student
        :param classes: number of classes
        :param scores: the scores of the student in list form
        :return: the gpa
        """
        weight_total = 0
        for i in scores:
            weight_total += i
        return weight_total/classes

    def get_grades(self, scores) -> list:
        """
        Function to get the weight of the students scores
        :param scores: list of the student's scores
        :return: a list of the weights of the scores
        """
        grade_weight = []
        for i in scores:
            if i >= 90:
                grade_weight.append(4)
            elif i >= 80:
                grade_weight.append(3)
            elif i >= 70:
                grade_weight.append(2)
            elif i >= 60:
                grade_weight.append(1)
            else:
                grade_weight.append(0)
        return grade_weight

    def get_num_classes(self) -> None:
        """
        Function: Get the number of classes and put the entry boxes for how many there are
        """
        num_classes = self.radio_1.get()
        if num_classes == 1:
            self.label_name.config(text='Name')
            self.label_score_1.config(text='Score 1')
            self.label_score_2.config(text='')
            self.label_score_3.config(text='')
            self.label_score_4.config(text='')
            self.entry_name.pack(padx=5, side='left')
            self.entry_score_1.pack(padx=5, side='left')
            self.entry_score_2.forget()
            self.entry_score_3.forget()
            self.entry_score_4.forget()
            self.label_display.destroy()
            self.entry_name.delete(0, END)
            self.entry_score_1.delete(0, END)
            self.entry_name.focus_set()
        elif num_classes == 2:
            self.label_name.config(text='Name')
            self.label_score_1.config(text='Score 1')
            self.label_score_2.config(text='Score 2')
            self.label_score_3.config(text='')
            self.label_score_4.config(text='')
            self.entry_name.pack(padx=5, side='left')
            self.entry_score_1.pack(padx=5, side='left')
            self.entry_score_2.pack(padx=5, side='left')
            self.entry_score_3.forget()
            self.entry_score_4.forget()
            self.label_display.destroy()
            self.entry_name.delete(0, END)
            self.entry_score_1.delete(0, END)
            self.entry_score_2.delete(0, END)
            self.entry_name.focus_set()
        elif num_classes == 3:
            self.label_name.config(text='Name')
            self.label_score_1.config(text='Score 1')
            self.label_score_2.config(text='Score 2')
            self.label_score_3.config(text='Score 3')
            self.label_score_4.config(text='')
            self.entry_name.pack(padx=5, side='left')
            self.entry_score_1.pack(padx=5, side='left')
            self.entry_score_2.pack(padx=5, side='left')
            self.entry_score_3.pack(padx=5, side='left')
            self.entry_score_4.forget()
            self.label_display.destroy()
            self.entry_name.delete(0, END)
            self.entry_score_1.delete(0, END)
            self.entry_score_2.delete(0, END)
            self.entry_score_3.delete(0, END)
            self.entry_name.focus_set()
        elif num_classes == 4:
            self.label_name.config(text='Name')
            self.label_score_1.config(text='Score 1')
            self.label_score_2.config(text='Score 2')
            self.label_score_3.config(text='Score 3')
            self.label_score_4.config(text='Score 4')
            self.entry_name.pack(padx=5, side='left')
            self.entry_score_1.pack(padx=5, side='left')
            self.entry_score_2.pack(padx=5, side='left')
            self.entry_score_3.pack(padx=5, side='left')
            self.entry_score_4.pack(padx=5, side='left')
            self.label_display.destroy()
            self.entry_name.delete(0, END)
            self.entry_score_1.delete(0, END)
            self.entry_score_2.delete(0, END)
            self.entry_score_3.delete(0, END)
            self.entry_score_4.delete(0, END)
            self.entry_name.focus_set()

    def get_name(self) -> str:
        """
        Function to get name from the entry
        :return: a string of the name
        """
        return self.entry_name.get()

    def clicked(self) -> None:
        """
        Function to run the GUI
        """
        score_string = ' '
        num_classes = self.radio_1.get()
        scores = []
        name = self.get_name()

        self.label_display.destroy()
        self.label_display = Label(self.frame_display, text='')
        self.label_display.pack(anchor='w', side='bottom')

        # adds the scores to the list of scores
        try:
            if num_classes == 1:
                scores.append(float(self.entry_score_1.get()))
            elif num_classes == 2:
                scores.append(float(self.entry_score_1.get()))
                scores.append(float(self.entry_score_2.get()))
            elif num_classes == 3:
                scores.append(float(self.entry_score_1.get()))
                scores.append(float(self.entry_score_2.get()))
                scores.append(float(self.entry_score_3.get()))
            elif num_classes == 4:
                scores.append(float(self.entry_score_1.get()))
                scores.append(float(self.entry_score_2.get()))
                scores.append(float(self.entry_score_3.get()))
                scores.append(float(self.entry_score_4.get()))
            grades = self.get_grades(scores)
            gpa = self.calculate_gpa(num_classes, grades)

            score_num = 1
            # Puts the letter scores in a string to send to the display
            for i in scores:
                if i >= 90:
                    score_string += f'Score {score_num}: A\n'
                    score_num += 1
                elif i >= 80:
                    score_string += f'Score {score_num}: B\n'
                    score_num += 1
                elif i >= 70:
                    score_string += f'Score {score_num}: C\n'
                    score_num += 1
                elif i >= 60:
                    score_string += f'Score {score_num}: D\n'
                    score_num += 1
                else:
                    score_string += f'Score {score_num}: F\n'
                    score_num += 1
            self.label_display.config(text=f"{score_string}{name}'s GPA: {gpa:.2f}")

            with open('file.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([name, gpa])

        except ValueError:
            self.label_display = Label(self.frame_display, text=f'Score must be in number form.\nex. 2 not two.')
            self.label_display.pack(anchor='w', side='bottom')
            self.frame_display.pack(anchor='w', pady=10)
            self.entry_score_1.delete(0, END)
            self.entry_score_2.delete(0, END)
            self.entry_score_3.delete(0, END)
            self.entry_score_4.delete(0, END)
            self.entry_score_1.focus_set()
