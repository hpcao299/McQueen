import socket
import os
from requests import get
import telebot
import validators
import ipaddress
from urllib.parse import urlparse

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def get_ip_details(ip = ""):
    if ip:
        response = get(f'https://ipinfo.io/{ip}/json')
        ip_details = response.json()

        return f"Public IPv4: {ip_details['ip']}\nLocation: {ip_details['city']}/{ip_details['country']}\nTimezone: {ip_details['timezone']}\nHostname: {ip_details['hostname']}\nOrigin: {ip_details['org']}"
    else:
        response = get('https://ipinfo.io/json')
        ip_details = response.json()

        return f"Public IPv4: {ip_details['ip']}\nLocation: {ip_details['city']}/{ip_details['country']}\nTimezone: {ip_details['timezone']}\nHostname: {ip_details['hostname']}\nOrigin: {ip_details['org']}"        

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello! Welcome to the bot " + str(message.chat.id))

@bot.message_handler(commands=['myip'])
def get_my_ip(message):
    try:
        public_ipv6 = get('https://api6.ipify.org').text
        ip_details = get_ip_details()

        bot.send_message(chat_id=message.chat.id, text=f"Public IPv6: {public_ipv6}\n{ip_details}")
    except Exception:
        bot.send_message(chat_id=message.chat.id, text="There is something wrong in our server")

@bot.message_handler(commands=['trackwebsite'])
def get_website_ip(message):
    text = message.text
    content = text.split("/trackwebsite", 1)[1].strip()

    if validators.url(content):
        try:
            hostname = urlparse(content).netloc
            ip = socket.gethostbyname(hostname)
            ip_details = get_ip_details(ip)
            bot.send_message(chat_id=message.chat.id, text=f"Result for {hostname}:\n\n{ip_details}\n\nFor more details: https://who.is/whois-ip/ip-address/{ip}")
        except Exception as e:
            bot.send_message(chat_id=message.chat.id, text=f"Found IP for {hostname}: {ip}\n\nFor more details: https://who.is/whois-ip/ip-address/{ip}")
    else:
        bot.send_message(chat_id=message.chat.id, text="Given URL is invalid.")
        
@bot.message_handler(commands=['trackip'])
def track_ip_details(message):
    text = message.text
    content = text.split('/trackip', 1)[1].strip()

    if content is None or content == "":
        bot.send_message(chat_id=message.chat.id, text="Provide me an IP address.\nExample: 8.8.8.8 (Google hostname)")
        return

    if validate_ip(content):
        hostname,_,_ = socket.gethostbyaddr(content)
        bot.send_message(chat_id=message.chat.id, text=f"Result for {content}:\n\nFound hostname: {hostname}\n\nFor more details: https://who.is/whois-ip/ip-address/{content}")
    else:
        bot.send_message(chat_id=message.chat.id, text=f"Given IP address is invalid.")

bot.infinity_polling()
