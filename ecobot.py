import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix ='!',intents = intents)

#retoss

retos = [
    "No utilisar plasticos por 1 semana.",
    "No utilizar el carro por un día.",
    "Plantar un árbol o una planta.",
    "Recoge la basura.",
    "Apaga las luces cuando salgas de una habitación.",
]  

@bot.command()
async def reto(ctx):
    reto_aleatorio = random.choice(retos) 
    await ctx.send(f"¡Tu reto ambiental es: {reto_aleatorio}")

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

bot.run('token')  
