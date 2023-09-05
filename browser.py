import sys
from PySide2 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

# Classes
class Ui_Main(object):
    def setupUi(self, main_window):
        main_window.setObjectName('main_window')
        main_window.resize(640, 480)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName('central_widget')
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setObjectName('grid_layout')
        self.button_back = QtWidgets.QPushButton(self.central_widget)
        self.button_back.setObjectName('button_back')
        self.grid_layout.addWidget(self.button_back, 0, 0, 1, 1)
        self.button_forward = QtWidgets.QPushButton(self.central_widget)
        self.button_forward.setObjectName('button_forward')
        self.grid_layout.addWidget(self.button_forward, 0, 1, 1, 1)
        self.address_bar = QtWidgets.QLineEdit(self.central_widget)
        self.address_bar.setObjectName('address_bar')
        self.grid_layout.addWidget(self.address_bar, 0, 2, 1, 1)
        self.button_reload = QtWidgets.QPushButton(self.central_widget)
        self.button_reload.setObjectName('button_reload')
        self.grid_layout.addWidget(self.button_reload, 0, 3, 1, 1)
        self.button_downloads = QtWidgets.QPushButton(self.central_widget)
        self.button_downloads.setObjectName('button_downloads')
        self.grid_layout.addWidget(self.button_downloads, 0, 4, 1, 1)
        self.button_options = QtWidgets.QPushButton(self.central_widget)
        self.button_options.setObjectName('button_options')
        self.grid_layout.addWidget(self.button_options, 0, 5, 1, 1)
        self.tab_widget = QtWidgets.QTabWidget(self.central_widget)
        self.tab_widget.setObjectName('tab_widget')
        self.tab_widget.setDocumentMode(False)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.grid_layout.addWidget(self.tab_widget, 1, 0, 1, 6)
        main_window.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 17))
        self.menubar.setObjectName('menubar')
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName('menu_file')
        self.menu_edit = QtWidgets.QMenu(self.menubar)
        self.menu_edit.setObjectName('menu_edit')
        self.menu_view = QtWidgets.QMenu(self.menubar)
        self.menu_view.setObjectName('menu_view')
        self.menu_zoom = QtWidgets.QMenu(self.menu_view)
        self.menu_zoom.setObjectName('menu_zoom')
        self.menu_tools = QtWidgets.QMenu(self.menubar)
        self.menu_tools.setObjectName('menu_tools')
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName('statusbar')
        main_window.setStatusBar(self.statusbar)
        self.action_new_tab = QtWidgets.QAction(main_window)
        self.action_new_tab.setObjectName('action_new_tab')
        self.action_open_file = QtWidgets.QAction(main_window)
        self.action_open_file.setObjectName('action_open_file')
        self.action_save_page = QtWidgets.QAction(main_window)
        self.action_save_page.setObjectName('action_save_page')
        self.action_exit = QtWidgets.QAction(main_window)
        self.action_exit.setObjectName('action_exit')
        self.action_undo = QtWidgets.QAction(main_window)
        self.action_undo.setObjectName('action_undo')
        self.action_redo = QtWidgets.QAction(main_window)
        self.action_redo.setObjectName('action_redo')
        self.action_cut = QtWidgets.QAction(main_window)
        self.action_cut.setObjectName('action_cut')
        self.action_copy = QtWidgets.QAction(main_window)
        self.action_copy.setObjectName('action_copy')
        self.action_paste = QtWidgets.QAction(main_window)
        self.action_paste.setObjectName('action_paste')
        self.action_delete = QtWidgets.QAction(main_window)
        self.action_delete.setObjectName('action_delete')
        self.action_select_all = QtWidgets.QAction(main_window)
        self.action_select_all.setObjectName('action_select_all')
        self.action_find = QtWidgets.QAction(main_window)
        self.action_find.setObjectName('action_find')
        self.action_fullscreen = QtWidgets.QAction(main_window)
        self.action_fullscreen.setObjectName('action_fullscreen')
        self.action_zoom_in = QtWidgets.QAction(main_window)
        self.action_zoom_in.setObjectName('action_zoom_in')
        self.action_zoom_out = QtWidgets.QAction(main_window)
        self.action_zoom_out.setObjectName('action_zoom_out')
        self.action_zoom_default = QtWidgets.QAction(main_window)
        self.action_zoom_default.setObjectName('action_zoom_default')
        self.action_downloads = QtWidgets.QAction(main_window)
        self.action_downloads.setObjectName('action_downloads')
        self.action_options = QtWidgets.QAction(main_window)
        self.action_options.setObjectName('action_options')
        self.menu_file.addAction(self.action_new_tab)
        self.menu_file.addAction(self.action_open_file)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_save_page)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menu_edit.addAction(self.action_undo)
        self.menu_edit.addAction(self.action_redo)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.action_cut)
        self.menu_edit.addAction(self.action_copy)
        self.menu_edit.addAction(self.action_paste)
        self.menu_edit.addAction(self.action_delete)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.action_select_all)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.action_find)
        self.menu_zoom.addAction(self.action_zoom_in)
        self.menu_zoom.addAction(self.action_zoom_out)
        self.menu_zoom.addSeparator()
        self.menu_zoom.addAction(self.action_zoom_default)
        self.menu_view.addAction(self.menu_zoom.menuAction())
        self.menu_view.addSeparator()
        self.menu_view.addAction(self.action_fullscreen)
        self.menu_tools.addAction(self.action_downloads)
        self.menu_tools.addSeparator()
        self.menu_tools.addAction(self.action_options)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_tools.menuAction())

        self.retranslateUi(main_window)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate('main_window', 'Pythium'))
        self.button_back.setText(_translate('main_window', 'Back'))
        self.button_forward.setText(_translate('main_window', 'Forward'))
        self.button_reload.setText(_translate('main_window', 'Reload'))
        self.button_downloads.setText(_translate('main_window', 'Downloads'))
        self.button_options.setText(_translate('main_window', 'Options'))
        self.menu_file.setTitle(_translate('main_window', 'File'))
        self.menu_edit.setTitle(_translate('main_window', 'Edit'))
        self.menu_view.setTitle(_translate('main_window', 'View'))
        self.menu_zoom.setTitle(_translate('main_window', 'Zoom'))
        self.menu_tools.setTitle(_translate('main_window', 'Tools'))
        self.action_new_tab.setText(_translate('main_window', 'New Tab'))
        self.action_open_file.setText(_translate('main_window', 'Open File'))
        self.action_save_page.setText(_translate('main_window', 'Save Page As'))
        self.action_exit.setText(_translate('main_window', 'Exit'))
        self.action_undo.setText(_translate('main_window', 'Undo'))
        self.action_redo.setText(_translate('main_window', 'Redo'))
        self.action_cut.setText(_translate('main_window', 'Cut'))
        self.action_copy.setText(_translate('main_window', 'Copy'))
        self.action_paste.setText(_translate('main_window', 'Paste'))
        self.action_delete.setText(_translate('main_window', 'Delete'))
        self.action_select_all.setText(_translate('main_window', 'Select All'))
        self.action_find.setText(_translate('main_window', 'Find In This Page'))
        self.action_fullscreen.setText(_translate('main_window', 'Fullscreen'))
        self.action_zoom_in.setText(_translate('main_window', 'Zoom In'))
        self.action_zoom_out.setText(_translate('main_window', 'Zoom Out'))
        self.action_zoom_default.setText(_translate('main_window', 'Actual Size'))
        self.action_downloads.setText(_translate('main_window', 'Downloads'))
        self.action_options.setText(_translate('main_window', 'Options'))

class Ui_Options(object):
    def setupUi(self, form):
        form.setObjectName('form')
        form.resize(240, 120)
        self.checkbox_javascript = QtWidgets.QCheckBox(form)
        self.checkbox_javascript.setGeometry(QtCore.QRect(70, 20, 72, 18))
        self.checkbox_javascript.setObjectName('checkbox_javascript')
        self.checkbox_cookies = QtWidgets.QCheckBox(form)
        self.checkbox_cookies.setGeometry(QtCore.QRect(70, 50, 72, 18))
        self.checkbox_cookies.setObjectName('checkbox_cookies')
        self.button_apply = QtWidgets.QPushButton(form)
        self.button_apply.setGeometry(QtCore.QRect(70, 80, 72, 18))
        self.button_apply.setObjectName('button_apply')

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate('form', 'Options'))
        self.checkbox_javascript.setText(_translate('form', 'Javascript'))
        self.checkbox_cookies.setText(_translate('form', 'Cookies'))
        self.button_apply.setText(_translate('form', 'Apply'))

class Ui_Confirm(object):
    def setupUi(self, form):
        form.setObjectName('form')
        form.resize(150, 100)
        self.grid_layout = QtWidgets.QGridLayout(form)
        self.grid_layout.setObjectName('grid_layout')
        self.button_ok = QtWidgets.QPushButton(form)
        self.button_ok.setObjectName('button_ok')
        self.grid_layout.addWidget(self.button_ok, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(form)
        self.label.setObjectName('label')
        self.grid_layout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate('form', 'Confirm'))
        self.button_ok.setText(_translate('form', 'OK'))
        self.label.setText(_translate('form', 'Download has finished.'))

class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    def acceptNavigationRequest(self, url,  _type, is_main_frame):
        if _type == QtWebEngineWidgets.QWebEnginePage.NavigationTypeLinkClicked:
            return True
        return super(WebEnginePage, self).acceptNavigationRequest(url, _type, is_main_frame)

class WebEngineView(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, main, *args, **kwargs):
        super(WebEngineView, self).__init__(*args, **kwargs)
        self.setPage(WebEnginePage(self))
        self._windows = main

    def createWindow(self, _type):
        self.blockSignals(not self._windows.pref[0])
        i = self._windows.tab_widget.addTab(self, 'Blank')
        self.urlChanged.connect(lambda: self._windows.update_search(self.url(), browser=self))
        self.loadFinished.connect(lambda: self._windows.tab_widget.setTabText(i, self.page().title()))
        return self

class Main(QtWidgets.QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent=parent)
        self.setupUi(self)
        self.tab_widget.currentChanged.connect(self.tab_changed)
        self.action_new_tab.triggered.connect(lambda: self.new_tab())
        self.action_options.triggered.connect(self.options)
        self.action_open_file.triggered.connect(self.open_file)
        self.action_save_page.triggered.connect(self.save_file)
        self.action_zoom_in.triggered.connect(self.zoom_in)
        self.action_zoom_out.triggered.connect(self.zoom_out)
        self.action_zoom_default.triggered.connect(self.zoom_reset)
        self.action_exit.triggered.connect(self.close)
        self.address_bar.returnPressed.connect(self.search)
        self.button_reload.clicked.connect(lambda: self.button('r'))
        self.button_back.clicked.connect(lambda: self.button('b'))
        self.button_forward.clicked.connect(lambda: self.button('f'))
        self.button_options.clicked.connect(self.options)
        self.pref = (True, True)
        QtWebEngineWidgets.QWebEngineProfile().defaultProfile().setPersistentStoragePath('storage/persistent/')
        QtWebEngineWidgets.QWebEngineProfile().defaultProfile().setCachePath('storage/cache/')
        QtWebEngineWidgets.QWebEngineProfile().defaultProfile().downloadRequested.connect(self.on_download_requested)
        self.load_conf()

    def new_tab(self, url='', label='Blank'):
        browser = WebEngineView(self)
        browser.blockSignals(not self.pref[0])
        surl = QtCore.QUrl(url)
        browser.setUrl(surl)
        i = self.tab_widget.addTab(browser, label)
        self.tab_widget.setCurrentIndex(i)
        browser.urlChanged.connect(lambda: self.update_search(surl, browser))
        browser.loadFinished.connect(lambda: self.tab_widget.setTabText(i, browser.page().title()))

    def tab_changed(self, i):
        try:
            qurl = QtCore.QUrl(self.tab_widget.currentWidget().url())
            self.update_search(qurl, browser=self.tab_widget.currentWidget())
        except AttributeError:
            pass
        
    def search(self):
        surl = QtCore.QUrl(self.address_bar.text())
        if surl.scheme() == '':
            surl.setScheme('http')
        try:
            self.tab_widget.currentWidget().setUrl(surl)
        except AttributeError:
            pass

    def options(self):
        dialog = QtWidgets.QDialog()
        ui = Ui_Options()
        ui.setupUi(dialog)
        ui.button_apply.clicked.connect(lambda: self.value_return(dialog, ui))
        ui.checkbox_javascript.setChecked(self.pref[0])
        ui.checkbox_cookies.setChecked(self.pref[1])
        dialog.exec_()

    def close_tab(self, i):
        try:
            self.tab_widget.widget(i).close()
        except AttributeError:
            pass
        self.tab_widget.removeTab(i)
    
    def value_return(self, dialog, ui):
        js = ui.checkbox_javascript.isChecked()
        ck = ui.checkbox_cookies.isChecked()
        dialog.close()
        self.pref = (js, ck)
        self.load_conf()

    def update_search(self, surl, browser=None):
        if browser != self.tab_widget.currentWidget():
            return
        self.address_bar.setText(browser.url().toString())

    def open_file(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', '', 'Hypertext Markup Language (*.htm *.html)' 'All files (*.*)')
        if filename:
            with open(filename, 'r') as f:
                html = f.read()
            try:
                self.tab_widget.currentWidget().setHtml(html)
                self.address_bar.setText(filename)
            except AttributeError:
                self.new_tab()
                self.tab_widget.currentWidget().setHtml(html)
                self.address_bar.setText(filename)

    def save_file(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Page As', '', 'Hypertext Markup Language (*.htm *html)' 'All files (*.*)')
        if filename:
            html = self.tab_widget.currentWidget().page().toHtml()
            with open(filename, 'w') as f:
                f.write(html.encode('utf8'))

    def on_download_requested(self, download):
        old_path = download.url().path()
        suffix = QtCore.QFileInfo(old_path).suffix()
        path, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', old_path, '*.' + suffix)
        if path:
            download.setPath(path)
            download.accept()
            download.finished.connect(self.on_download_finished)

    def on_download_finished(self):
        dialog = QtWidgets.QDialog()
        ui = Ui_Confirm()
        ui.setupUi(dialog)
        ui.button_ok.clicked.connect(dialog.close)
        dialog.exec_()

    def load_conf(self):
        QtWebEngineWidgets.QWebEngineSettings.defaultSettings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.JavascriptEnabled, not self.pref[0])
        QtWebEngineWidgets.QWebEngineSettings.defaultSettings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.LocalStorageEnabled, self.pref[1])

    def button(self, b):
        try:
            if b == 'r':
                self.tab_widget.currentWidget().reload()
            elif b == 'f':
                self.tab_widget.currentWidget().forward()
            elif b == 'b':
                self.tab_widget.currentWidget().back()
        except AttributeError:
            pass

    def zoom_in(self):
        try:
            self.tab_widget.currentWidget().setZoomFactor(self.tab_widget.currentWidget().zoomFactor() + 0.1)
        except AttributeError:
            pass

    def zoom_out(self):
        try:
            self.tab_widget.currentWidget().setZoomFactor(self.tab_widget.currentWidget().zoomFactor() - 0.1)
        except AttributeError:
            pass

    def zoom_reset(self):
        try:
            self.tab_widget.currentWidget().setZoomFactor(1)
        except AttributeError:
            pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = Main()
    mw.show()
    app.exec_()
