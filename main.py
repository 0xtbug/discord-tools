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

with open('config.json') as f:
    config = json.load(f)
    
token = config.get("token")

def scale(time):
    defined = 60
    for unit in ["m", "h"]:
        if time < defined:
            return f"{time:.2f}{unit}"
        time /= defined

def Init():
    if config.get('token') == "token-here":
        os.system('cls')
        print(f"\n\n{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}You didnt put your token in the config.json file\n\n"+Fore.RESET)
        exit()
    else:
        token = config.get('token')
        try:
            client.run(token, bot=False, reconnect=True)
            os.system(f'Discord LevelUpBot')
        except discord.errors.LoginFailure:
            print(f"\n\n{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Token is invalid\n\n"+Fore.RESET)
            exit()

def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = []
        for line in file:
            lines.append(line)
        return lines

os.system('cls')
result = pyfiglet.figlet_format("""Discord Tools""", font = "slant"  )
print (colored(result, 'yellow'))
ip = requests.get('https://api.ipify.org').text
x = datetime.datetime.now(pytz.timezone("Asia/Jakarta"))
print (colored('''Created by: YSA DEV - Recoded by 0xtbug''', 'cyan', attrs=['bold']))
print (colored('===========================================================', 'green', attrs=['bold']))
print (colored(f"Ξ START           : {x.strftime('%d-%m-%Y %H:%M:%S')} \nΞ Your IP         : {ip} ", 'green', attrs=['bold']))
print (colored('=========================================================== \n', 'green', attrs=['bold']))
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
async def lp(ctx,amount: int):
    await ctx.message.delete()
    msgsend = amount
    success_count = 0
    fail_count = 0
    print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Sending {Fore.WHITE}{msgsend}{Fore.LIGHTBLACK_EX} messages to {Fore.WHITE}#{ctx.channel.name}{Fore.LIGHTBLACK_EX} channel in {Fore.WHITE}{ctx.guild.name}{Fore.LIGHTBLACK_EX} server")
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Estimated Time: {Fore.WHITE}{scale(msgsend)}\n")
    while msgsend > 0:
        x = datetime.datetime.now(pytz.timezone("Asia/Jakarta"))
        try:
            msgsend -= 1
            success_count += 1
            print(f"{Fore.WHITE}[{Fore.GREEN}{x.strftime('%d-%m-%Y %H:%M:%S')}{Fore.WHITE}] {Fore.LIGHTBLACK_EX}Message sent! | Messages left to send: {Fore.WHITE}{msgsend} {Fore.LIGHTBLACK_EX}| Estimated Time: {Fore.WHITE}{scale(msgsend)}")
            if msgsend == 0:
                print(f"\n{Fore.WHITE}[{Fore.GREEN}{x.strftime('%d-%m-%Y %H:%M:%S')}{Fore.WHITE}] {Fore.LIGHTBLACK_EX}All messages was sent. Successful: {Fore.WHITE}{success_count} {Fore.LIGHTBLACK_EX}| Failed: {Fore.WHITE}{fail_count}")
            if choicel == "ID":
                kata = read_file('kataid.txt')
                output = random.choice(kata)
            elif choicel == "EN":
                kataen = read_file('kataen.txt')
                output = random.choice(kataen)
            else:
                output = "Invalid input"
            await ctx.send(output)
        except:
            fail_count += 1
            print(f"{Fore.WHITE}[{Fore.RED}{x.strftime('%d-%m-%Y %H:%M:%S')}{Fore.WHITE}] {Fore.LIGHTBLACK_EX}Cannot send message {Fore.WHITE}#{msgsend}")
            pass
        await asyncio.sleep(1)
        async for message in ctx.message.channel.history(limit=1).filter(lambda m: m.author == client.user).map(lambda m: m):
            if choicec == "Y":
                try:
                    await message.delete()
                    print(f"{Fore.WHITE}[{Fore.GREEN}{x.strftime('%d-%m-%Y %H:%M:%S')}{Fore.WHITE}] {Fore.LIGHTBLACK_EX}Success delete message {Fore.WHITE}#{msgsend}")
                except:
                    print(f"{Fore.WHITE}[{Fore.RED}{x.strftime('%d-%m-%Y %H:%M:%S')}{Fore.WHITE}] {Fore.LIGHTBLACK_EX}Cannot delete message {Fore.WHITE}#{msgsend}")
                    pass
        await asyncio.sleep(delaytime)
    return

@client.event
async def print_info():
    await client.wait_until_ready()
    print (colored('+===================== BOT START! ========================+', 'red', attrs=['bold']))
    print(f"{Fore.WHITE}[ {Fore.GREEN}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Login as: {Fore.WHITE}{client.user.name}")
    print(f"{Fore.WHITE}[ {Fore.GREEN}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Write ON DISCORD: {Fore.WHITE}\n!lp <number of messages> to Start Level UP")
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

Init()