import platform, os, time, socket, urllib.request, requests

# Obtenha o token do bot e substitua o valor abaixo
def send_to_telegram(message):
    apiToken = 'SEU_TOKEN'
    chatID = 'SEU-CHAT-ID'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)


if platform.system() == "Windows":
    ping_command = "ping -n 1 google.com > nul"
    ping_command6 = "ping -6 -n 1 google.com > nul"
else:
    ping_command = "ping -c 1 google.com > /dev/null 2>&1"
    ping_command6 = "ping6 -c 1 google.com > /dev/null 2>&1"

while True:
    response = os.system(ping_command)
    response6 = os.system(ping_command6)

    if response == 0:
        print("Ping concluído com sucesso.")

        # Obtém o endereço IP da interface de rede LAN em IPv4 e IPv6
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("google.com", 80))
        lan_ipv4 = s.getsockname()[0]
        s.close()

        hostname = socket.gethostname()
        print("Endereço IP da LAN em IPv4:", lan_ipv4)

        # Obtém o endereço IP da interface de rede WAN em IPv4 e IPv6
        wan_ipv4 = urllib.request.urlopen("https://ipv4.icanhazip.com").read().decode().strip()
        print("Endereço IP da WAN em IPv4:", wan_ipv4)
        
        if response6 == 0:
            wan_ipv6 = urllib.request.urlopen("https://ipv6.icanhazip.com").read().decode().strip()
            print("Endereço IP da WAN em IPv6:", wan_ipv6)
        else:
            wan_ipv6="null"

        # Crie uma mensagem com as informações do IP
        message = f"Hostname: {hostname}\nEndereço IP da LAN em IPv4: {lan_ipv4}\nEndereço IP da WAN em IPv4: {wan_ipv4}\nEndereço IP da WAN em IPv6: {wan_ipv6}"
        send_to_telegram(message)
        break
    else:
        print("Ping não concluído. Tentando novamente em 5 segundos...")
        time.sleep(5)
