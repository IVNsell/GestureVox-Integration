import json
from fuzzywuzzy import fuzz
import webbrowser
import subprocess
import Steam_geames_activaation_name
def ckeck_num_comands_start(text_user):
    # Открываем файл settings.json и загружаем его содержимое
    with open('settings.json', 'r', encoding='utf-8') as file:
        settings_data = json.load(file)

    # Создаем словарь для хранения значений по различным категориям
    category_values = {}
    # Проходим по всем ключам в словаре settings_data
    for key in settings_data:
        # Определяем префиксы категорий
        prefixes = [
            "Steam_Voice_",
            "Game_Voice_",
            "Site_Voice_",
            "Program_Voice_",
        ]

        # Проверяем, начинается ли текущий ключ с одного из префиксов
        for prefix in prefixes:
            if key.startswith(prefix):
                # Извлекаем имя категории, например, "Steam_Voice_i" -> "Steam_Voice"
                category = prefix.rstrip('_')

                # Создаем список значений для этой категории, если его еще нет
                if category not in category_values:
                    category_values[category] = []

                # Добавляем кортеж (ключ, значение) в список для текущей категории
                category_values[category].append((key, settings_data[key]))

    # Выводим полученные значения для каждой категории
    for category, values in category_values.items():
        # print(f"{category} Values:")
        for key, value in values:
            # print(f"    {key}: {value}")
            for val in value:
                # print(f"Text_user: {text_user}     Value: {val}")
                if fuzz.ratio(text_user, val) > 60:
                    # print(key)
                    print(val)
                    index = key.find("_Voice_")
                    filtered_text = key[index + len("_Voice_"):]
                    print(filtered_text)
                    parts = key.split("_Voice_")
                    before_voice = parts[0]
                    print(before_voice)
                    avalible = settings_data[f"{before_voice}_Availibal_{filtered_text}"].lower() == 'true'
                    print(avalible)
                    if before_voice == "Site" and avalible == True:
                        site_content = settings_data.get(f"Site_Content_{filtered_text}")
                        webbrowser.open(site_content, 0, True)
                        break
                    elif before_voice == "Program" and avalible == True:
                        program_content = settings_data.get(f"Program_Content_{filtered_text}")
                        subprocess.Popen([program_content])
                        break
                    elif before_voice == "Game" and avalible == True:
                        game_content = settings_data.get(f"Game_Content_{filtered_text}")
                        subprocess.Popen([game_content])
                        break
                    elif before_voice == "Steam" and avalible == True:
                        steam_content = settings_data.get(f"Steam_Content_{filtered_text}")
                        steam_path = settings_data.get("Path_Foler_Steam")
                        Steam_geames_activaation_name.game(steam_content, steam_path)
                        break
                    # return filtered_text, before_voice

# text_user = input("Write your app: ")
# ckeck_num_comands_start(text_user)