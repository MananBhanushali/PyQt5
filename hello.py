import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Change The Title
        self.setWindowTitle("Hello PyQt5")

        # To Change Window Icon

        # self.setWindowIcon(QtGui.QIcon("../CodeX/CodeX Base/codex.png"))

        # Set A Vertical Layout
        self.setLayout(qtw.QVBoxLayout())

        # Create A Label
        my_label = qtw.QLabel("What is Your Name?")
        my_label.setFont(qtg.QFont("Helvetica", 18))

        # Create A Entry Box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")

        # Create A Button
        my_button = qtw.QPushButton("Press Me", clicked=lambda: press_it())

        # Add Widgets to Layout
        self.layout().addWidget(my_label)
        self.layout().addWidget(my_entry)
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            my_label.setText(f"Hello {my_entry.text()}!")

            # Clear The Entry Box
            my_entry.setText("")


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
