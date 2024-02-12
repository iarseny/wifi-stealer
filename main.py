import subprocess

info = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("cp866").split("\n")
wifi_fis = [line.split(":")[1][1:-1] for line in info if "Все профили пользователей" in line]

for wifi in wifi_fis:
    res = subprocess.check_output(["netsh", "wlan", "show", "profiles", wifi, "key=clear"]).decode("cp866").split("\n")
    res = [line.split(":")[1][1:-1] for line in res if "Содержимое ключа" in line]

    try:
        print(f"Имя сети: {wifi}, пароль {res[0]}")
    except IndexError:
        print("Не найдено пароля")
