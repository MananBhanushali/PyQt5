import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Change The Title
        self.setWindowTitle("Spin Boxes with PyQt5")

        # Set A Vertical Layout
        self.setLayout(qtw.QVBoxLayout())

        # Create A Label
        my_label = qtw.QLabel("Pick Something from the List Below")
        my_label.setFont(qtg.QFont("Helvetica", 24))

        # Create A Spin Box
        my_spin = qtw.QSpinBox(self,
                               value=10,
                               maximum=100,
                               minimum=0,
                               singleStep=5,
                               prefix="#",
                               suffix="!!!")

        my_label.setFont(qtg.QFont("Helvetica", 18))

        # Create A Button
        my_button = qtw.QPushButton("Press Me", clicked=lambda: press_it())

        # Add Widgets to Layout
        self.layout().addWidget(my_label)
        self.layout().addWidget(my_spin)
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            my_label.setText(f"You Picked {my_spin.value()}!")


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
