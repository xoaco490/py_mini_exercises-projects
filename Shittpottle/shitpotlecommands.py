import discord
import os
import json
import random
import io
import aiohttp
from discord.ext import commands
from discord.utils import get
TOKEN = 'ACA VA TOKEN'

#TODO IDEAS:
#Alternar entre frases para errores/on

#Ubbi Dubbi
def ubbi_dubbi(sentence):
    vowels_dict = {i: f"ub{i}" for i in "aeiou"}
    return sentence.lower().translate(str.maketrans(vowels_dict))
#Pig Latin
def pig_latin(sentence):
    result = ""
    for word in sentence.split():
        result += word[1:] + word[0] + "ay "
    return result
bot = commands.Bot(command_prefix='=')

@bot.command()
async def ubbi(ctx, *, arg):
    await ctx.send(ubbi_dubbi(arg))
@bot.command()
async def pig(ctx, *, arg):
    await ctx.send(pig_latin(arg))
@bot.command()
async def holp(ctx):
    await ctx.send("Hola soy el bot mas poronga del universo mis habilidades son:\n=pig (oracion/palabra a traducir al pig)\n=ubbi (oracion/palabra a traducir a ubbi dubbi)\n=dog (para foto aleatoria de perro)\n=breed (breed + la raza maestra del perro (por ejemplo collie)\n=dolar si te queres morir de tristeza\n=echo (repite mensajes para decir los mensajeros son putos)")

@bot.command()
async def dog(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://dog.ceo/api/breeds/image/random") as r:
            res = await r.json()
            await ctx.send(res['message'])
            
@bot.command()
async def breed(ctx, *, arg):
    raza = arg
    raza = raza.lower()
    async with aiohttp.ClientSession() as session:
        async with session.get("https://dog.ceo/api/breed/"+ raza +"/images/random") as r:
            res = await r.json()
            if res['status'] == "success":
                await ctx.send(res['message'])
            else:
                await ctx.send("upa en algun lugar la cagamo")
        async with session.get("https://dog.ceo/api/breed/"+ raza +"/list") as r:
            res = await r.json()
            if res['status'] == "success":
                await ctx.send("las sub razas de el "+ raza + " son las siguientes:")
                await ctx.send(res['message'])
                await ctx.send("recuerda que puedes buscar las sub razas con el comando =subBreed")
            else:
                await ctx.send("definitivamente la cagamos")


@bot.command()
async def subBreed(ctx, *, args):
    raza = args
    raza = raza.lower()
    raza = raza.split()
    async with aiohttp.ClientSession() as session:
        async with session.get("https://dog.ceo/api/breed/"+raza[0]+"/"+raza[1]+"/images/random") as r:
            res = await r.json()
            if res['status'] == "success":
                await ctx.send(res['message'])
            else:
                await ctx.send("upa en algun lugar la cagamo")


            
            



@bot.command()
async def dolar(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("free currconv private api") as r:
            res = await r.json()
            await ctx.send(res['USD_ARS'])
            await ctx.send("y nisiquira es el blue, estamos en el horno")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel("General ID")#GENERAL
    await channel.send("Y vos che {0.mention}?".format(member))
    
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel("General ID")#GENERAL
    await channel.send("Pica de aca la concha tuya {0.mention}".format(member))

@bot.event
async def  on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("NO ESCRIBISTE NINGUN ARGUMENTO MOGOLICO")

@bot.command()
async def echo(ctx, *, message=None):
     message = message or "Boludo si no me tiras mensaje no puedo decir nada"
     await ctx.message.delete()
     await ctx.send(message)

@bot.command()
async def pingo(ctx):
    await ctx.send(f'Pong!\n{round(bot.latency*1000)}ms')
    await ctx.send("Servidor chileno pete la concha de la lora")


#COMO MIERDA SE CONSGUEN VARIOS MENSAJES?????

#@bot.event
#async def on_message(message):
#    if message.content.startswith('$greet'):
#        channel = message.channel
#        await channel.send('Say hello!')
#
#        def check(m):
#            return m.content == 'hello' and m.channel == channel
#
#        msg = await client.wait_for('message', check=check)
#        await channel.send('Hello {.author}!'.format(msg))
#@bot.event
#async def on_message(message):
#    def check(m):
#        return m.channel == message.channel and m.author != client.user
#    if message.content.startswith("!order"):
#        channel = message.channel
#        await channel.send("in game name")
#        in_game_name = await client.await_for('message', check=check)
#        await channel.send("tu nombre ingame es: "+in_game_name)
#        print(in_game_name)




#Aliases sirve para llamar al comando de diferentes formas
@bot.command(aliases=['bola8', 'test', '8ball'])
async def _8ball(ctx, *, question):
    responses = ["Obvio papa.",
                "Olvidate que siiii mi rey.",
                "Sin lugar a duda perro.",
                "Si.",
                "¿Si?.",
                "Puede de ser. Ndeaa mandaba esa.",
                "Seguro que si.",
                "The game.",
                "Yes.",
                "Todo a punta a que sn.",
                "Que se yo.",
                "Pregunta mas tarde.",
                "Si te lo digo me vas a cagar a piñas.",
                "NO ROMPAS LA PIJA.",
                "Pensalo mas fuerte y preguntame despues.",
                "Ni ahi.",
                "Mi veredicto es no.",
                "Arma es aquel objeto construido específicamente para el ataque o defensa ... mal podría extenderse ese concepto a objetos que no encuadran en esa categoría sin recaer en una interpretación analógica in malam parte vedada por el principio de legalidad (art. 18, CN).",
                "Ni en pedo.",
                "Ojalá.",
                "La fortaleza de tu agravio demuestra la debilidad de tu argumento."]
    await ctx.send(f'Pregunta: {question}\nRespuesta: {random.choice(responses)}')


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Viva peronia'))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    channel = bot.get_channel("General ID")
    await channel.send("Que onda larvass")

bot.run(TOKEN)