#pegar ip da lan usando ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' |grep -Eo '([0-9]*\.){3}[0-9]*' |grep -v '127.0.0.1'
#pegar ip wan ipv4 usando curl -4 icanhazip.com
#pegar ip wan ipv6 usando curl -6 icanhazip.com

#!/bin/bash

import platform
import os
import time
import socket
import urllib.request
import telegram

# Obtenha o token do bot e substitua o valor abaixo
TOKEN = '5743626552:AAFTLiLkmRq_3nMI32Cfy_lyRlS9_oCpaA4'
CHAT_ID = '364880828'


if platform.system() == "Windows":
    ping_command = "ping -n 1 google.com > nul"
else:
    ping_command = "ping -c 1 google.com > /dev/null 2>&1"

while True:
    response = os.system(ping_command)

    if response == 0:
        print("Ping concluído com sucesso.")

        # Obtém o endereço IP da interface de rede LAN em IPv4 e IPv6
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        lan_ipv4 = s.getsockname()[0]
        s.close()
        lan_ipv6 = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)[0][4][0]


        hostname = socket.gethostname()
        print("Endereço IP da LAN em IPv4:", lan_ipv4)
        #print("Endereço IP da LAN em IPv6:", lan_ipv6)

        # Obtém o endereço IP da interface de rede WAN em IPv4 e IPv6
        wan_ipv4 = urllib.request.urlopen("https://ipv4.icanhazip.com").read().decode().strip()
        wan_ipv6 = urllib.request.urlopen("https://ipv6.icanhazip.com").read().decode().strip()
        print("Endereço IP da WAN em IPv4:", wan_ipv4)
        print("Endereço IP da WAN em IPv6:", wan_ipv6)
        
        
        # Crie uma mensagem com as informações do IP
        message = f"Hostname: {hostname}\nIP LAN Address: {lan_ipv4}\nIP WAN Address: {wan_ipv4}\nIP WAN6 Address: {wan_ipv6}"

        # Crie uma instância do bot
        bot = telegram.Bot(TOKEN)

        # Envie a mensagem para o chat_id especificado
        #bot.send_message(chat_id=CHAT_ID, text=message)
        bot.send_message(chat_id=CHAT_ID, text=message)
        break
    else:
        print("Ping não concluído. Tentando novamente em 5 segundos...")
        time.sleep(5)
