import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Change The Title
        self.setWindowTitle("Forms With PyQt5")

        # Set A Form Layout
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        # Add Widgets
        label_1 = qtw.QLabel("This is a Cool Label Row")
        label_1.setFont(qtg.QFont("Helvetica", 24))

        first_name = qtw.QLineEdit(self)
        last_name = qtw.QLineEdit(self)

        # Add Rows To App
        form_layout.addRow(label_1)
        form_layout.addRow("First Name", first_name)
        form_layout.addRow("Last Name", last_name)
        form_layout.addRow(qtw.QPushButton("Press Me", clicked=lambda: press_it()))

        self.show()

        def press_it():
            label_1.setText(f"You Clicked The Button, {first_name.text()} {last_name.text()}!")


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
