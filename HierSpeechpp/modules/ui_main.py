# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainIAkdkQ.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QScrollBar, QSizePolicy, QSlider,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1108, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setEnabled(True)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(64, 255, 182); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(54, 207, 148);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(54, 207, 148);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "54, 207, 148);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(64, 255, 182)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(64, 255, 182);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(64, 255, 182); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(64, 255, 182);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(64, 255, 182);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(54, 207, 148);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(64, 255, 182);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(64, 255, 182);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(54, 207, 148);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(64, 255, 182);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(64, 255, 182);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(64, 255, 182);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background-image: url(:/images/images/images/Logo.png);")
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setWeight(QFont.Bold)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_lib = QPushButton(self.topMenu)
        self.btn_lib.setObjectName(u"btn_lib")
        sizePolicy.setHeightForWidth(self.btn_lib.sizePolicy().hasHeightForWidth())
        self.btn_lib.setSizePolicy(sizePolicy)
        self.btn_lib.setMinimumSize(QSize(0, 45))
        self.btn_lib.setFont(font)
        self.btn_lib.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lib.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_lib.setStyleSheet(u"background-image: url(:/icons/images/icons/8665118_book_open_icon.png);")

        self.verticalLayout_8.addWidget(self.btn_lib)

        self.btn_info = QPushButton(self.topMenu)
        self.btn_info.setObjectName(u"btn_info")
        sizePolicy.setHeightForWidth(self.btn_info.sizePolicy().hasHeightForWidth())
        self.btn_info.setSizePolicy(sizePolicy)
        self.btn_info.setMinimumSize(QSize(0, 45))
        self.btn_info.setFont(font)
        self.btn_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_info.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_info.setStyleSheet(u"background-image: url(:/icons/images/icons/information_icon.png);\n"
"")

        self.verticalLayout_8.addWidget(self.btn_info)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/hand.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.Shape.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Shadow.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.Info_me = QWidget()
        self.Info_me.setObjectName(u"Info_me")
        self.verticalLayout_23 = QVBoxLayout(self.Info_me)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_37 = QLabel(self.Info_me)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"font: 23pt \"Segoe UI\";")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_37, 0, 0, 1, 1)

        self.label_40 = QLabel(self.Info_me)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(16777215, 35))
        self.label_40.setStyleSheet(u"font: 15pt \"Segoe UI\";")

        self.gridLayout_5.addWidget(self.label_40, 3, 0, 1, 1)

        self.label_42 = QLabel(self.Info_me)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(16777215, 35))
        self.label_42.setStyleSheet(u"font: 15pt \"Segoe UI\";\n"
"")

        self.gridLayout_5.addWidget(self.label_42, 5, 0, 1, 1)

        self.label_44 = QLabel(self.Info_me)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(16777215, 35))
        self.label_44.setStyleSheet(u"font: 15pt \"Segoe UI\";\n"
"")

        self.gridLayout_5.addWidget(self.label_44, 7, 0, 1, 1)

        self.label_38 = QLabel(self.Info_me)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(16777215, 35))
        self.label_38.setStyleSheet(u"font: 15pt \"Segoe UI\";")

        self.gridLayout_5.addWidget(self.label_38, 1, 0, 1, 1)

        self.label_43 = QLabel(self.Info_me)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(0, 250))
        self.label_43.setMaximumSize(QSize(16777215, 500))
        self.label_43.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_5.addWidget(self.label_43, 6, 0, 1, 1)

        self.label_39 = QLabel(self.Info_me)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(16777215, 35))
        self.label_39.setStyleSheet(u"font: 15pt \"Segoe UI\";")

        self.gridLayout_5.addWidget(self.label_39, 2, 0, 1, 1)

        self.label_41 = QLabel(self.Info_me)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(16777215, 35))
        self.label_41.setStyleSheet(u"font: 15pt \"Segoe UI\";")

        self.gridLayout_5.addWidget(self.label_41, 4, 0, 1, 1)

        self.label_45 = QLabel(self.Info_me)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(0, 5))
        self.label_45.setMaximumSize(QSize(16777215, 5))
        self.label_45.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_5.addWidget(self.label_45, 8, 0, 1, 1)


        self.verticalLayout_23.addLayout(self.gridLayout_5)

        self.stackedWidget.addWidget(self.Info_me)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)

        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBoxx = QCheckBox(self.row_2)
        self.checkBoxx.setObjectName(u"checkBoxx")
        self.checkBoxx.setAutoFillBackground(False)
        self.checkBoxx.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBoxx, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 274, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon5)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.new_my_page = QWidget()
        self.new_my_page.setObjectName(u"new_my_page")
        self.gridLayout_3 = QGridLayout(self.new_my_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea_2 = QScrollArea(self.new_my_page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 988, 585))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(450, 11, 331, 31))
        self.label_2.setMaximumSize(QSize(16777215, 40))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(23)
        font5.setBold(False)
        font5.setItalic(False)
        self.label_2.setFont(font5)
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_2.setStyleSheet(u"font: 23pt \"Segoe UI\";")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setMargin(0)
        self.Start = QPushButton(self.frame_2)
        self.Start.setObjectName(u"Start")
        self.Start.setGeometry(QRect(830, 20, 30, 35))
        self.Start.setMinimumSize(QSize(0, 35))
        self.Start.setMaximumSize(QSize(30, 30))
        self.Start.setStyleSheet(u"background-image: url(:/images/images/images/Play.png);\n"
"border: none;")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(860, 20, 71, 31))
        self.pushButton_2.setMaximumSize(QSize(16777215, 40))
        self.pushButton_2.setStyleSheet(u"color: rgb(64, 255, 182);\n"
"font: 18pt \"Comic Sans MS\";\n"
"border: none;")
        self.VideoInstruct = QPushButton(self.frame_2)
        self.VideoInstruct.setObjectName(u"VideoInstruct")
        self.VideoInstruct.setGeometry(QRect(800, 150, 51, 24))
        self.VideoInstruct.setStyleSheet(u"border: none;\n"
"font: 16pt \"Segoe UI\";\n"
"color: rgb(171, 46, 80);")
        self.MoreInformation = QPushButton(self.frame_2)
        self.MoreInformation.setObjectName(u"MoreInformation")
        self.MoreInformation.setGeometry(QRect(800, 190, 161, 24))
        self.MoreInformation.setStyleSheet(u"border: none;\n"
"font: 16pt \"Segoe UI\";\n"
"color: rgb(171, 46, 80);")
        self.Presentation = QPushButton(self.frame_2)
        self.Presentation.setObjectName(u"Presentation")
        self.Presentation.setGeometry(QRect(800, 110, 111, 24))
        self.Presentation.setStyleSheet(u"border: none;\n"
"font: 16pt \"Segoe UI\";\n"
"color: rgb(171, 46, 80);")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-1, 29, 381, 242))
        self.textBrowser_2 = QTextBrowser(self.frame_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(410, 50, 341, 291))
        self.textBrowser_2.setStyleSheet(u"font: 18pt \"Segoe UI\";\n"
"border: none;")

        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_3.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.new_my_page)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_21 = QVBoxLayout(self.new_page)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.scrollArea_7 = QScrollArea(self.new_page)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea_7.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_7.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea_7.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, -757, 980, 1309))
        self.scrollAreaWidgetContents_6.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_23 = QHBoxLayout(self.scrollAreaWidgetContents_6)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_5 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(125, 16777215))
        self.label_5.setStyleSheet(u"font: 15pt \"Segoe UI\";")

        self.horizontalLayout_16.addWidget(self.label_5)

        self.voice_asis = QPushButton(self.scrollAreaWidgetContents_6)
        self.voice_asis.setObjectName(u"voice_asis")
        self.voice_asis.setMaximumSize(QSize(100, 16777215))
        self.voice_asis.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.horizontalLayout_16.addWidget(self.voice_asis)

        self.label_17 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 50))
        self.label_17.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_16.addWidget(self.label_17)


        self.gridLayout_6.addLayout(self.horizontalLayout_16, 2, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.comboBox_new_commands = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_new_commands.addItem("")
        self.comboBox_new_commands.addItem("")
        self.comboBox_new_commands.addItem("")
        self.comboBox_new_commands.setObjectName(u"comboBox_new_commands")
        self.comboBox_new_commands.setStyleSheet(u"font: 13pt \"Segoe UI\";")

        self.gridLayout_8.addWidget(self.comboBox_new_commands, 2, 3, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_47 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"font: 15pt \"Segoe UI\";")

        self.horizontalLayout_14.addWidget(self.label_47)

        self.path_steam_line_edit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.path_steam_line_edit.setObjectName(u"path_steam_line_edit")
        self.path_steam_line_edit.setStyleSheet(u"font: 13pt \"Segoe UI\";")

        self.horizontalLayout_14.addWidget(self.path_steam_line_edit)


        self.gridLayout_8.addLayout(self.horizontalLayout_14, 5, 3, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_12 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font: 15pt \"Segoe UI\";")

        self.horizontalLayout_7.addWidget(self.label_12)

        self.lineEdit_3 = QLineEdit(self.scrollAreaWidgetContents_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"font: 13pt \"Segoe UI\";")

        self.horizontalLayout_7.addWidget(self.lineEdit_3)


        self.gridLayout_8.addLayout(self.horizontalLayout_7, 4, 2, 1, 1)

        self.radioButton_2 = QRadioButton(self.scrollAreaWidgetContents_6)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_8.addWidget(self.radioButton_2, 2, 1, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setStyleSheet(u"font: 15pt \"Segoe UI\";")

        self.gridLayout_8.addWidget(self.label_9, 1, 2, 1, 1)

        self.comboBox_3 = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setStyleSheet(u"font: 13pt \"Segoe UI\";")

        self.gridLayout_8.addWidget(self.comboBox_3, 2, 2, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 15pt \"Segoe UI\";")

        self.gridLayout_8.addWidget(self.label_6, 1, 0, 1, 1)

        self.comboBox_6 = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setStyleSheet(u"font: 13pt \"Segoe UI\";")

        self.gridLayout_8.addWidget(self.comboBox_6, 8, 2, 1, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_8.addWidget(self.label_11, 6, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.comboBox_state_comands = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_state_comands.setObjectName(u"comboBox_state_comands")
        self.comboBox_state_comands.setMaximumSize(QSize(250, 16777215))
        self.comboBox_state_comands.setStyleSheet(u"font: 13pt \"Segoe UI\";")

        self.horizontalLayout_13.addWidget(self.comboBox_state_comands)

        self.label_15 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_13.addWidget(self.label_15)


        self.gridLayout_8.addLayout(self.horizontalLayout_13, 2, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_48 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"font: 15pt \"Segoe UI\";")

        self.horizontalLayout_22.addWidget(self.label_48)

        self.lineEdit_name_new = QLineEdit(self.scrollAreaWidgetContents_6)
        self.lineEdit_name_new.setObjectName(u"lineEdit_name_new")
        self.lineEdit_name_new.setStyleSheet(u"font: 13pt \"Segoe UI\";")

        self.horizontalLayout_22.addWidget(self.lineEdit_name_new)


        self.gridLayout_8.addLayout(self.horizontalLayout_22, 3, 3, 1, 1)

        self.label_35 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_8.addWidget(self.label_35, 0, 0, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_8.addWidget(self.label_7, 1, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_14 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 15pt \"Segoe UI\";")

        self.horizontalLayout_8.addWidget(self.label_14)

        self.content_line_edit = QLineEdit(self.scrollAreaWidgetContents_6)
        self.content_line_edit.setObjectName(u"content_line_edit")
        self.content_line_edit.setStyleSheet(u"font: 13pt \"Segoe UI\";")

        self.horizontalLayout_8.addWidget(self.content_line_edit)


        self.gridLayout_8.addLayout(self.horizontalLayout_8, 4, 3, 1, 1)

        self.label_49 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"font: 15pt \"Segoe UI\";")

        self.gridLayout_8.addWidget(self.label_49, 7, 2, 1, 1)

        self.pushButton_DELETE = QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_DELETE.setObjectName(u"pushButton_DELETE")
        self.pushButton_DELETE.setMinimumSize(QSize(0, 30))

        self.gridLayout_8.addWidget(self.pushButton_DELETE, 9, 2, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 15pt \"Segoe UI\";")

        self.gridLayout_8.addWidget(self.label_13, 1, 3, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 15pt \"Segoe UI\";")

        self.horizontalLayout_6.addWidget(self.label_10)

        self.lineEdit_2 = QLineEdit(self.scrollAreaWidgetContents_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"font: 13pt \"Segoe UI\";")

        self.horizontalLayout_6.addWidget(self.lineEdit_2)


        self.gridLayout_8.addLayout(self.horizontalLayout_6, 3, 2, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_8.addWidget(self.label_8, 3, 1, 1, 1)

        self.checkBoxx_2 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBoxx_2.setObjectName(u"checkBoxx_2")

        self.gridLayout_8.addWidget(self.checkBoxx_2, 3, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 30))
        self.pushButton_3.setMaximumSize(QSize(500, 30))
        self.pushButton_3.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.gridLayout_8.addWidget(self.pushButton_3, 5, 2, 1, 1)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.say_button_new = QPushButton(self.scrollAreaWidgetContents_6)
        self.say_button_new.setObjectName(u"say_button_new")
        self.say_button_new.setMinimumSize(QSize(0, 30))
        self.say_button_new.setMaximumSize(QSize(500, 30))
        self.say_button_new.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.horizontalLayout_26.addWidget(self.say_button_new)

        self.comboBox_4 = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setStyleSheet(u"font: 11pt \"Segoe UI\";")
        self.comboBox_4.setMinimumSize(QSize(65, 0))
        self.comboBox_4.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_26.addWidget(self.comboBox_4)


        self.gridLayout_8.addLayout(self.horizontalLayout_26, 6, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_8, 4, 0, 1, 1)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_21 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 50))
        self.label_21.setStyleSheet(u"font: 23pt \"Segoe UI\";")

        self.gridLayout_9.addWidget(self.label_21, 0, 1, 1, 1)

        self.label_18 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(500, 50))
        self.label_18.setStyleSheet(u"font: 23pt \"Segoe UI\";")

        self.gridLayout_9.addWidget(self.label_18, 0, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")

        self.gridLayout_9.addLayout(self.horizontalLayout_18, 3, 0, 1, 1)

        self.comboBox_music = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_music.setObjectName(u"comboBox_music")
        self.comboBox_music.setMinimumSize(QSize(0, 35))
        self.comboBox_music.setMaximumSize(QSize(215, 30))
        self.comboBox_music.setStyleSheet(u"font: 15pt \"Segoe UI\";")

        self.gridLayout_9.addWidget(self.comboBox_music, 1, 1, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_34 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.horizontalLayout_24.addWidget(self.label_34)


        self.gridLayout_9.addLayout(self.horizontalLayout_24, 0, 2, 1, 1)

        self.default_settings = QPushButton(self.scrollAreaWidgetContents_6)
        self.default_settings.setObjectName(u"default_settings")
        self.default_settings.setMaximumSize(QSize(200, 40))
        self.default_settings.setStyleSheet(u"font: 18pt \"Segoe UI\";")

        self.gridLayout_9.addWidget(self.default_settings, 5, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_19 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(175, 24))
        self.label_19.setStyleSheet(u"font: 15pt \"Segoe UI\";")

        self.horizontalLayout_17.addWidget(self.label_19)

        self.lineEdit_5 = QLineEdit(self.scrollAreaWidgetContents_6)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(150, 24))
        self.lineEdit_5.setStyleSheet(u"font: 13pt \"Segoe UI\";")

        self.horizontalLayout_17.addWidget(self.lineEdit_5)

        self.label_20 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 25))
        self.label_20.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_17.addWidget(self.label_20)


        self.gridLayout_9.addLayout(self.horizontalLayout_17, 1, 0, 1, 1)

        self.label_55 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_9.addWidget(self.label_55, 4, 0, 1, 1)


        self.verticalLayout_24.addLayout(self.gridLayout_9)


        self.gridLayout_6.addLayout(self.verticalLayout_24, 5, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents_6)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 80))
        self.label.setStyleSheet(u"font: 23pt \"Segoe UI\";")

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_4 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(130, 16777215))
        self.label_4.setStyleSheet(u"font: 15pt \"Segoe UI\";")

        self.horizontalLayout_15.addWidget(self.label_4)

        self.chose_asistent_name = QPushButton(self.scrollAreaWidgetContents_6)
        self.chose_asistent_name.setObjectName(u"chose_asistent_name")
        self.chose_asistent_name.setMaximumSize(QSize(130, 16777215))
        self.chose_asistent_name.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.horizontalLayout_15.addWidget(self.chose_asistent_name)

        self.label_16 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 50))
        self.label_16.setMaximumSize(QSize(10, 50))

        self.horizontalLayout_15.addWidget(self.label_16)

        self.comboBox_2 = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(65, 0))
        self.comboBox_2.setMaximumSize(QSize(30, 16777215))
        self.comboBox_2.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.horizontalLayout_15.addWidget(self.comboBox_2)

        self.label_56 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_15.addWidget(self.label_56)


        self.gridLayout_6.addLayout(self.horizontalLayout_15, 1, 0, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.checkBox_11 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.gridLayout_11.addWidget(self.checkBox_11, 6, 4, 1, 1)

        self.checkBox_10 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout_11.addWidget(self.checkBox_10, 6, 2, 1, 1)

        self.checkBox_9 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout_11.addWidget(self.checkBox_9, 6, 0, 1, 1)

        self.label_30 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_11.addWidget(self.label_30, 5, 3, 1, 1)

        self.checkBox_3 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_11.addWidget(self.checkBox_3, 2, 4, 1, 1)

        self.Gesture_7 = QLabel(self.scrollAreaWidgetContents_6)
        self.Gesture_7.setObjectName(u"Gesture_7")
        self.Gesture_7.setMinimumSize(QSize(0, 160))
        self.Gesture_7.setMaximumSize(QSize(215, 300))
        self.Gesture_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.Gesture_7, 3, 4, 1, 1)

        self.Gesture_8 = QLabel(self.scrollAreaWidgetContents_6)
        self.Gesture_8.setObjectName(u"Gesture_8")
        self.Gesture_8.setMinimumSize(QSize(0, 160))
        self.Gesture_8.setMaximumSize(QSize(215, 300))
        self.Gesture_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.Gesture_8, 3, 6, 1, 1)

        self.Gesture_1 = QLabel(self.scrollAreaWidgetContents_6)
        self.Gesture_1.setObjectName(u"Gesture_1")
        self.Gesture_1.setMinimumSize(QSize(0, 160))
        self.Gesture_1.setMaximumSize(QSize(215, 160))
        self.Gesture_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.Gesture_1, 1, 0, 1, 1)

        self.checkBox_12 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.gridLayout_11.addWidget(self.checkBox_12, 6, 6, 1, 1)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(5, 50))
        self.label_25.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_11.addWidget(self.label_25, 1, 3, 1, 1)

        self.label_29 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_11.addWidget(self.label_29, 3, 5, 1, 1)

        self.Gesture_12 = QLabel(self.scrollAreaWidgetContents_6)
        self.Gesture_12.setObjectName(u"Gesture_12")
        self.Gesture_12.setMinimumSize(QSize(0, 160))
        self.Gesture_12.setMaximumSize(QSize(215, 300))
        self.Gesture_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.Gesture_12, 5, 6, 1, 1)

        self.Gesture_6 = QLabel(self.scrollAreaWidgetContents_6)
        self.Gesture_6.setObjectName(u"Gesture_6")
        self.Gesture_6.setMinimumSize(QSize(0, 160))
        self.Gesture_6.setMaximumSize(QSize(215, 300))
        self.Gesture_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.Gesture_6, 3, 2, 1, 1)

        self.checkBox_1 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_1.setObjectName(u"checkBox_1")

        self.gridLayout_11.addWidget(self.checkBox_1, 2, 0, 1, 1)

        self.Gesture_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.Gesture_2.setObjectName(u"Gesture_2")
        self.Gesture_2.setMinimumSize(QSize(0, 160))
        self.Gesture_2.setMaximumSize(QSize(215, 16777215))
        self.Gesture_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.Gesture_2, 1, 2, 1, 1)

        self.checkBox_6 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_11.addWidget(self.checkBox_6, 4, 2, 1, 1)

        self.Gesture_9 = QLabel(self.scrollAreaWidgetContents_6)
        self.Gesture_9.setObjectName(u"Gesture_9")
        self.Gesture_9.setMinimumSize(QSize(0, 160))
        self.Gesture_9.setMaximumSize(QSize(215, 300))
        self.Gesture_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.Gesture_9, 5, 0, 1, 1)

        self.checkBox_7 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout_11.addWidget(self.checkBox_7, 4, 4, 1, 1)

        self.checkBox_5 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_11.addWidget(self.checkBox_5, 4, 0, 1, 1)

        self.Gesture_5 = QLabel(self.scrollAreaWidgetContents_6)
        self.Gesture_5.setObjectName(u"Gesture_5")
        self.Gesture_5.setMinimumSize(QSize(0, 160))
        self.Gesture_5.setMaximumSize(QSize(215, 300))
        self.Gesture_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.Gesture_5, 3, 0, 1, 1)

        self.Gesture_4 = QLabel(self.scrollAreaWidgetContents_6)
        self.Gesture_4.setObjectName(u"Gesture_4")
        self.Gesture_4.setMinimumSize(QSize(0, 160))
        self.Gesture_4.setMaximumSize(QSize(215, 16777215))
        self.Gesture_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.Gesture_4, 1, 6, 1, 1)

        self.label_27 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_11.addWidget(self.label_27, 3, 1, 1, 1)

        self.Gesture_3 = QLabel(self.scrollAreaWidgetContents_6)
        self.Gesture_3.setObjectName(u"Gesture_3")
        self.Gesture_3.setMinimumSize(QSize(0, 160))
        self.Gesture_3.setMaximumSize(QSize(215, 16777215))
        self.Gesture_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.Gesture_3, 1, 4, 1, 1)

        self.Gesture_11 = QLabel(self.scrollAreaWidgetContents_6)
        self.Gesture_11.setObjectName(u"Gesture_11")
        self.Gesture_11.setMinimumSize(QSize(0, 160))
        self.Gesture_11.setMaximumSize(QSize(215, 300))
        self.Gesture_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.Gesture_11, 5, 4, 1, 1)

        self.checkBox_8 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout_11.addWidget(self.checkBox_8, 4, 6, 1, 1)

        self.Gesture_10 = QLabel(self.scrollAreaWidgetContents_6)
        self.Gesture_10.setObjectName(u"Gesture_10")
        self.Gesture_10.setMinimumSize(QSize(0, 160))
        self.Gesture_10.setMaximumSize(QSize(215, 300))
        self.Gesture_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.Gesture_10, 5, 2, 1, 1)

        self.checkBox_2 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_11.addWidget(self.checkBox_2, 2, 2, 1, 1)

        self.label_26 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(5, 50))
        self.label_26.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_11.addWidget(self.label_26, 1, 5, 1, 1)

        self.checkBox_4 = QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_11.addWidget(self.checkBox_4, 2, 6, 1, 1)

        self.label_28 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_11.addWidget(self.label_28, 3, 3, 1, 1)

        self.label_24 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(5, 50))
        self.label_24.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_11.addWidget(self.label_24, 1, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_11, 3, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")

        self.horizontalLayout_20.addLayout(self.gridLayout_10)


        self.verticalLayout_4.addLayout(self.horizontalLayout_20)


        self.gridLayout_6.addLayout(self.verticalLayout_4, 6, 0, 1, 1)


        self.verticalLayout_20.addLayout(self.gridLayout_6)


        self.horizontalLayout_23.addLayout(self.verticalLayout_20)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_21.addWidget(self.scrollArea_7)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")

        self.verticalLayout_21.addLayout(self.verticalLayout_22)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_23 = QLabel(self.new_page)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_19.addWidget(self.label_23)


        self.verticalLayout_21.addLayout(self.horizontalLayout_19)

        self.stackedWidget.addWidget(self.new_page)
        self.thanks_page = QWidget()
        self.thanks_page.setObjectName(u"thanks_page")
        self.verticalLayout_27 = QVBoxLayout(self.thanks_page)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_46 = QLabel(self.thanks_page)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(0, 50))
        self.label_46.setMaximumSize(QSize(16777215, 40))
        self.label_46.setStyleSheet(u"font: 23pt \"Segoe UI\";\n"
"")
        self.label_46.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label_46, 0, 0, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_52 = QLabel(self.thanks_page)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_12.addWidget(self.label_52, 2, 2, 1, 1)

        self.Name_3 = QLabel(self.thanks_page)
        self.Name_3.setObjectName(u"Name_3")
        self.Name_3.setMaximumSize(QSize(16777215, 35))
        self.Name_3.setStyleSheet(u"font: 15pt \"Segoe UI\";\n"
"")

        self.gridLayout_12.addWidget(self.Name_3, 3, 0, 1, 1)

        self.label_51 = QLabel(self.thanks_page)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_12.addWidget(self.label_51, 1, 2, 1, 1)

        self.Name_2 = QLabel(self.thanks_page)
        self.Name_2.setObjectName(u"Name_2")
        self.Name_2.setMaximumSize(QSize(16777215, 35))
        self.Name_2.setStyleSheet(u"font: 15pt \"Segoe UI\";\n"
"")

        self.gridLayout_12.addWidget(self.Name_2, 2, 0, 1, 1)

        self.Link_3 = QPushButton(self.thanks_page)
        self.Link_3.setObjectName(u"Link_3")
        self.Link_3.setStyleSheet(u"border: none;\n"
"font: 15pt \"Segoe UI\";color: rgb(171, 46, 80);")

        self.gridLayout_12.addWidget(self.Link_3, 3, 1, 1, 1)

        self.label_50 = QLabel(self.thanks_page)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_12.addWidget(self.label_50, 4, 0, 1, 1)

        self.Name_1 = QLabel(self.thanks_page)
        self.Name_1.setObjectName(u"Name_1")
        self.Name_1.setMaximumSize(QSize(16777215, 35))
        self.Name_1.setStyleSheet(u"font: 15pt \"Segoe UI\";\n"
"")

        self.gridLayout_12.addWidget(self.Name_1, 1, 0, 1, 1)

        self.label_53 = QLabel(self.thanks_page)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_12.addWidget(self.label_53, 3, 2, 1, 1)

        self.Link_1 = QPushButton(self.thanks_page)
        self.Link_1.setObjectName(u"Link_1")
        self.Link_1.setStyleSheet(u"border: none;\n"
"font: 15pt \"Segoe UI\";\n"
"color: rgb(171, 46, 80);")

        self.gridLayout_12.addWidget(self.Link_1, 1, 1, 1, 1)

        self.Link_2 = QPushButton(self.thanks_page)
        self.Link_2.setObjectName(u"Link_2")
        self.Link_2.setStyleSheet(u"border: none;\n"
"font: 15pt \"Segoe UI\";color: rgb(171, 46, 80);")

        self.gridLayout_12.addWidget(self.Link_2, 2, 1, 1, 1)

        self.label_54 = QLabel(self.thanks_page)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(16777215, 10))
        self.label_54.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_12.addWidget(self.label_54, 0, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_12, 1, 0, 1, 1)


        self.verticalLayout_27.addLayout(self.gridLayout_7)

        self.stackedWidget.addWidget(self.thanks_page)
        self.Instruction = QWidget()
        self.Instruction.setObjectName(u"Instruction")
        self.verticalLayout_25 = QVBoxLayout(self.Instruction)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_22 = QLabel(self.Instruction)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 30))
        self.label_22.setMaximumSize(QSize(16777215, 50))
        self.label_22.setStyleSheet(u"font: 23pt \"Segoe UI\";")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_22)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_31 = QLabel(self.Instruction)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 300))
        self.label_31.setMaximumSize(QSize(16777215, 300))
        self.label_31.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.horizontalLayout_10.addWidget(self.label_31)

        self.widgetInstruction = QWidget(self.Instruction)
        self.widgetInstruction.setObjectName(u"widgetInstruction")
        self.widgetInstruction.setMinimumSize(QSize(613, 345))
        self.widgetInstruction.setMaximumSize(QSize(825, 393))

        self.horizontalLayout_10.addWidget(self.widgetInstruction)

        self.label_32 = QLabel(self.Instruction)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")

        self.horizontalLayout_10.addWidget(self.label_32)


        self.verticalLayout_25.addLayout(self.horizontalLayout_10)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_33 = QLabel(self.Instruction)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.horizontalLayout_25.addWidget(self.label_33)

        self.pushButton_left = QPushButton(self.Instruction)
        self.pushButton_left.setObjectName(u"pushButton_left")
        self.pushButton_left.setMaximumSize(QSize(32, 32))
        self.pushButton_left.setStyleSheet(u"border: none;\n"
"background-image: url(:/icons/images/icons/play_back_icon.png);\n"
"")

        self.horizontalLayout_25.addWidget(self.pushButton_left)

        self.pushButton_play = QPushButton(self.Instruction)
        self.pushButton_play.setObjectName(u"pushButton_play")
        self.pushButton_play.setMinimumSize(QSize(0, 32))
        self.pushButton_play.setMaximumSize(QSize(32, 32))
        self.pushButton_play.setStyleSheet(u"border: none;\n"
"background-image: url(:/icons/images/icons/play_game_music_icon.png);")

        self.horizontalLayout_25.addWidget(self.pushButton_play)

        self.pushButton_right = QPushButton(self.Instruction)
        self.pushButton_right.setObjectName(u"pushButton_right")
        self.pushButton_right.setMaximumSize(QSize(32, 32))
        self.pushButton_right.setStyleSheet(u"border: none;\n"
"background-image: url(:/icons/images/icons/play_forward_icon.png);")

        self.horizontalLayout_25.addWidget(self.pushButton_right)

        self.label_36 = QLabel(self.Instruction)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")

        self.horizontalLayout_25.addWidget(self.label_36)


        self.verticalLayout_29.addLayout(self.horizontalLayout_25)


        self.verticalLayout_25.addLayout(self.verticalLayout_29)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.scrollArea_5 = QScrollArea(self.Instruction)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setMaximumSize(QSize(16777215, 300))
        self.scrollArea_5.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea_5.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_5.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea_5.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 978, 513))
        self.scrollAreaWidgetContents_7.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_21 = QHBoxLayout(self.scrollAreaWidgetContents_7)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.textBrowser = QTextBrowser(self.scrollAreaWidgetContents_7)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(0, 495))
        self.textBrowser.setStyleSheet(u"font: 15pt \"Segoe UI\";\n"
"border: none;")

        self.horizontalLayout_21.addWidget(self.textBrowser)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_26.addWidget(self.scrollArea_5)


        self.verticalLayout_25.addLayout(self.verticalLayout_26)

        self.stackedWidget.addWidget(self.Instruction)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setBold(False)
        font6.setItalic(False)
        self.creditsLabel.setFont(font6)
        self.creditsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_lib.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_info.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zen"
                        "o Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"GestureVox Integration", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"About me", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"most mashatelnye projects at the moment.", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"programming (not only for this project) contact me through my e-mail.", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"   My e-mail: IVNsell13@gmail.com", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u" My name is Ivan Gaidarov.", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"I am a student of the 10th grade. I narivatisya programmer and this is one of my", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"If you have any questions about my project or you want to talk to me about ", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.checkBoxx.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"GestureVox Integration ", None))
#if QT_CONFIG(accessibility)
        self.Start.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.Start.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.VideoInstruct.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.MoreInformation.setText(QCoreApplication.translate("MainWindow", u"More information", None))
        self.Presentation.setText(QCoreApplication.translate("MainWindow", u"Presentaion", None))
        self.label_3.setText("")
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This program enables computer control using hand gestures and voice commands. Customize your assistant's voice, name, commands, and more with GestureVox Integration.</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Voice asistent ", None))
        self.voice_asis.setText(QCoreApplication.translate("MainWindow", u"Voice", None))
        self.label_17.setText("")
        self.comboBox_new_commands.setItemText(0, QCoreApplication.translate("MainWindow", u"Program", None))
        self.comboBox_new_commands.setItemText(1, QCoreApplication.translate("MainWindow", u"Site", None))
        self.comboBox_new_commands.setItemText(2, QCoreApplication.translate("MainWindow", u"Game", None))

        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Path Steam Game", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.radioButton_2.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Commands", None))
        self.label_11.setText("")
        self.label_15.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_35.setText("")
        self.label_7.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Dell command", None))
        self.pushButton_DELETE.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"New commands", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.label_8.setText("")
        self.checkBoxx_2.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.say_button_new.setText(QCoreApplication.translate("MainWindow", u"Say", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_4.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_4.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_4.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_4.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

        self.label_21.setText(QCoreApplication.translate("MainWindow", u"  Music", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"   Ghat-GPT", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"fasdfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", None))
        self.default_settings.setText(QCoreApplication.translate("MainWindow", u"Default Settings", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Chat-GPT accesses:", None))
        self.label_20.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"   Settings", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Asistent name", None))
        self.chose_asistent_name.setText(QCoreApplication.translate("MainWindow", u"Chose Name", None))
        self.label_16.setText("")
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

        self.label_56.setText("")
        self.checkBox_11.setText("")
        self.checkBox_10.setText("")
        self.checkBox_9.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.checkBox_3.setText("")
        self.Gesture_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Gesture_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Gesture_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.checkBox_12.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Gesture_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Gesture_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.checkBox_1.setText("")
        self.Gesture_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.checkBox_6.setText("")
        self.Gesture_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.checkBox_7.setText("")
        self.checkBox_5.setText("")
        self.Gesture_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Gesture_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Gesture_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Gesture_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.checkBox_8.setText("")
        self.Gesture_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.checkBox_2.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.checkBox_4.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_23.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Thanks these people", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Name_3.setText(QCoreApplication.translate("MainWindow", u"trungkienbkhn ", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Name_2.setText(QCoreApplication.translate("MainWindow", u"Wanderson M. Pimenta", None))
        self.Link_3.setText(QCoreApplication.translate("MainWindow", u"https://github.com/trungkienbkhn", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Name_1.setText(QCoreApplication.translate("MainWindow", u"sh-lee-prml", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Link_1.setText(QCoreApplication.translate("MainWindow", u"https://github.com/sh-lee-prml", None))
        self.Link_2.setText(QCoreApplication.translate("MainWindow", u"https://github.com/Wanderson-Magalhaes", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Instruction", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_left.setText("")
        self.pushButton_play.setText("")
        self.pushButton_right.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\"> To change the voice of your assistant in the program, press the Chose Name button and then wait for a beep, then say the name of your assistant three times in a row for more accuracy.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\"> To change the v"
                        "oice of your assistant press the Voice button and then select the voice file .mp3, preferably it should last about 2-3 seconds.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\"> You can also disable and enable commands, if there is a check mark next to a command then it is active.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\"> You can change modes if the command has it, under the line with the command there is a circle by default it is colored, but you can change it by clicking on it you will change the modes of the command.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\"> In the Edit tab you can select a team and edit its path and name.</span></p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\"> In the New commands tab you can select the path to the game or to the site and then in the Content field write the path to the game or to the site (programs are usually stored in .exe).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\"> You can also change the way Chat-GPT addresses you, for example you can ask it to address you as a helper, manager, character from the game and so on.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\"> You can view a list of music in the Music tab.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span styl"
                        "e=\" font-size:16pt;\"> If you want to return all settings to their original state, click on the Default Settings button.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Ivan Gaydarov", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

