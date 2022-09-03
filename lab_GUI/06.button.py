from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys

#pyqt 구조: 슬롯과 시그널(신호)

class GUI(QWidget):

    def __init__(self):
        super().__init__()

        # 창 크기 조절
        self.setFixedSize(400, 300)
        # 창 제목 설정
        self.setWindowTitle('제목')
        # 창 띄우기
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GUI()
    sys.exit(app.exec_())