from NIWEVN import *
package_path = widget_pp(__file__)

from PySide2.QtWidgets import QLabel, QVBoxLayout, QPushButton
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap

from PySide2.QtWidgets import QWidget

class %CLASS%(QWidget):
    def __init__(self, parent_node_instance):
        super(%CLASS%, self).__init__()

        # leave these lines ------------------------------
        self.parent_node_instance = parent_node_instance
        # ------------------------------------------------

        self.label = QLabel()
        pix = QPixmap(package_path+'perceptron.png')
        self.label.setPixmap(pix.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.label)
        self.setStyleSheet('background: transparent;')


    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass


    def remove_event(self):
        pass
