from PyQt5.QtCore import QUrl, QSettings
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QStatusBar, QAction, QShortcut, QToolBar, QLabel, QLineEdit, QApplication, QWidget, QCheckBox
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5 import uic
import sys, os, qdarkstyle, globals

globals.cmd("Browser")

#settings
bookmarks = {}
settings = QSettings("Souvlaki42", "Souvlaki Browser")
homepage = settings.value("homepage")
if settings.value("darktheme") == "true":
	darktheme = True
else:
	darktheme = False
if settings.value("linkpreview") == "true":
	linkpreview = True
else:
	linkpreview = False
if settings.value("bookmarks") == "true":
	bookmarkbar = True
else:
	bookmarkbar = False

class Settings(QWidget):
	def __init__(self):
		super(Settings, self).__init__()
		uic.loadUi("settings.ui", self)
		self.hometext = self.findChild(QLineEdit, "hometext")
		self.hometext.setProperty("text", settings.value("homepage"))
		self.darkcheck = self.findChild(QCheckBox, "darkcheck")
		self.darkcheck.setProperty("checked", settings.value("darktheme"))
		self.linkpreviewcheck = self.findChild(QCheckBox, "linkpreviewcheck")
		self.linkpreviewcheck.setProperty("checked", settings.value("linkpreview"))
		self.bookmarkcheck = self.findChild(QCheckBox, "bookmarkcheck")
		self.bookmarkcheck.setProperty("checked", settings.value("bookmarks"))

	def closeEvent(self, event):
		settings.setValue("darktheme", self.darkcheck.property("checked"))
		settings.setValue("homepage", self.hometext.property("text"))
		settings.setValue("linkpreview", self.linkpreviewcheck.property("checked"))
		settings.setValue("bookmarks", self.bookmarkcheck.property("checked"))

class MainWindow(QMainWindow):
	def __init__(self):#, *args, **kwargs):
		super(MainWindow, self).__init__()#*args, **kwargs)

		os.system('cls' if os.name == 'nt' else 'clear')

		self.showMaximized()

		self.tabs = QTabWidget()

		self.tabs.setDocumentMode(True)

		self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

		self.tabs.currentChanged.connect(self.current_tab_changed)

		self.tabs.setTabsClosable(True)

		self.tabs.tabCloseRequested.connect(self.close_current_tab)

		self.setCentralWidget(self.tabs)

		self.status = QStatusBar()

		self.setStatusBar(self.status)

		self.navtb = QToolBar("Navigation")

		self.addToolBar(self.navtb)

		self.addToolBarBreak()

		self.fav = QToolBar("Bookmarks")

		self.addToolBar(self.fav)

		back_btn = QAction(QIcon(os.path.join('images', 'arrow-left.svg')), "Back", self)
		back_btn.setStatusTip("Back to previous page")
		back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
		self.navtb.addAction(back_btn)
		back_short = QShortcut(QKeySequence("Alt+Left"), self)
		back_short.activated.connect(lambda: self.tabs.currentWidget().back())

		next_btn = QAction(QIcon(os.path.join('images', 'arrow-right.svg')), "Forward", self)
		next_btn.setStatusTip("Forward to next page")
		next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
		self.navtb.addAction(next_btn)
		next_short = QShortcut(QKeySequence("Alt+Right"), self)
		next_short.activated.connect(lambda: self.tabs.currentWidget().forward())

		reload_btn = QAction(QIcon(os.path.join('images', 'rotate-right.png')), "Reload", self)
		reload_btn.setStatusTip("Reload page")
		reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
		self.navtb.addAction(reload_btn)
		reload_short = QShortcut(QKeySequence("F5"), self)
		reload_short.activated.connect(lambda: self.tabs.currentWidget().reload())

		stop_btn = QAction(QIcon(os.path.join('images', 'cross.png')), "Stop", self)
		stop_btn.setStatusTip("Stop loading current page")
		stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
		self.navtb.addAction(stop_btn)
		stop_short = QShortcut(QKeySequence("Alt+ESC"), self)
		stop_short.activated.connect(lambda: self.tabs.currentWidget().stop())

		home_btn = QAction(QIcon(os.path.join('images', 'home.png')), "Home", self)
		home_btn.setStatusTip("Go home")
		home_btn.triggered.connect(self.navigate_home)
		self.navtb.addAction(home_btn)
		home_short = QShortcut(QKeySequence("Alt+Home"), self)
		home_short.activated.connect(self.navigate_home)

		self.ssl_btn = QAction()
		self.ssl_btn.setStatusTip("SSL/TLS Info")
		self.ssl_btn.setIcon(QIcon(os.path.join('images', 'unlock.png')))
		self.navtb.addAction(self.ssl_btn)

		empty3_lbl = QLabel("  ",self)
		self.navtb.addWidget(empty3_lbl)

		self.urlbar = QLineEdit()
		self.urlbar.setStyleSheet("QLineEdit { border-radius: 10px;}")

		self.urlbar.returnPressed.connect(self.navigate_to_url)

		self.navtb.addWidget(self.urlbar)

		empty4_lbl = QLabel("  ",self)
		self.navtb.addWidget(empty4_lbl)

		newwindow_btn = QAction(QIcon(os.path.join('images', 'browser.png')), "New Window", self)
		newwindow_btn.setStatusTip("Open new window")
		newwindow_btn.triggered.connect(lambda:MainWindow())
		self.navtb.addAction(newwindow_btn)
		newwindow_short = QShortcut(QKeySequence("Ctrl+N"), self)
		newwindow_short.activated.connect(lambda:MainWindow())

		source_btn = QAction(QIcon(os.path.join('images', 'stats.png')), "Source", self)
		source_btn.setStatusTip("View page source")
		source_btn.triggered.connect(lambda:self.tabs.currentWidget().setUrl(QUrl(source())))
		self.navtb.addAction(source_btn)
		source_short = QShortcut(QKeySequence("Ctrl+U"), self)
		source_short.activated.connect(lambda:self.tabs.currentWidget().setUrl(QUrl(source())))

		clean_btn = QAction(QIcon(os.path.join('images', 'broom.png')), "Cleaner", self)
		clean_btn.setStatusTip("Clean useless browser data")
		clean_btn.triggered.connect(lambda:cleanup())
		self.navtb.addAction(clean_btn)
		clean_short = QShortcut(QKeySequence("Alt+J"), self)
		clean_short.activated.connect(lambda:cleanup())

		settings_btn = QAction(QIcon(os.path.join('images', 'settings.png')), "Settings", self)
		settings_btn.setToolTip("Open browser settings window")
		settings_btn.triggered.connect(lambda:open_settings(self))
		self.navtb.addAction(settings_btn)
		settings_short = QShortcut(QKeySequence("Alt+P"), self)
		settings_short.activated.connect(lambda:open_settings(self))

		newtab_short = QShortcut(QKeySequence("Ctrl+T"), self)
		newtab_short.activated.connect(lambda:self.add_new_tab(QUrl(homepage), 'Homepage'))
		closetab_short = QShortcut(QKeySequence("Ctrl+W"), self)
		closetab_short.activated.connect(lambda:self.close_current_tab(self.tabs.currentIndex()))

		def cleanup():
			os.system('cls' if os.name == 'nt' else 'clear')

		def open_settings(self):
			self.settings = Settings()
			self.settings.show()

		def source():
			source = "view-source:"
			url = str(self.urlbar.text())
			r = source + url
			t = str(r)
			return t

		self.add_new_tab(QUrl(homepage), 'Homepage')

		self.setWindowTitle("Browser")

	def sethome(self, url, homepage):
		homepage = url

	def add_new_tab(self, qurl = None, label = "Blank"):

		if qurl is None:

			qurl = QUrl(homepage)

		browser = QWebEngineView()
		browser.settings().setAttribute(
			QWebEngineSettings.FullScreenSupportEnabled, True
		)
		browser.settings().setAttribute(
			QWebEngineSettings.JavascriptCanOpenWindows, True
		)

		browser.setUrl(qurl)

		i = self.tabs.addTab(browser, label)
		self.tabs.setCurrentIndex(i)
		self.tabs.setTabIcon(i, browser.icon())
		browser.iconChanged.connect(lambda icon, browser=browser: self.update_icon(browser, icon))

		browser.urlChanged.connect(lambda qurl, browser = browser:
								self.update_urlbar(qurl, browser))

		browser.page().profile().downloadRequested.connect(self._downloadRequested)

		# browser.setContextMenuPolicy

		if linkpreview:
			browser.page().linkHovered.connect(self.status.showMessage)

		browser.page().fullScreenRequested.connect(lambda request, browser = browser: self.handle_fullscreen_requested(request))

		browser.loadFinished.connect(lambda _, i = i, browser = browser:
									self.tabs.setTabText(i, browser.page().title()))

	def update_icon(self, browser, icon):
		index = self.tabs.indexOf(browser)
		self.tabs.setTabIcon(index, icon)


	def tab_open_doubleclick(self, i):

		if i == -1:
			self.add_new_tab()

	def closeEvent(self, event):
		os.system('cls' if os.name == 'nt' else 'clear')

	def handle_fullscreen_requested(self, request):
		request.accept()
		if request.toggleOn():
			self.showFullScreen()
			self.statusBar().hide()
			self.navtb.hide()
			self.tabs.tabBar().hide()
		else:
			self.showMaximized()
			self.statusBar().show()
			self.navtb.show()
			self.tabs.tabBar().show()

	def _downloadRequested(self,item):
		item.accept()

	def current_tab_changed(self, i):

		qurl = self.tabs.currentWidget().url()

		self.update_urlbar(qurl, self.tabs.currentWidget())

		self.update_title(self.tabs.currentWidget())

	def close_current_tab(self, i):
		if self.tabs.count() < 2:
			self.close()
			return
		page = self.tabs.widget(i)
		self.tabs.removeTab(i)
		page.deleteLater()

	def update_title(self, browser):

		if browser != self.tabs.currentWidget():
			return

		title = self.tabs.currentWidget().page().title()

	def navigate_home(self):

		self.tabs.currentWidget().setUrl(QUrl(homepage))

	def navigate_to_url(self):

		q = QUrl(self.urlbar.text())

		if q.scheme() == "":

			q.setScheme("http")

		self.tabs.currentWidget().setUrl(q)

	def update_urlbar(self, q, browser = None):

		if browser != self.tabs.currentWidget():

			return

		self.urlbar.setText(q.toString())

		self.urlbar.setCursorPosition(0)

		if q.scheme() == 'https':
			# Secure padlock icon
			self.ssl_btn.setStatusTip("Secure Connection")
			self.ssl_btn.setIcon(QIcon(os.path.join('images', 'lock.png')))

		else:
			# Insecure padlock icon
			self.ssl_btn.setStatusTip("Insecure Connection")
			self.ssl_btn.setIcon(QIcon(os.path.join('images', 'unlock.png')))


app = QApplication(sys.argv)

if darktheme == True:
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
else:
	app.setStyleSheet("")

app.setApplicationName("Browser")

app.setWindowIcon(QIcon("images/logo.png"))

window = MainWindow()
window.show()
app.exec_()