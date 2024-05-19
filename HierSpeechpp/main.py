"""
C struct definitions credit
Author: Wanderson M. Pimenta  (https://github.com/Wanderson-Magalhaes)
Source: https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6
"""
import sys
import os
import time
# from numba import jit
# import platform
# import Name_asis_change
import shutil
from rapidfuzz import fuzz
import subprocess
import File_to_name_list
from subprocess import Popen, PIPE
# import New_Commands_Voice_EDV
# import threading
# from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
# from PySide6.QtGui import QPixmap
# from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget
# from PySide6.QtCore import QTimer
# from PySide6.QtCore import QUrl
# from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimedia import QMediaPlayer , QAudioOutput
import ctypes
import threading
import json
from PySide6.QtMultimediaWidgets import QVideoWidget
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////

from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

with open('settings.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

VK_SPACE = 0x20
# Вызываем функцию для нажатия комбинации клавиш Win + E
def space_tup():
    time.sleep(0.33)
    ctypes.windll.user32.keybd_event(VK_SPACE, 0, 0, 0)
    ctypes.windll.user32.keybd_event(VK_SPACE, 0, 2, 0)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(1108, 720)
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
        widgets.Presentation.clicked.connect(self.openWebsitepresent)
        widgets.VideoInstruct.clicked.connect(self.vieoInstruct)
        widgets.MoreInformation.clicked.connect(self.openWebsitetroll)
        widgets.voice_asis.clicked.connect(self.select_and_move_file)
        widgets.chose_asistent_name.clicked.connect(lambda: self.chose_name_default_thre(True))
        widgets.lineEdit_5.returnPressed.connect(self.on_return_pressed)
        widgets.default_settings.clicked.connect(lambda: self.chose_name_default_thre(False))
        widgets.say_button_new.clicked.connect(self.say_button_func)
        widgets.pushButton_DELETE.clicked.connect(self.dell_button_push)
        widgets.pushButton_3.clicked.connect(self.edit_button_push)
        widgets.Link_1.clicked.connect(lambda: self.linksenc("https://github.com/sh-lee-prml"))
        widgets.Link_2.clicked.connect(lambda: self.linksenc("https://github.com/Wanderson-Magalhaes"))
        widgets.Link_3.clicked.connect(lambda: self.linksenc("https://github.com/trungkienbkhn"))
        self.ui.comboBox_2.setCurrentIndex(int(data["Name_number"]) - 1)
        self.ui.comboBox_4.setCurrentIndex(int(data["Say_number"]) - 1)
        # self.ui.comboBox_music.activated.connect(self.addMusicGrag)
        # self.ui.comboBox_music.activated.connect(self.addMusicGrag)
        self.ui.comboBox_music.enterEvent = self.addMusicGrag
        # self.ui.comboBox_music.currentIndexChanged.connect(self.addMusicGrag)
        # self.ui.comboBox_music.activateWindow()
        # widgets.content_line_edit.returnPressed.connect()
        # widgets.path_steam_line_edit.returnPressed.connect()


        folder_path_musci_list = r"C:\Users\IVNsell\Desktop\IVNsell\Python\GestureVox Integration\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\HierSpeechpp\HierSpeechpp\playlist"

        files_music_mp3 = os.listdir(folder_path_musci_list)
        # Выводим имена файлов с расширением .mp3 (без расширения)
        mp3_files_music_list = [file[:-4] for file in files_music_mp3 if file.lower().endswith('.mp3')]
        print(mp3_files_music_list)
        # Выводим имена файлов
        # for mp3_file_mus in mp3_files_music_list:
        #     print(mp3_file_mus)

        # new_items = ["Элемент 1", "Элемент 2", "Элемент 3"]
        self.ui.comboBox_music.addItems(mp3_files_music_list)
        # for i in range(self.ui.comboBox_music.count()):
        #     print(self.ui.comboBox_music.itemText(i))
        file_name_list = File_to_name_list.open_tu_name()
        self.ui.comboBox_6.addItems(file_name_list)
        self.ui.comboBox_3.addItems(file_name_list)
        commands_list = []
        for i in range(0, 13):  # Перебираем номера команд с 1 до 12
            command_key = f"Command_{i}"
            command_value = data.get(command_key, "")
            if command_value:
                commands_list.append(command_value)

        # Добавление списка команд в QComboBox
        self.ui.comboBox_state_comands.addItems(commands_list)
        self.ui.comboBox_state_comands.addItems(file_name_list)
        box_2_text = self.ui.comboBox_state_comands.currentText()
        if box_2_text == "Time (current / comp)":
            checkbox_box2_value = data["Command_0_activate"].lower() == 'true'
            self.ui.checkBoxx_2.setChecked(checkbox_box2_value)
            radio_box2_value = data["Command_0_mode"].lower() == 'true'
            self.ui.radioButton_2.setChecked(radio_box2_value)
        self.ui.comboBox_state_comands.currentIndexChanged.connect(self.on_combobox_changed)
        self.ui.checkBoxx_2.stateChanged.connect(self.checkBoxCommands_activate)
        self.ui.radioButton_2.toggled.connect(self.checkBoxCommands_mode)
        # Создание списка self.checkBoxes, содержащего ссылки на чекбоксы checkBox_1 до checkBox_10
        # for i in range(3, 13):  # Начиная с 3 и до 12 (включительно)
        #     checkbox_name = f"checkBox_{i}"
        #     checkbox = getattr(self.ui, checkbox_name)
        #     checkbox.setChecked(True)  # Устанавливаем галочку (включено) для текущего чекбокса
        for key in data:
            if key.startswith('Gesture_'):
                # Извлечение номера чекбокса из ключа (например, из 'Gesture_1' получаем '1')
                gesture_number = key.split('_')[1]
                checkbox_name = f'checkBox_{gesture_number}'

                # Получение ссылки на соответствующий чекбокс из интерфейса
                checkbox = getattr(self.ui, checkbox_name, None)

                if checkbox is not None:
                    # Преобразование значения из JSON в булево
                    checkbox_value = data[key].lower() == 'true'
                    # Установка значения чекбокса
                    checkbox.setChecked(checkbox_value)
        # self.browser = QWebEngineView(self.ui.widget)
        # self.browser = QWebEngineView(self.ui.widget)
        # # self.setCentralWidget(self.ui.widget)
        # self.browser.setUrl(QUrl("https://www.youtube.com/embed/69v-9IuRt9M?autoplay=1&controls=0"))
        # self.browser.resize(self.ui.widget.size())
        # # self.browser.move(100, 50)
        # self.browser.show()
        self.checkBoxes = [getattr(self.ui, f"checkBox_{i}") for i in range(1, 13)]

        # Подключение события изменения состояния чекбоксов к методу checkBoxStateChanged
        for checkbox in self.checkBoxes:
            checkbox.stateChanged.connect(self.checkBoxStateChanged)

        #
        # central_widget = QWidget(self.ui.widget)
        # # self.setCentralWidget(central_widget)
        #
        # layout = QVBoxLayout(central_widget)
        # self.web_view = QWebEngineView()
        # layout.addWidget(self.web_view)
        #
        # video_url = "https://www.youtube.com/embed/69v-9IuRt9M?autoplay=1&controls=0"
        # embed_code = f"<iframe width='560' height='315' src='{video_url}' frameborder='0' allowfullscreen></iframe>"
        # self.web_view.setHtml(embed_code)

        # Виджет видео
        self.videoWidget = QVideoWidget(self.ui.widgetInstruction)

        # Настройка медиаплеера
        self.mediaPlayer = QMediaPlayer(self)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.videoWidget.resize(self.ui.widgetInstruction.size())

        # Настройка аудиовыхода
        self.audioOutput = QAudioOutput(self)
        self.mediaPlayer.setAudioOutput(self.audioOutput)

        # Установите путь к вашему видеофайлу здесь
        self.mediaPlayer.setSource(QUrl.fromLocalFile(r"C:\Users\IVNsell\Desktop\IMG_0953.avi"))

        # Связывание кнопок с функциями
        widgets.pushButton_play.clicked.connect(self.togglePlayPause)
        widgets.pushButton_left.clicked.connect(lambda: self.skipVideo(-5))
        widgets.pushButton_right.clicked.connect(lambda: self.skipVideo(5))

        # Макет для видео
        self.videoLayout = QVBoxLayout(self)
        self.videoLayout.addWidget(self.videoWidget)

        def togglePlayPauseOne():
            self.mediaPlayer.play()
            self.mediaPlayer.pause()

        togglePlayPauseOne()
        #
        #
        # # Кнопка воспроизведения
        #
        # # Установка макета
        self.setLayout(self.videoLayout)
        self.videoWidget.setStyleSheet(u"background-color: transparent;")
        # self.videoWidget.resize(self.ui.widget.size())
        pix = QPixmap(r'C:\Users\IVNsell\OneDrive\Рабочий стол\Presentation\probone.jpg')

        # Получение размеров виджета, в котором будет отображаться изображение
        w = self.ui.label_3.width()
        h = self.ui.label_3.height()

        # Установка масштабированного изображения в QLabel
        self.ui.label_3.setPixmap(pix.scaled(w, h, Qt.KeepAspectRatio))


        # Получение размеров виджета, в котором будет отображаться изображение
        w = self.ui.Gesture_1.maximumWidth()
        h = self.ui.Gesture_1.maximumHeight()

        # Установка масштабированного изображения в QLabel
        for i in range(1, 13):
            base_path = fr'C:\\Users\\IVNsell\\OneDrive\\Рабочий стол\\Presentation\\New_Foto_Gesture\\Gesture_{i}.png'
            label_name = getattr(self.ui, f'Gesture_{i}')
            image_path = base_path.format(i)  # Форматируем путь к изображению
            pixmap = QPixmap(image_path)
            label_name.setPixmap(pixmap.scaled(w, h, Qt.KeepAspectRatio))




        # TOGGLE MENU  371   181
        # ///////////////////////////////////////////////////////////////
        # widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
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
        # widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_lib.clicked.connect(self.buttonClick)
        widgets.btn_info.clicked.connect(self.buttonClick)
        widgets.btn_exit.clicked.connect(self.buttonClick)
        widgets.Start.clicked.connect(self.buttonClickStart)
        widgets.pushButton_2.clicked.connect(self.buttonClickStart)
        widgets.toggleLeftBox.clicked.connect(self.openCloseLeftBoxMain)
        # widgets.extraCloseColumnBtn.clicked.connect(self.openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            url = QUrl("https://www.youtube.com/watch?v=xvFZjo5PgG0")  # Замените ссылку на нужную вам
            QDesktopServices.openUrl(url)
            space_tup()
            # UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        # useCustomTheme = False
        # themeFile = "themes\py_dracula_light.qss"
        #
        # # SET THEME AND HACKS
        # if useCustomTheme:
        #     # LOAD AND APPLY STYLE
        #     UIFunctions.theme(self, themeFile, True)
        #
        #     # SET HACKS
        #     AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.new_my_page)
        # widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
    def saveCheckBoxValues(self):
        with open('settings.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

    def linksenc(self, lab):
        # Открыть веб-сайт при нажатии на командную ссылку
        url = QUrl(lab)  # Замените ссылку на нужную вам
        QDesktopServices.openUrl(url)
        space_tup()
    def addMusicGrag(self, even):
        print('Hello')
        print("I clicked")
        with open('settings.json', 'r', encoding='utf-8') as json_file:
            dataset = json.load(json_file)
        print(dataset["Music_Name"])
        print(dataset["Music_DELL"])
        if dataset["Music_DELL"] == "":
            music_name = dataset["Music_Name"]
            similarity_threshold = 50
            should_add_item = True

            # Проверяем сходство music_name со всеми элементами comboBox
            for i in range(self.ui.comboBox_music.count()):
                item_text = self.ui.comboBox_music.itemText(i)
                similarity_ratio = fuzz.ratio(music_name, item_text)
                print(f"Элемент {i}: {item_text} - Сходство: {similarity_ratio}")
                if fuzz.ratio(music_name, item_text) > 80:
                    # Если хотя бы один элемент превышает порог сходства, не добавляем новый элемент
                    should_add_item = False
                    print(f"Элемент {i} превышает порог сходства {similarity_threshold}%")
                    break
            # Добавляем новый элемент, если ни один элемент не превышает порог сходства
            if should_add_item and music_name != "":
                self.ui.comboBox_music.addItem(music_name)
                self.saveCheckBoxValues()
                print(f"Элемент {music_name} успешно добавлен")
        elif dataset["Music_DELL"] != "":
            dell_name = dataset["Music_DELL"]
            for i in range(self.ui.comboBox_music.count()):
                item_text = self.ui.comboBox_music.itemText(i)
                similarity_ratio = fuzz.ratio(dell_name, item_text)
                print(f"Элемент {i}: {item_text} - Сходство: {similarity_ratio}")

                if similarity_ratio > 80:
                    # Если хотя бы один элемент превышает порог сходства, прекратить выполнение
                    self.ui.comboBox_music.removeItem(i)
                    dataset["Music_DELL"] = ""
                    self.saveCheckBoxValues()

    def run_secondary_script_new_commands_program(self):
        with Popen([sys.executable, '-u', 'New_Commands_Voice_EDV.py'],
                   stdout=PIPE, universal_newlines=True) as process:
            for lines in process.stdout:
                lines = lines.strip()

                if lines:  # Проверяем, что строка не пустая
                    # Убираем лишние символы из строки, такие как квадратные скобки и апострофы
                    cleaned_lines = lines.replace('[', '').replace(']', '').replace("'", "")

                    # Разбиваем очищенную строку на отдельные слова
                    words = [word.strip() for word in cleaned_lines.split(',') if word.strip()]

                    # Определяем новый ключ в формате "Program_Voice_<max_index + 1>"
                    max_index = max(
                        [int(key.split("_")[-1]) for key in data.keys() if key.startswith("Program_Voice_")] or [0])
                    new_key_voice = f"Program_Voice_{max_index + 1}"

                    # Сохраняем слова в виде списка без лишних символов
                    data[new_key_voice] = words
                    self.saveCheckBoxValues()  # Сохраняем обновленные значения чекбоксов в JSON

                    # Пример сохранения в JSON файл
                    with open('settings.json', 'w') as json_file:
                        json.dump(data, json_file, indent=4)  # Записываем данные в файл JSON с отступами

                    return words  # Возвращаем слова, если это нужно для дальнейшей обработки

    def run_secondary_script_new_commands_site(self):
        with Popen([sys.executable, '-u', 'New_Commands_Voice_EDV.py'],
                   stdout=PIPE, universal_newlines=True) as process:
            for lines in process.stdout:
                lines = lines.strip()

                if lines:  # Проверяем, что строка не пустая
                    # Убираем лишние символы из строки, такие как квадратные скобки и апострофы
                    cleaned_lines = lines.replace('[', '').replace(']', '').replace("'", "")

                    # Разбиваем очищенную строку на отдельные слова
                    words = [word.strip() for word in cleaned_lines.split(',') if word.strip()]

                    # Определяем новый ключ в формате "Program_Voice_<max_index + 1>"
                    max_index = max(
                        [int(key.split("_")[-1]) for key in data.keys() if key.startswith("Site_Voice_")] or [0])
                    new_key_voice = f"Site_Voice_{max_index + 1}"

                    # Сохраняем слова в виде списка без лишних символов
                    data[new_key_voice] = words
                    self.saveCheckBoxValues()  # Сохраняем обновленные значения чекбоксов в JSON

                    # Пример сохранения в JSON файл
                    with open('settings.json', 'w') as json_file:
                        json.dump(data, json_file, indent=4)  # Записываем данные в файл JSON с отступами

                    return words  # Возвращаем слова, если это нужно для дальнейшей обработки

    def run_secondary_script_new_commands_game(self):
        with Popen([sys.executable, '-u', 'New_Commands_Voice_EDV.py'],
                   stdout=PIPE, universal_newlines=True) as process:
            for lines in process.stdout:
                lines = lines.strip()

                if lines:  # Проверяем, что строка не пустая
                    # Убираем лишние символы из строки, такие как квадратные скобки и апострофы
                    cleaned_lines = lines.replace('[', '').replace(']', '').replace("'", "")

                    # Разбиваем очищенную строку на отдельные слова
                    words = [word.strip() for word in cleaned_lines.split(',') if word.strip()]

                    # Определяем новый ключ в формате "Program_Voice_<max_index + 1>"
                    max_index = max(
                        [int(key.split("_")[-1]) for key in data.keys() if key.startswith("Game_Voice_")] or [0])
                    new_key_voice = f"Game_Voice_{max_index + 1}"

                    # Сохраняем слова в виде списка без лишних символов
                    data[new_key_voice] = words
                    self.saveCheckBoxValues()  # Сохраняем обновленные значения чекбоксов в JSON

                    # Пример сохранения в JSON файл
                    with open('settings.json', 'w') as json_file:
                        json.dump(data, json_file, indent=4)  # Записываем данные в файл JSON с отступами

                    return words  # Возвращаем слова, если это нужно для дальнейшей обработки

    def run_secondary_script_new_commands_steam_game(self):
        with Popen([sys.executable, '-u', 'New_Commands_Voice_EDV.py'],
                   stdout=PIPE, universal_newlines=True) as process:
            for lines in process.stdout:
                lines = lines.strip()

                if lines:  # Проверяем, что строка не пустая
                    # Убираем лишние символы из строки, такие как квадратные скобки и апострофы
                    cleaned_lines = lines.replace('[', '').replace(']', '').replace("'", "")

                    # Разбиваем очищенную строку на отдельные слова
                    words = [word.strip() for word in cleaned_lines.split(',') if word.strip()]

                    # Определяем новый ключ в формате "Program_Voice_<max_index + 1>"
                    max_index = max(
                        [int(key.split("_")[-1]) for key in data.keys() if key.startswith("Steam_Voice_")] or [0])
                    new_key_voice = f"Steam_Voice_{max_index + 1}"

                    # Сохраняем слова в виде списка без лишних символов
                    data[new_key_voice] = words
                    self.saveCheckBoxValues()  # Сохраняем обновленные значения чекбоксов в JSON

                    # Пример сохранения в JSON файл
                    with open('settings.json', 'w') as json_file:
                        json.dump(data, json_file, indent=4)  # Записываем данные в файл JSON с отступами

                    return words  # Возвращаем слова, если это нужно для дальнейшей обработки

    def edit_button_push(self):
        selected_text = self.ui.comboBox_3.currentText()
        print(selected_text)
        index_text = self.ui.comboBox_3.currentIndex()
        print(index_text)
        edit_path = self.ui.lineEdit_2.text()
        edit_name = self.ui.lineEdit_3.text()
        ed_path = True
        ed_name = True
        if edit_path == '' and edit_name == '':
            print("Text now.")
            ed_path = False
            ed_name = False
        elif edit_name == '':
            ed_name = False
        elif edit_path == '':
            ed_path = False
        print(f"Path: {edit_path}, Name: {edit_name}")
        Content_prot = File_to_name_list.find_matching_key(selected_text, threshold=0.8)
        Content = Content_prot.replace("Name", "Content")
        print(Content)
        Name = File_to_name_list.find_matching_key(selected_text, threshold=0.8)
        print(Name)
        if ed_path == True:
            data[f"{Content}"] = edit_path
        if ed_name == True:
            data[f"{Name}"] = edit_name
        self.ui.comboBox_3.setItemText(index_text, edit_name)
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.saveCheckBoxValues()
    def dell_button_push(self):
        elements_to_remove = []
        selected_text = self.ui.comboBox_6.currentText()
        index_selected = self.ui.comboBox_6.currentIndex()
        self.ui.comboBox_6.removeItem(index_selected)
        print(selected_text)
        Name = File_to_name_list.find_matching_key(selected_text, threshold=0.8)
        elements_to_remove.append(Name)
        print(Name)
        Voice_prot = File_to_name_list.find_matching_key(selected_text, threshold=0.8)
        Voice = Voice_prot.replace("Name", "Voice")
        elements_to_remove.append(Voice)
        print(Voice)
        Content_prot  = File_to_name_list.find_matching_key(selected_text, threshold=0.8)
        Content = Content_prot.replace("Name", "Content")
        elements_to_remove.append(Content)
        print(Content)
        Availibal_prot = File_to_name_list.find_matching_key(selected_text, threshold=0.8)
        Availibal = Availibal_prot.replace("Name", "Availibal")
        elements_to_remove.append(Availibal)
        print(Availibal)
        File_to_name_list.remove_elements_from_settings(elements_to_remove)
        print("Files successfully deleted.")

    def say_button_func(self):
        selected_text = self.ui.comboBox_new_commands.currentText()
        print(f"Change element: {selected_text}")
        if self.ui.content_line_edit.text() != '':
            say_num = self.ui.comboBox_4.currentText()
            print(self.ui.comboBox_4.currentText())
            data["Say_number"] = say_num
            self.savechange_settings(data)
            if selected_text == "Program":
                text_name = self.ui.lineEdit_name_new.text()
                print(text_name)
                max_index = 0
                for key in data.keys():
                    if key.startswith("Program_Name_"):
                        try:
                            index = int(key.split("_")[-1])
                            print(f"intex: {index}")
                            if index > max_index:
                                max_index = index
                        except ValueError:
                            continue
                new_key = f"Program_Name_{max_index + 1}"
                data[new_key] = text_name

                max_index = 0
                for key in data.keys():
                    if key.startswith("Program_Availibal_"):
                        try:
                            index = int(key.split("_")[-1])
                            print(f"intex: {index}")
                            if index > max_index:
                                max_index = index
                        except ValueError:
                            continue
                new_key = f"Program_Availibal_{max_index + 1}"
                data[new_key] = "True"

                text = self.ui.content_line_edit.text()
                print(text)
                max_index = 0
                for key in data.keys():
                    if key.startswith("Program_Content_"):
                        try:
                            index = int(key.split("_")[-1])
                            print(f"intex: {index}")
                            if index > max_index:
                                max_index = index
                        except ValueError:
                            continue
                new_key = f"Program_Content_{max_index + 1}"
                data[new_key] = text
                thread = threading.Thread(target=self.run_secondary_script_new_commands_program)
                thread.start()
                self.ui.comboBox_3.addItem(text_name)
                self.ui.comboBox_6.addItem(text_name)
                self.ui.lineEdit_name_new.clear()
                self.ui.path_steam_line_edit.clear()
                self.ui.content_line_edit.clear()
                self.saveCheckBoxValues()
            elif selected_text == "Site":
                selected_text = self.ui.comboBox_new_commands.currentText()
                print(f"Change element: {selected_text}")
                if selected_text == "Site":
                    text_name = self.ui.lineEdit_name_new.text()
                    print(text_name)
                    max_index = 0
                    for key in data.keys():
                        if key.startswith("Site_Name_"):
                            try:
                                index = int(key.split("_")[-1])
                                print(f"intex: {index}")
                                if index > max_index:
                                    max_index = index
                            except ValueError:
                                continue
                    new_key = f"Site_Name_{max_index + 1}"
                    data[new_key] = text_name

                    max_index = 0
                    for key in data.keys():
                        if key.startswith("Site_Availibal_"):
                            try:
                                index = int(key.split("_")[-1])
                                print(f"intex: {index}")
                                if index > max_index:
                                    max_index = index
                            except ValueError:
                                continue
                    new_key = f"Site_Availibal_{max_index + 1}"
                    data[new_key] = "True"

                    text = self.ui.content_line_edit.text()
                    print(text)
                    max_index = 0
                    for key in data.keys():
                        if key.startswith("Site_Content_"):
                            try:
                                index = int(key.split("_")[-1])
                                print(f"intex: {index}")
                                if index > max_index:
                                    max_index = index
                            except ValueError:
                                continue
                    new_key = f"Site_Content_{max_index + 1}"
                    data[new_key] = text
                    thread = threading.Thread(target=self.run_secondary_script_new_commands_site)
                    thread.start()
                    self.ui.comboBox_3.addItem(text_name)
                    self.ui.comboBox_6.addItem(text_name)
                    self.ui.lineEdit_name_new.clear()
                    self.ui.path_steam_line_edit.clear()
                    self.ui.content_line_edit.clear()
                    self.saveCheckBoxValues()
            elif selected_text == "Game":
                steam_text = self.ui.path_steam_line_edit.text()
                text = self.ui.content_line_edit.text()
                if text.endswith(".exe"):
                    selected_text = self.ui.comboBox_new_commands.currentText()
                    print(f"Change element: {selected_text}")
                    if selected_text == "Game":
                        text_name = self.ui.lineEdit_name_new.text()
                        print(text_name)
                        max_index = 0
                        for key in data.keys():
                            if key.startswith("Game_Name_"):
                                try:
                                    index = int(key.split("_")[-1])
                                    print(f"intex: {index}")
                                    if index > max_index:
                                        max_index = index
                                except ValueError:
                                    continue
                        new_key = f"Game_Name_{max_index + 1}"
                        data[new_key] = text_name

                        max_index = 0
                        for key in data.keys():
                            if key.startswith("Game_Availibal_"):
                                try:
                                    index = int(key.split("_")[-1])
                                    print(f"intex: {index}")
                                    if index > max_index:
                                        max_index = index
                                except ValueError:
                                    continue
                        new_key = f"Game_Availibal_{max_index + 1}"
                        data[new_key] = "True"

                        text = self.ui.content_line_edit.text()
                        print(text)
                        max_index = 0
                        for key in data.keys():
                            if key.startswith("Game_Content_"):
                                try:
                                    index = int(key.split("_")[-1])
                                    print(f"intex: {index}")
                                    if index > max_index:
                                        max_index = index
                                except ValueError:
                                    continue
                        new_key = f"Game_Content_{max_index + 1}"
                        data[new_key] = text
                        thread = threading.Thread(target=self.run_secondary_script_new_commands_game)
                        thread.start()
                        self.ui.comboBox_3.addItem(text_name)
                        self.ui.comboBox_6.addItem(text_name)
                        self.ui.lineEdit_name_new.clear()
                        self.ui.path_steam_line_edit.clear()
                        self.ui.content_line_edit.clear()
                        self.saveCheckBoxValues()
                else:
                    selected_text = self.ui.comboBox_new_commands.currentText()
                    print(f"Change element: {selected_text}")
                    if selected_text == "Game":
                        text_name = self.ui.lineEdit_name_new.text()
                        print(text_name)
                        max_index = 0
                        for key in data.keys():
                            if key.startswith("Steam_Name_"):
                                try:
                                    index = int(key.split("_")[-1])
                                    print(f"intex: {index}")
                                    if index > max_index:
                                        max_index = index
                                except ValueError:
                                    continue
                        new_key = f"Steam_Name_{max_index + 1}"
                        data[new_key] = text_name

                        max_index = 0
                        for key in data.keys():
                            if key.startswith("Steam_Availibal_"):
                                try:
                                    index = int(key.split("_")[-1])
                                    print(f"intex: {index}")
                                    if index > max_index:
                                        max_index = index
                                except ValueError:
                                    continue
                        new_key = f"Steam_Availibal_{max_index + 1}"
                        data[new_key] = "True"

                        text = self.ui.content_line_edit.text()
                        print(text)
                        max_index = 0
                        for key in data.keys():
                            if key.startswith("Steam_Content_"):
                                try:
                                    index = int(key.split("_")[-1])
                                    print(f"intex: {index}")
                                    if index > max_index:
                                        max_index = index
                                except ValueError:
                                    continue
                        new_key = f"Steam_Content_{max_index + 1}"
                        data[new_key] = text
                        thread = threading.Thread(target=self.run_secondary_script_new_commands_steam_game)
                        thread.start()
                        self.ui.comboBox_3.addItem(text_name)
                        self.ui.comboBox_6.addItem(text_name)
                        self.ui.lineEdit_name_new.clear()
                        self.ui.path_steam_line_edit.clear()
                        self.ui.content_line_edit.clear()
                        self.saveCheckBoxValues()
                        if steam_text != '':
                            with open('Settings.json', 'r', encoding='utf-8') as default_file:
                                settings = json.load(default_file)
                            settings["Path_Foler_Steam"] = steam_text
                            # Записываем содержимое в файл settings.json, перезаписывая его
                            with open('settings.json', 'w', encoding='utf-8') as settings_file:
                                json.dump(settings, settings_file, indent=4, ensure_ascii=False)
    def on_combobox_changed(self):
        # Получение текста выбранного элемента
        selected_text = self.ui.comboBox_state_comands.currentText()
        print(f"Change element: {selected_text}")

        # Получение индекса выбранного элемента
        selected_index = self.ui.comboBox_state_comands.currentIndex()
        print(f"Index element: {selected_index}")
        if selected_index <= 11:
            checkbox_box2_value = data[f"Command_{selected_index}_activate"].lower() == 'true'
            self.ui.checkBoxx_2.setChecked(checkbox_box2_value)
            radio_box2_value = data[f"Command_{selected_index}_mode"].lower() == 'true'
            self.ui.radioButton_2.setChecked(radio_box2_value)
        elif selected_index > 11:
            Availibal_prot = File_to_name_list.find_matching_key(selected_text, threshold=0.8)
            Availibal = Availibal_prot.replace("Name", "Availibal")
            checkbox_box2_value = data[f"{Availibal}"].lower() == 'true'
            self.ui.checkBoxx_2.setChecked(checkbox_box2_value)
            print(Availibal)

    def checkBoxCommands_activate(self):
        sender = self.sender()
        selected_text = self.ui.comboBox_state_comands.currentText()
        selected_index = self.ui.comboBox_state_comands.currentIndex()
        print(f"Index element: {selected_index}")
        if selected_index <= 11:
            if sender.isChecked():
                new_value = "True"
            else:
                new_value = "False"
            data[f"Command_{selected_index}_activate"] = new_value
        elif selected_index > 11:
            if sender.isChecked():
                new_value = "True"
            else:
                new_value = "False"
            Availibal_prot = File_to_name_list.find_matching_key(selected_text, threshold=0.8)
            Availibal = Availibal_prot.replace("Name", "Availibal")
            data[f"{Availibal}"] = new_value

        self.saveCheckBoxValues()
    def checkBoxCommands_mode(self):
        sender = self.sender()
        selected_index = self.ui.comboBox_state_comands.currentIndex()
        print(f"Index element: {selected_index}")
        if sender.isChecked():
            new_value = "True"
        else:
            new_value = "False"
        data[f"Command_{selected_index}_mode"] = new_value
        self.saveCheckBoxValues()

    # def set_default(self):
    #
        # boolis = set_default_yes_no_ok.main_logic()
        # print(boolis)
        # if boolis == True:
        #     with open('Settings_Default.json', 'r', encoding='utf-8') as default_file:
        #         default_settings = json.load(default_file)
        #
        #     # Записываем содержимое в файл settings.json, перезаписывая его
        #     with open('settings.json', 'w', encoding='utf-8') as settings_file:
        #         json.dump(default_settings, settings_file, indent=4)
        # else:
        #     pass
    def savechange_settings(self, data):
        with open('settings.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

    def run_secondary_script(self):
        subprocess.run(["python", "C:/Users/IVNsell/Desktop/IVNsell/Python/GestureVox Integration/Modern_GUI_PyDracula_PySide6_or_PyQt6-master/HierSpeechpp/HierSpeechpp/Name_asis_change.py"])
    def chose_name_default(self, log):
        if log:
            # name_asis_list = Name_asis_change.main_logic_name()
            name_num = self.ui.comboBox_2.currentText()
            print(self.ui.comboBox_2.currentText())
            data["Name_asis_default"] = "True"
            data["Name_number"] = name_num
            self.savechange_settings(data)
            thread = threading.Thread(target=self.run_secondary_script)
            thread.start()
        else:
            # boolis = Name_asis_change.main_logic_default()
            data["Name_asis_default"] = "False"
            self.savechange_settings(data)
            thread = threading.Thread(target=self.run_secondary_script)
            thread.start()
            # print(boolis)

    def chose_name_default_thre(self, log):
        print("asinc_activate")
        threading.Thread(target=self.chose_name_default(log, )).start()

    def on_return_pressed(self):
        # Проверяем, активен ли lineEdit_5 и есть ли в нем текст
        if self.ui.lineEdit_5.hasFocus() and self.ui.lineEdit_5.text():
            text = self.ui.lineEdit_5.text()
            data["Chat_GPT"] = text
            print(text)
            self.ui.lineEdit_5.clear()
            self.saveCheckBoxValues()

    def FIVIC(self):
        print("fivic")
        # subprocess.run(["python", "C:/Users/IVNsell/Desktop/IVNsell/Python/Tect_OpenCV_for_project/OpenCV_plus_ultra.py"])
        subprocess.run(["python", "C:/Users/IVNsell/Desktop/IVNsell/Python/GestureVox Integration/Modern_GUI_PyDracula_PySide6_or_PyQt6-master/HierSpeechpp/HierSpeechpp/FIVferen.py"])

    def select_and_move_file(self):
        # Open the file selection dialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Select a voice file", "", "Voice Files (*.wav)")
        if file_name:
            # Get the file name from the full path
            file_base_name = os.path.basename(file_name)

            # Set the path to the folder where we want to move the file
            destination_folder = 'example/'
            destination_path = os.path.join(destination_folder, file_base_name)
            data["FIV"] = "True"
            print("oke")
            self.saveCheckBoxValues()
            threading.Thread(target=self.FIVIC).start()
            print("pip")
            # Check if the file exists in the target folder
            if not os.path.exists(destination_path):
                try:
                    # Move the file
                    shutil.move(file_name, destination_path)
                    data["Voice asistent"] = f"{file_base_name}"
                    self.saveCheckBoxValues()
                    print(f'File "{file_base_name}" has been moved to "{destination_folder}"')
                except Exception as e:
                    print(f'An error occurred while moving the file: {e}')
            else:
                # If the file already exists, print a message
                data["Voice asistent"] = f"{file_base_name}"
                self.saveCheckBoxValues()
                print(
                    f'File "{file_base_name}" already exists in the folder "{destination_folder}". Moving not performed.')

    def checkBoxStateChanged(self, state):
        sender = self.sender()
        checkbox_number = int(sender.objectName().split('_')[-1])
        gesture_key = f"Gesture_{checkbox_number}"
        print(f"{gesture_key} State: {state}")

        if sender.isChecked():
            new_value = "True"
        else:
            new_value = "False"

        new_value = new_value.capitalize()
        data[gesture_key] = new_value
        self.saveCheckBoxValues()

        # Сохраняем обновленные значения флажков в файл JSON
        # self.saveCheckBoxValues()
    # Функции для управления воспроизведением
    def togglePlayPause(self):
        if self.mediaPlayer.playbackState() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
            # Изменение иконки на 'play'
            widgets.pushButton_play.setStyleSheet(u"border: none;\n"
"background-image: url(:/icons/images/icons/play_game_music_icon.png);")
        else:
            self.mediaPlayer.play()
            # Изменение иконки на 'pause'
            widgets.pushButton_play.setStyleSheet(u"border: none;\n"
"background-image: url(:/icons/images/icons/pause_icon.png);")

    def skipVideo(self, seconds):
        currentPosition = self.mediaPlayer.position()
        self.mediaPlayer.setPosition(currentPosition + seconds * 1000)
    def playMedia(self):
        if self.mediaPlayer.playbackState() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
            self.playButton.setText('Play')
        else:
            self.mediaPlayer.play()
            self.playButton.setText('Pause')
    def openWebsitetroll(self, lab):
        # Открыть веб-сайт при нажатии на командную ссылку
        url = QUrl("https://www.youtube.com/watch?v=xvFZjo5PgG0")  # Замените ссылку на нужную вам
        QDesktopServices.openUrl(url)
        space_tup()
    def vieoInstruct(self, lab):
        # Открыть веб-сайт при нажатии на командную ссылку
        url = QUrl("https://youtu.be/WR_tgqRLJmw")  # Замените ссылку на нужную вам
        QDesktopServices.openUrl(url)
    def openWebsitepresent(self, lab):
        url = QUrl("https://www.figma.com/design/GN3yYRv0Ft6Nj3qVZxoaoT/Haydarov?node-id=2325%3A434&t=7lVHl8R2EWQp0U0X-1")  # Замените ссылку на нужную вам
        QDesktopServices.openUrl(url)
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
            widgets.stackedWidget.setCurrentWidget(widgets.Instruction) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_info":
            widgets.stackedWidget.setCurrentWidget(widgets.Info_me)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            print("Save BTN clicked!")
        if btnName == "btn_exit":
            widgets.stackedWidget.setCurrentWidget(widgets.thanks_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED   Collor: 64, 255, 182
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            print("Exit BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

        # EXTRA LEFT BOX

    # def openCloseLeftBox(self):
    #     # GET BUTTON CLICKED
    #     UIFunctions.toggleLeftBox(self, True)
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
        widgets.stackedWidget.setCurrentWidget(widgets.new_page)  # SET PAGE
        UIFunctions.resetStyle(self, btnName)
        togel.setStyleSheet(UIFunctions.selectMenu(togel.styleSheet()))
        # togel_style = widgets.toggleLeftBox.styleSheet()

        # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
        # UIFunctions.toggleLeftBox(self, True)

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    # def resizeEvent(self, event):
    #     # Update Size Grips
    #     UIFunctions.resize_grips(self)

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