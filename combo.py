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
        my_label = qtw.QLabel("Pick Something from the List Below")
        my_label.setFont(qtg.QFont("Helvetica", 24))

        # Create A Combo Box
        my_combo = qtw.QComboBox(self,
                                 editable=True,
                                 insertPolicy=qtw.QComboBox.InsertAtTop)

        # Add Items to Combo Box
        my_combo.addItem("Pepperoni", "Something")
        my_combo.addItem("Cheese", 2)
        my_combo.addItem("Mushroom", qtw.QWidget)
        my_combo.addItem("Peppers")


        # Create A Button
        my_button = qtw.QPushButton("Press Me", clicked=lambda: press_it())

        # Add Widgets to Layout
        self.layout().addWidget(my_label)
        self.layout().addWidget(my_combo)
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            my_label.setText(f"You Picked {my_combo.currentText()}!")



app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
