from discord import Message, Member
from discord.ext import commands
from discord.ext.commands import Context
from discord.utils import get
from datetime import date
import random
import time
import discord.utils


# ---------------------------------------------- #
# ----------- BOT VARIABLES SECTION ------------ #
# ---------------------------------------------- #


TOKEN = ''  # BOT TOKEN, DO NOT SHARE
COMMAND_PREFIX = "!"

today = str(date.today())
oraUp = time.strftime("%H", time.localtime())
minutiUp = time.strftime("%M", time.localtime())
colore = 0x822434


# ---------------------------------------------- #
# ----------- BOT STARTUP SECTION ------------ #
# ---------------------------------------------- #


bot = discord.Client()
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)


# ---------------------------------------------- #
# ------------ BOT.EVENT SECTION --------------- #
# ---------------------------------------------- #


@bot.event
async def on_ready():
    print('Bot server started as nickname {0.user}'.format(bot))


# ----------------------------------------------------- #
# ------------- BOT.COMMANDS SECTION ------------------ #
# ----------------------------------------------------- #


@bot.command()
async def hello(ctx: Context):
    await ctx.channel.send(embed=discord.Embed(title="Ciao!", description="Come va?", color=colore))


@bot.command()
async def ora(ctx: Context):
    ora = int(time.strftime("%H", time.localtime()))
    minuti = time.strftime("%M")
    orario = 'Sono le ore ' + str(ora + 1) + ":" + minuti
    await ctx.channel.send(embed=discord.Embed(title="Ora", description=orario, color=colore))


@bot.command()
async def uptime(ctx: Context):
    string = 'Sono online dalle ore ' + str(int(oraUp) + 1) + ":" + minutiUp + ' del giorno ' + today
    await ctx.channel.send(embed=discord.Embed(title="Uptime", description=string, color=colore))


@bot.command()
async def roll(ctx: Context, *args):
    errore = 'I dati inseriti sono errati, utilizzare la formula "!roll LANCIdFACCE", per esempio 1d20 per un lancio di un dado a 20 facce.\n\
                                                           Il massimo di facce e lanci è 200, i valori negativi non vengono accettati.\n'
    istruzioni = 'Utilizzare la formula "!roll LANCIdFACCE", per esempio 1d20 per un lancio di un dado a 20 facce.\n' \
                 'Il massimo di facce e lanci è 200, i valori negativi non vengono accettati.\n'
    try:
        stringok = False
        stringa = args[0]
        stringok = True
        listaDadoRoll = stringa.split('d')
        if int(listaDadoRoll[0]) > 200 or int(listaDadoRoll[1]) > 200 or int(listaDadoRoll[0]) <= 0 or int(
                listaDadoRoll[1]) <= 0:
            await ctx.channel.send(embed=discord.Embed(title="Istruzioni", description=istruzioni, color=colore))
        else:
            resultStrDadi = ''
            rollSomma = 0
            for tiri in range(int(listaDadoRoll[0])):
                rollTemp = random.randint(0, int(listaDadoRoll[1]) - 1)
                resultStrDadi = resultStrDadi + ' ' + str(rollTemp + 1)
                rollSomma += rollTemp + 1
            if int(listaDadoRoll[0]) == 1:
                await ctx.channel.send(
                    embed=discord.Embed(title="Il risultato del lancio è:", description=str(rollSomma), color=colore))
            else:
                await ctx.channel.send(embed=discord.Embed(title="Il risultato del lancio è:",description=resultStrDadi + ' ' + '\n' + 'La somma è ' + str(rollSomma), color=0x822434))
    except:
        if stringok:
            await ctx.channel.send(embed=discord.Embed(title="Errore", description=errore, color=colore))
        else:
            await ctx.channel.send(embed=discord.Embed(title="Istruzioni", description=istruzioni, color=colore))


@bot.command()
async def f(ctx: Context):
    await ctx.channel.send(embed=discord.Embed(
        description='**FFFFFFFFFFFFFFFF**\n**F**\n**F**\n**F**\n**FFFFFFFFF**\n**F**\n**F**\n**F**\n**F**\n**F**',
        color=0x822434))

# ---------------------------------------------- #
# ------------ BOT.EVENT SECTION --------------- #
# ---------------------------------------------- #

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    ciao = "fh"
    if '*' in message.content:
        stringa = message.content.replace('*', 'Ə') + ' #GenderNeutrale'
        await message.channel.send(embed=discord.Embed(title="#GenderNeutrale", description=stringa, color=colore))

    if message.channel.id == 816773641572057119:
        descrizione = ""
        channel = bot.get_channel(776145787566161980)
        titolo = message.content.split("\n")
        for elemento in titolo[1:]:
            descrizione += elemento + "\n"
        await channel.send(embed=discord.Embed(title=titolo[0], description=descrizione, color=colore))

    await bot.process_commands(message)


bot.run(TOKEN)