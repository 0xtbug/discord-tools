import discord
import random
import string
import asyncio
import datetime
import requests
import os
import json
import pyfiglet
import pytz
from termcolor import colored
from colorama import Fore

from discord.ext import (
    commands,
    tasks
)

client = discord.Client()
client = commands.Bot(
    command_prefix="!",
    self_bot=True
)
client.remove_command('help')

def scale(time):
    defined = 60
    for unit in ["m", "h"]:
        if time < defined:
            return f"{time:.2f}{unit}"
        time /= defined

def get_user_info(user_id):
    response = requests.get(f'https://discordlookup.mesavirep.xyz/v1/user/{user_id}')
    if response.status_code == 200:
        user_info = response.json()
        return user_info.get("tag", "Unknown").replace("#0", "")
    else:
        return "Unknown"

def Init(token):
    if token["token"] == "token-here":
        os.system('cls')
        print(f"\n{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}You haven't entered your token into the config.json file.\n\n"+Fore.RESET)
        exit()
    else:
        try:
            client.run(token["token"], bot=False, reconnect=True)
            os.system(f'Discord LevelUpBot')
        except discord.errors.LoginFailure:
            print(f"\n{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Token not valid\n\n"+Fore.RESET)

def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = []
        for line in file:
            lines.append(line)
        return lines

with open('config.json') as f:
    config = json.load(f)

is_telegram_bot = config.get("is_telegram_bot", False)

os.system('cls')
result = pyfiglet.figlet_format("""Discord Tools""", font="slant")
print(colored(result, 'yellow'))
ip = requests.get('https://api.ipify.org').text
x = datetime.datetime.now(pytz.timezone("Asia/Jakarta"))
print (colored('''Created by: YSA DEV - Recoded by 0xtbug''', 'cyan', attrs=['bold']))
print (colored('===========================================================', 'green', attrs=['bold']))
print (colored(f"Ξ START           : {x.strftime('%d-%m-%Y %H:%M:%S')} \nΞ Your IP         : {ip} ", 'green', attrs=['bold']))
print (colored('=========================================================== \n', 'green', attrs=['bold']))
print("List Account: ");

for idx, token in enumerate(config["accounts"], start=1):
    user_name = get_user_info(token["id"])
    print(f"{idx}. {user_name}")

while True:
    token_index = int(input("Choose your account: "))
    if 1 <= token_index <= len(config["accounts"]):
        break
    else:
        print("Indeks not valid, please input correctly!")
        
while True:
    choicel = str(input("Choose language ID or EN: ")).upper()
    if choicel != "ID" and choicel != "EN":
        print("Invalid input. Please enter either ID or EN.")
    else:
        break
while True:
    choicec = str(input("Remove message after send? (y/N): ")).upper()
    if choicec != "Y" and choicec != "N":
        print("Invalid input. Please enter either y or n.")
    else:
        break
while True:
    delaytime = int(input("Enter time ex. 60 seconds = 1 minutes: "))
    if delaytime <= 0:
        print("Invalid input. Please enter a valid time.")
    else:
        break

@client.command()
async def lp(ctx, amount: int):
    await ctx.message.delete()
    msgsend = amount
    success_count = 0
    fail_count = 0
    print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Sending {Fore.WHITE}{msgsend}{Fore.LIGHTBLACK_EX} messages to {Fore.WHITE}#{ctx.channel.name}{Fore.LIGHTBLACK_EX} channel in {Fore.WHITE}{ctx.guild.name}{Fore.LIGHTBLACK_EX} server")
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Estimated Time: {Fore.WHITE}{scale(msgsend)}\n")
    
    x = datetime.datetime.now(pytz.timezone("Asia/Jakarta"))
    try:
        for _ in range(msgsend):
            output = get_random_output()
            await ctx.send(output)
            success_count += 1
            msgsend -= 1
            print(f"{Fore.WHITE}[{Fore.GREEN}{x.strftime('%d-%m-%Y %H:%M:%S')}{Fore.WHITE}] {Fore.LIGHTBLACK_EX}Message sent! | Messages left to send: {Fore.WHITE}{msgsend} {Fore.LIGHTBLACK_EX}| Estimated Time: {Fore.WHITE}{scale(msgsend)}")
            await asyncio.sleep(1)
            if choicec == "Y":
                async for message in ctx.message.channel.history(limit=1).filter(lambda m: m.author == client.user).map(lambda m: m):
                    try:
                        await message.delete()
                        print(f"{Fore.WHITE}[{Fore.GREEN}{x.strftime('%d-%m-%Y %H:%M:%S')}{Fore.WHITE}] {Fore.LIGHTBLACK_EX}Success delete message {Fore.WHITE}#{msgsend}")
                    except:
                        print(f"{Fore.WHITE}[{Fore.RED}{x.strftime('%d-%m-%Y %H:%M:%S')}{Fore.WHITE}] {Fore.LIGHTBLACK_EX}Cannot delete message {Fore.WHITE}#{msgsend}")
                        pass
            await asyncio.sleep(delaytime)
    except Exception as e:
        fail_count += 1
        print(f"{Fore.WHITE}[{Fore.RED}{x.strftime('%d-%m-%Y %H:%M:%S')}{Fore.WHITE}] {Fore.LIGHTBLACK_EX}Error: {e} | Cannot send message {Fore.WHITE}#{msgsend}")
    if is_telegram_bot:
        await send_telegram_message(ctx, config["telegram"]["token"], config["telegram"]["chat_id"], success_count, fail_count)
    else:
        print(f"\n[{x.strftime('%d-%m-%Y %H:%M:%S')}] All messages have been sent. Successful: {success_count} | Failed: {fail_count}")
        return

def get_random_output():
    if choicel == "ID":
        kata = read_file('kataid.txt')
        return random.choice(kata)
    elif choicel == "EN":
        kataen = read_file('kataen.txt')
        return random.choice(kataen)
    else:
        return "Invalid input"

async def send_telegram_message(ctx, token, chat_id, success_count, fail_count):
    guild_name = ctx.guild.name if ctx.guild else "Unknown Guild"

    url = f'https://api.telegram.org/bot{token}/sendMessage'
    message = f'\n ℹ️ *Info Discord LevelUp* \n\n 🧐 From account: {client.user.name} \n 🔔 To server: {guild_name} \n\n 🚀 *All messages have been sent!* \nSuccess: {success_count} | Failed: {fail_count}'

    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown',
    }

    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(f"\n[Telegram] Message successfully sent to Telegram.")
    else:
        print(f"\n[Telegram] Failed to send message to Telegram. (Status code: {response.status_code})")

@client.event
async def print_info():
    await client.wait_until_ready()
    print (colored('+===================== BOT START! ========================+', 'red', attrs=['bold']))
    print(f"{Fore.WHITE}[ {Fore.GREEN}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Logged as: {Fore.WHITE}{client.user.name}")
    print(f"{Fore.WHITE}[ {Fore.GREEN}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Write ON DISCORD channel: {Fore.WHITE}\n!lp <number of messages> to Start Level UP")
client.loop.create_task(print_info())

@client.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord error: {error}"+Fore.RESET)    
    else:
        print(f"{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}{error_str}"+Fore.RESET)

if __name__ == "__main__":
    chosen_token = config["accounts"][token_index - 1]
    Init(chosen_token)