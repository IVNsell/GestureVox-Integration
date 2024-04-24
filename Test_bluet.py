# from PyQt5.QtCore import Qt, QCoreApplication, QThread  # Добавьте эту строку
# from PyQt5.QtBluetooth import QBluetoothDeviceDiscoveryAgent
# from PyQt5.QtWidgets import QApplication
# import sys
#
# class BluetoothScanner(QCoreApplication):
#     def __init__(self, argv):
#         super().__init__(argv)
#
#         self.discovery_agent = QBluetoothDeviceDiscoveryAgent(self)
#         self.discovery_agent.deviceDiscovered.connect(self.device_discovered)
#
#         print("Scanning for Bluetooth devices. Enter '0' to stop...")
#         self.discovery_agent.start()
#
#         # Запускаем цикл проверки ввода с консоли в отдельном потоке
#         self.console_thread = ConsoleThread(self)
#         self.console_thread.start()
#
#     def device_discovered(self, device):
#         print(f"Device discovered: {device.name()} ({device.address().toString()})")
#
#     def stop_scanning(self):
#         # Останавливаем сканирование
#         self.discovery_agent.stop()
#
# class ConsoleThread(QThread):
#     def __init__(self, scanner):
#         super().__init__()
#         self.scanner = scanner
#
#     def run(self):
#         while True:
#             # Читаем ввод с консоли
#             user_input = input()
#             if user_input == '0':
#                 # Вызываем метод остановки сканирования из основного потока
#                 self.scanner.stop_scanning()
#                 break
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     scanner = BluetoothScanner(sys.argv)
#     sys.exit(app.exec_())

import subprocess
import time
def Connect_Rezer_Opus():
    try:
        subprocess.run(["C:/Users/IVNsell/source/repos/Lessons/Lesson_0/bin/Debug/net8.0/Lesson_0.exe"])
    except subprocess.CalledProcessError as e:
        # Обработка исключения, например, вывод сообщения об ошибке
        print(f"An error occurred: {e}")
def DisConnect_Razer_Opus():
    subprocess.run(["C:/Users/IVNsell/source/repos/DisConnect_Razer_Opus/DisConnect_Razer_Opus/bin/Debug/net8.0/DisConnect_Razer_Opus.exe"])
    time.sleep(0.7)
    subprocess.run(["C:/Users/IVNsell/source/repos/DisConnect_Razer_Opus/DisConnect_Razer_Opus/bin/Debug/net8.0/DisConnect_Razer_Opus.exe"])
# DisConnect_Razer_Opus()
# Connect_Rezer_Opus()
#32feet.NET
#Install-Package System.Configuration.ConfigurationManager -Version 4.7.0
