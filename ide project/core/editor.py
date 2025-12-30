from PyQt5.QtWidgets import QTextEdit

class Editor(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setAcceptRichText(False)
        self.setPlaceholderText("Write your code here...")
        self.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #dcdcdc;
                font-family: Consolas;
                font-size: 14px;
            }
        """)
