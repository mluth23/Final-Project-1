from gui import *


def main():
    window = Tk()
    window.title('GPA Calculator')
    window.geometry('350x490')
    window.resizable(False, False)
    gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()