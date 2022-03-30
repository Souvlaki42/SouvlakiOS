from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5.Qsci import *

import os, sys, globals

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #clear terminal
        self.saved = True
        globals.cmd("Notepad")

        font = QFont()
        font.setFamily('Courier')
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.setFont(font)

        def text_changed():
            title = self.windowTitle()
            self.saved = False
            self.lines = str(self.editor.lines())
            self.linechar = len(self.lines)
            self.editor.setMarginWidth(0,10*self.linechar)
            if not "*" in title:
                self.setWindowTitle("*" + title)
            if self.editor.text == "":
                self.saved = True

        layout = QVBoxLayout()
        self.editor = QsciScintilla()
        self.filedialog = QFileDialog(self)
        self.lines = 1
        self.linechar = 1
        self.editor.textChanged.connect(lambda:text_changed())
        self.editor.setMarginsFont(font)
        self.editor.setMarginsForegroundColor(QColor("#hhhhhh"))
        self.editor.setMarginLineNumbers(0, True)
        self.editor.setMarginsBackgroundColor(QColor("#cccccc"))
        self.editor.setMarginWidth(0,10*self.linechar)
        # Set the autocompletions to case Insensitive
        # self.editor.setAutoCompletionCaseSensitivity(False)
        # Set the autocompletion to not replace the word to the right of the cursor
        # self.editor.setAutoCompletionReplaceWord(False)
        # Set the autocompletion source to be the words in the
        # document
        # self.editor.setAutoCompletionSource(QsciScintilla.AcsDocument)
        # Set the autocompletion dialog to appear as soon as 1 character is typed
        # self.editor.setAutoCompletionThreshold(1)

        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.editor.setFont(fixedfont)

        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        self.path = None

        layout.addWidget(self.editor)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        toolbar = QToolBar("Toolbar")
        toolbar.setIconSize(QSize(32, 32))
        self.addToolBar(toolbar)
        toolbar.setMovable(False)

        new_action = QAction(QIcon(os.path.join('images', 'ui-tab--plus.png')), "Create new page...", self)
        new_action.setStatusTip("Create new page")
        new_action.triggered.connect(self.new_file)
        toolbar.addAction(new_action)

        open_file_action = QAction(QIcon(os.path.join('images', 'blue-folder-open-document.png')), "Open file...", self)
        open_file_action.setStatusTip("Open file")
        open_file_action.triggered.connect(self.file_open)
        toolbar.addAction(open_file_action)

        save_file_action = QAction(QIcon(os.path.join('images', 'disk.png')), "Save", self)
        save_file_action.setStatusTip("Save current page")
        save_file_action.triggered.connect(self.file_save)
        toolbar.addAction(save_file_action)

        saveas_file_action = QAction(QIcon(os.path.join('images', 'disk--pencil.png')), "Save As...", self)
        saveas_file_action.setStatusTip("Save current page to specified file")
        saveas_file_action.triggered.connect(self.file_saveas)
        toolbar.addAction(saveas_file_action)

        print_action = QAction(QIcon(os.path.join('images', 'printer.png')), "Print...", self)
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect(self.file_print)
        toolbar.addAction(print_action)

        undo_action = QAction(QIcon(os.path.join('images', 'arrow-curve-180-left.png')), "Undo", self)
        undo_action.setStatusTip("Undo last change")
        undo_action.triggered.connect(self.editor.undo)
        toolbar.addAction(undo_action)

        redo_action = QAction(QIcon(os.path.join('images', 'arrow-curve.png')), "Redo", self)
        redo_action.setStatusTip("Redo last change")
        redo_action.triggered.connect(self.editor.redo)
        toolbar.addAction(redo_action)

        cut_action = QAction(QIcon(os.path.join('images', 'scissors.png')), "Cut", self)
        cut_action.setStatusTip("Cut selected text")
        cut_action.triggered.connect(self.editor.cut)
        toolbar.addAction(cut_action)

        copy_action = QAction(QIcon(os.path.join('images', 'document-copy.png')), "Copy", self)
        copy_action.setStatusTip("Copy selected text")
        copy_action.triggered.connect(self.editor.copy)
        toolbar.addAction(copy_action)

        paste_action = QAction(QIcon(os.path.join('images', 'clipboard-paste-document-text.png')), "Paste", self)
        paste_action.setStatusTip("Paste from clipboard")
        paste_action.triggered.connect(self.editor.paste)
        toolbar.addAction(paste_action)

        select_action = QAction(QIcon(os.path.join('images', 'selection-input.png')), "Select all", self)
        select_action.setStatusTip("Select all text")
        select_action.triggered.connect(lambda:self.editor.selectAll())
        toolbar.addAction(select_action)

        wrap_action = QAction(QIcon(os.path.join('images', 'arrow-continue.png')), "Wrap text to window", self)
        wrap_action.setStatusTip("Toggle wrap text to window")
        # wrap_action.setCheckable(True)
        wrap_action.setChecked(True)
        wrap_action.triggered.connect(self.edit_toggle_wrap)
        toolbar.addAction(wrap_action)

        self.update_title()
        self.show()

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def new_file(self):
        self.editor.setText("")
        self.path = None
        self.update_title()

    def file_open(self):
        path, _ = self.filedialog.getOpenFileName(self, "Open file", "", "All files (*.*) ;; Text files (*.txt *.doc *.docx) ;; Code files (*.py *.java *.cpp) ;; Conf files (*.json *.conf *.ini)")
        if path:
            try:
                with open(path, 'rU') as f:
                    text = f.read()

            except Exception as e:
                self.dialog_critical(str(e))

            else:
                self.path = path
                self.editor.setText(text)
                self.update_title()

    def file_save(self):
        if self.path is None:
            # If we do not have a path, we need to use Save As.
            return self.file_saveas()

        self._save_to_path(self.path)

    def file_saveas(self):
        path, _ = self.filedialog.getSaveFileName(self, "Open file", "", "All files (*.*) ;; Text files (*.txt *.doc *.docx) ;; Code files (*.py *.java *.cpp) ;; Conf files (*.json *.conf *.ini)")

        if not path:
            # If dialog is cancelled, will return ''
            return

        self._save_to_path(path)

    def _save_to_path(self, path):
        text = self.editor.text()
        try:
            with open(path, 'w') as f:
                f.write(text)
                self.saved = True

        except Exception as e:
            self.dialog_critical(str(e))

        else:
            self.path = path
            self.update_title()

    def file_print(self):
        dlg = QPrintDialog()
        if dlg.exec_():
            self.editor.print_(dlg.printer())

    def update_title(self):
        self.setWindowTitle("%s - Notepad" % (os.path.basename(self.path) if self.path else "Untitled"))

    def edit_toggle_wrap(self):
        self.editor.setWrapMode(QsciScintilla.WrapCharacter)

    def closeEvent(self, event):
        if not self.saved:
            close = QMessageBox()
            close.setText("Do you want to save before exit?")
            close.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            close = close.exec()

            if close == QMessageBox.Yes:
                event.ignore()
                self.file_save()
                os.system("exit")
            else:
                event.accept()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setApplicationName("Notepad")
    app.setWindowIcon(QIcon("images/logo.png"))

    window = MainWindow()
    app.exec_()