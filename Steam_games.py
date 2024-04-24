import time
import pygetwindow as gw
import subprocess
import pyautogui as pg

def Cyberpunk_2077():
    print(234)
    def close_window(window_title):
        print(1)
        target_window = gw.getWindowsWithTitle(window_title)
        if target_window:
            target_window[0].close()
    def cyberpunk_sub():
        print(12)
        steam_path = r"C:\Program Files (x86)\Steam\steam.exe"  # Укажите путь к исполняемому файлу Steam
        game_id = "1091500"  # ID Cyberpunk 2077
        subprocess.Popen([steam_path, f"steam://rungameid/{game_id}"])
    def py_auto():
        print(13)
        time.sleep(5)
        pg.moveTo(542, 519)
        pg.leftClick()
    window_title_to_close = "Steam"
    close_window(window_title_to_close)
    cyberpunk_sub()
    py_auto()
def Diying_Light_2():
    print(234)
    def close_window(window_title):
        print(1)
        target_window = gw.getWindowsWithTitle(window_title)
        if target_window:
            target_window[0].close()
    def cyberpunk_sub():
        print(12)
        steam_path = r"C:\Program Files (x86)\Steam\steam.exe"  # Укажите путь к исполняемому файлу Steam
        game_id = "534380"  # ID Diying Light 2
        subprocess.Popen([steam_path, f"steam://rungameid/{game_id}"])
    window_title_to_close = "Steam"
    close_window(window_title_to_close)
    cyberpunk_sub()
def Terarria():
    print(234)
    def close_window(window_title):
        print(1)
        target_window = gw.getWindowsWithTitle(window_title)
        if target_window:
            target_window[0].close()
    def cyberpunk_sub():
        print(12)
        steam_path = r"C:\Program Files (x86)\Steam\steam.exe"  # Укажите путь к исполняемому файлу Steam
        game_id = "105600"  # ID Terarria
        subprocess.Popen([steam_path, f"steam://rungameid/{game_id}"])
    window_title_to_close = "Steam"
    close_window(window_title_to_close)
    cyberpunk_sub()
def Wallpeper_Engine():
    print(234)
    def close_window(window_title):
        print(1)
        target_window = gw.getWindowsWithTitle(window_title)
        if target_window:
            target_window[0].close()
    def wallpeper_sub():
        print(12)                                                                             #
        steam_path = r"C:\Program Files (x86)\Steam\steam.exe"  # Укажите путь к исполняемому файлу Steam
        game_id = "431960"  # ID Wallpeper Engine
        subprocess.Popen([steam_path, f"steam://rungameid/{game_id}"])
    def py_auto():
        time.sleep(0.3)
        pg.moveTo(1713, 620)
        pg.click()
    window_title_to_close = "Steam"
    wallpeper_sub()
    close_window(window_title_to_close)
    py_auto()