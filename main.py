# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import time
import platform
import subprocess
import threading

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "PyDracula - Modern GUI"
        description = "GestureVox Integration"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_lib.clicked.connect(self.buttonClick)
        widgets.btn_info.clicked.connect(self.buttonClick)
        widgets.btn_exit.clicked.connect(self.buttonClick)
        widgets.Start.clicked.connect(self.buttonClickStart)
        widgets.pushButton_2.clicked.connect(self.buttonClickStart)
        widgets.toggleLeftBox.clicked.connect(self.openCloseLeftBoxMain)
        widgets.extraCloseColumnBtn.clicked.connect(self.openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.new_my_page)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def Buy(self):
        self.close()
    def OpenCV_plus_ultra(self):
        # subprocess.run(["python", "C:/Users/IVNsell/Desktop/IVNsell/Python/Tect_OpenCV_for_project/OpenCV_plus_ultra.py"])
        subprocess.run(["python", "C:/Users/IVNsell/Desktop/IVNsell/Python/GestureVox Integration/Modern_GUI_PyDracula_PySide6_or_PyQt6-master/HierSpeechpp/HierSpeechpp/GestureVoxIntegration.py"])
    def buttonClickStart(self):
        btn = self.sender()
        btnName = btn.objectName()
        threading.Thread(target=self.OpenCV_plus_ultra).start()
        if btnName == "Start":
            print("Start")
        if btnName == "pushButton_2":
            print("pushButton_2")
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        # print(btn)
        btnName = btn.objectName()
        ToggelLeftBox = "toggleLeftBox"
        # SHOW HOME PAGE
        UIFunctions.resetStyle_bottom(self, btnName)
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.new_my_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_lib":
            widgets.stackedWidget.setCurrentWidget(widgets.new_my_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_info":
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            print("Save BTN clicked!")
        if btnName == "btn_exit":
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED   Collor: 64, 255, 182
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            print("Exit BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

        # EXTRA LEFT BOX

    def openCloseLeftBox(self):
        # GET BUTTON CLICKED
        UIFunctions.toggleLeftBox(self, True)
    def openCloseLeftBoxMain(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        # print(btn)
        btnName = btn.objectName()
        togel = self.sender()
        ToggelLeftBox = "toggleLeftBox"
        # ToggelLeftBox = togel.objectName()
        print(btnName)
        print(ToggelLeftBox)
        UIFunctions.resetStyle(self, btnName)
        togel.setStyleSheet(UIFunctions.selectMenu(togel.styleSheet()))
        # togel_style = widgets.toggleLeftBox.styleSheet()

        # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
        UIFunctions.toggleLeftBox(self, True)

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
