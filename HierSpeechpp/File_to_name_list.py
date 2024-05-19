import json
import difflib

with open('settings.json', 'r', encoding='utf-8') as f:
    settings_data = json.load(f)

def open_tu_name():
    # Открываем файл settings.json и загружаем его содержимое как словарь

    # Словарь для хранения значений, где ключи - имена с префиксами (например, Steam_Name_{i}),
    # значения - строка, содержащая все найденные значения через запятую
    name_value_strings = {}

    # Ищем ключи с нужными префиксами и сохраняем их значения в словарь
    for key, value in settings_data.items():
        if key.startswith("Steam_Name_") or \
                key.startswith("Game_Name_") or \
                key.startswith("Program_Name_") or \
                key.startswith("Site_Name_"):
            # Извлекаем индекс i из ключа, например, Steam_Name_{i}
            try:
                index = int(key.split('_')[-1])  # Получаем индекс i из ключа
            except ValueError:
                continue  # Пропускаем ключи, у которых неверный формат индекса

            # Формируем имя ключа без индекса, например, Steam_Name_
            name_prefix = '_'.join(key.split('_')[:-1]) + '_'

            # Формируем полное имя ключа, например, Steam_Name_{i}
            full_key = f"{name_prefix}{index}"

            # Проверяем, существует ли уже такой ключ в словаре
            if full_key in name_value_strings:
                # Если ключ уже есть, добавляем новое значение через запятую
                name_value_strings[full_key] += f", {value}"
            else:
                # Если ключа еще нет, создаем новую строку значений
                name_value_strings[full_key] = value

    list_text = []
    for key, values in name_value_strings.items():
        print(f"Key: {key}, Values: {values}")
        list_text.append(values)
    print(list_text)
    return list_text

def find_matching_key(input_text, threshold=0.8):
    with open('settings.json', 'r', encoding='utf-8') as f:
        settings_datas = json.load(f)
    # Проходим по всем ключам и значениям из файла настроек
    for key, value in settings_datas.items():
        if isinstance(value, list):
            # Если значение - список, объединяем его в одну строку для сравнения
            value_str = ' '.join(value)
        else:
            value_str = str(value)

        # Используем SequenceMatcher для сравнения строк
        similarity = difflib.SequenceMatcher(None, input_text.lower(), value_str.lower()).ratio()

        # Если степень сходства больше порогового значения, возвращаем ключ
        if similarity >= threshold:
            return key

    # Если не найдено подходящего ключа, возвращаем None
    return None

# Пример использования: запрос пользователя
# user_input = input("Введите текст для поиска: ")
#
# # Находим соответствующий ключ с пороговым сходством 80%
# matching_key = find_matching_key(user_input, threshold=0.8)
#
# if matching_key:
#     print(f"Найден соответствующий ключ: {matching_key}")
# else:
#     print("Соответствующий ключ не найден.")
def remove_elements_from_settings(elements_to_remove):

    # Проходим по каждому элементу из списка elements_to_remove
    for element in elements_to_remove:
        # Проверяем, существует ли такой элемент в settings_data
        if element in settings_data:
            # Удаляем элемент из словаря settings_data
            del settings_data[element]

    # Записываем обновленные данные обратно в файл settings.json
    with open('settings.json', 'w', encoding='utf-8') as f:
        json.dump(settings_data, f, indent=4, ensure_ascii=False)



# Пример использования:
# if __name__ == "__main__":
#     # Список элементов, которые нужно удалить
#     elements_to_remove = ["Program_Name_2", "Program_Voice_2", "Program_Content_2"]
#
#     # Вызываем функцию remove_elements_from_settings для удаления элементов из файла
#     remove_elements_from_settings("settings.json", elements_to_remove)
#
#     print("Элементы успешно удалены из файла settings.json.")