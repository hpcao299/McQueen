import socket
import os
from requests import get
import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello! Welcome to the bot " + str(message.chat.id))

@bot.message_handler(commands=['myip'])
def get_my_ip(message):
    public_ipv6 = get('https://api6.ipify.org').text
    response = get('https://ipinfo.io/json')

    ip_details = response.json()
    bot.send_message(chat_id=message.chat.id, text=f"Public IPv4: {ip_details['ip']}\nPublic IPv6: {public_ipv6}\nLocation: {ip_details['city']}/{ip_details['country']}\nTimezone: {ip_details['timezone']}\nHostname: {ip_details['hostname']}\nOrigin: {ip_details['org']}")



bot.polling()
