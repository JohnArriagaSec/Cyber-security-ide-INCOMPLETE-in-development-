from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox
from core.editor import Editor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tellerium Code Editor")
        self.setGeometry(100, 100, 1000, 600)

        #editor widget
        self.editor = Editor()
        self.setCentralWidget(self.editor)

        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if path:
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            self.editor.setPlainText(text)

    def save_file(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Python Files (*.py);;All Files (*)")
        if path:
            with open(path, 'w', encoding='utf-8') as f:
                text = self.editor.toPlainText()
                f.write(text)
            QMessageBox.information(self, "Saved", "File saved successfully!")
