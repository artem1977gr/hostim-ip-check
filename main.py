import urllib.request

try:
    with urllib.request.urlopen(
        "https://api.ipify.org", timeout=15
    ) as response:
        ip = response.read().decode().strip()

    print("Исходящий IP Hostim:", ip, flush=True)

except Exception as error:
    print("Ошибка проверки:", error, flush=True)
