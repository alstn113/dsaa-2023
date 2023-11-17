from PyQt5.QtWidgets import QDesktopWidget


def center(self):
    """
    Center the window on the screen
    """
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())
