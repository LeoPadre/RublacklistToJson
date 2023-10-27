import socket
import json
import requests

# Функция для получения IP-адреса сайта
def get_ip_address(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.error:
        return None

# URL для получения списка адресов с сайта
url = "https://reestr.rublacklist.net/api/v3/domains/"

# Отправляем GET-запрос и получаем данные в формате JSON
response = requests.get(url)
if response.status_code != 200:
    print("Не удалось получить список адресов с сайта")
    exit()

websites = response.json()

# Измените названия файлов именно в этом месте
output_file_path = 'domain_list.json'

# Создаем список для хранения данных в формате JSON
result_data = []

# Проходим по каждому сайту, получаем IP-адрес и добавляем в список
for i, website in enumerate(websites, start=1):
    ip_address = get_ip_address(website)
    if ip_address:
        result_data.append({"hostname": website, "ip": ip_address})
    print(f"Обработан {i}/{len(websites)} адрес: {website}")

# Записываем результат в JSON-файл
with open(output_file_path, 'w') as output_file:
    json.dump(result_data, output_file, indent=4)

print("Готово. Результат сохранен в", output_file_path)