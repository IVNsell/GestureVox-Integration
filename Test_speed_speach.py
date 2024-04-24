# import Test_To_Speach
# import Jarvis_Voice
# import tts_test
# text = "добрый день меня зовут ваня гайдаров"
# # Jarvis_Voice.main(text)
# tts_test.speak(text)
# # Test_To_Speach.text_to_speech(text)
import torch

# Загрузка весов из файла
checkpoint_path = 'G_100000.pth'  # Замените на фактический путь к вашему файлу
checkpoint = torch.load(checkpoint_path, map_location=torch.device('cpu'))  # Если нет GPU

# Печать ключей весов
print("Keys in the checkpoint:")
print(checkpoint.keys())

# Печать структуры модели (если она есть)
if 'model' in checkpoint:
    print("\nModel structure:")
    print(checkpoint['model'])
else:
    print("\nModel structure is not available in the checkpoint.")

# Печать значений параметров (если они есть)
if 'model_state_dict' in checkpoint:
    print("\nValues of model parameters:")
    for key, value in checkpoint['model_state_dict'].items():
        print(f"{key}: {value}")
else:
    print("\nModel parameters are not available in the checkpoint.")
