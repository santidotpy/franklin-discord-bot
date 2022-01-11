import time
import discord
import os
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.core import bot_has_permissions
from discord.ext.commands.errors import MissingRequiredArgument
import biografias
import dolar
import unidades
from help_msgs import comandos
import crypto_related
from candlestick import candles_graph, return_days_ago
import memes



description = 'Bot que permite saber el precio de un protucto con la carga impositiva en Argentina (Ej. un juego de Steam) y el precio de distintas cryptos y divisas'

bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    #print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="los mercados | ?ben for help"))


# ==== AYUDA Y BIO ====
@bot.command(description='Ayuda para ver comandos disponibles con ejemplos')
@bot_has_permissions(manage_messages=True)
async def ben(ctx):
    ayuda = comandos['ben']
    bluehelp = comandos['blue']
    tarjetahelp = comandos['tarjeta']
    cardhelp = comandos['card']
    oficialhelp = comandos['oficial']
    usdarshelp = comandos['usdars']
    taxhelp = comandos['tax']
    biohelp = comandos['bio']
    pricehelp = comandos['price']
    memes = comandos['meme']

    embed = discord.Embed(title='AYUDA', description='Guia de comandos de Franklin', color = discord.Color.red())
    # `` es para que en discord se vea como code
    embed.add_field(name='Comando', value=f'`?ben`\n`?blue`\n`?tarjeta`\n`?card`\n`?oficial`\n`?usdars`\n`?tax`\n\n`?bio`\n\n`?price`\n\n\n`?meme`', inline=True)
    embed.add_field(name='Descripcion', value=f'{ayuda}\n{bluehelp}\n{tarjetahelp}\n{cardhelp}\n{oficialhelp}\n{usdarshelp}\n{taxhelp}\n{biohelp}\n{pricehelp}\n{memes}', inline=True)

    await ctx.send(embed=embed)
    time.sleep(.15)
    await ctx.message.delete()


"""
Para saber un poco sobre la vida Franklin
"""
@bot.command(description='Te cuento un poco de la bio de Benjamin Franklin')
#@bot_has_permissions(manage_messages=True)
async def bio(ctx, idioma:str='esp'):
    description_eng = biografias.desc_eng()
    bodyeng = biografias.body_eng()
    description_esp = biografias.desc_esp()
    bodyesp = biografias.body_esp()

    if idioma == 'esp':
        embed = discord.Embed(title='Benjamin Franklin', url='https://www.biography.com/scholar/benjamin-franklin', description=description_esp, color = discord.Color.dark_green())
        embed.add_field(name='Quien era Benjamin Franklin?', value=bodyesp, inline=False)
    elif idioma == 'eng':
        embed = discord.Embed(title='Benjamin Franklin', url='https://www.biography.com/scholar/benjamin-franklin', description=description_eng, color = discord.Color.dark_green())
        embed.add_field(name='Who Was Benjamin Franklin?', value=bodyeng, inline=False)
        embed.set_footer(text='“A house is not a home unless it contains food and fire for the mind as well as the body.” Benjamin Franklin')

    embed.set_thumbnail(url='https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTY2NTIxNzUwNjAxODY4NTEx/benjamin-franklin_editedjpg.jpg')
    await ctx.send(embed=embed)
    time.sleep(.15)
    await ctx.message.delete()



# ==== FINANZAS ====
@bot.command(description='Valor del dolar blue hasta la fecha en Argentina')
@bot_has_permissions(manage_messages=True)
async def oficial(ctx):
    compra, venta, fecha = dolar.dolar_oficial()

    embed = discord.Embed(title='Precio Dolar "OFICIAL"', color = discord.Color.green())
    embed.add_field(name='Compra', value=f'${compra}', inline=True)
    embed.add_field(name='Venta', value=f'${venta}', inline=True)
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/2/23/US_one_dollar_bill%2C_obverse%2C_series_2009.jpg')
    embed.set_footer(text=fecha)
    await ctx.send(embed=embed)
    time.sleep(.15)
    await ctx.message.delete()


@bot.command(description='Valor del dolar blue hasta la fecha en Argentina')
@bot_has_permissions(manage_messages=True)
async def blue(ctx):
    compra, venta, fecha = dolar.dolar_blue()

    # discord.Embed puede tener description si se quiere
    embed = discord.Embed(title='Precio Dolar BLUE', color = discord.Color.green())
    embed.add_field(name='Compra', value=f'${compra}', inline=True)
    embed.add_field(name='Venta', value=f'${venta}', inline=True)
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/2/23/US_one_dollar_bill%2C_obverse%2C_series_2009.jpg')
    embed.set_footer(text=fecha)

    await ctx.send(embed=embed)
    time.sleep(.15)
    await ctx.message.delete()


@bot.command(description='Valor del dolar que te toma la tarjeta hasta la fecha en Argentina')
@bot_has_permissions(manage_messages=True)
async def tarjeta(ctx):
    venta, fecha = dolar.dolar_turista()

    # discord.Embed puede tener description si se quiere
    embed = discord.Embed(title='Precio Dolar TARJETA', color = discord.Color.green())
    embed.add_field(name='Precio', value=f'${venta}', inline=True)
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/2/23/US_one_dollar_bill%2C_obverse%2C_series_2009.jpg')
    embed.set_footer(text=fecha)

    await ctx.send(embed=embed)
    time.sleep(.15)
    await ctx.message.delete()


@bot.command(description='Convierte pesos argentinos a dolares a valor tarjeta')
@bot_has_permissions(manage_messages=True)
async def card(ctx, usd : float):
    venta, fecha = dolar.dolar_turista()
    venta = round(float(venta), 3)
    convert = round(usd * venta, 2)
    author = ctx.message.author

    embed = discord.Embed(title='Dolares a Pesos Argentinos', description=f'A precio Dolar Tarjeta\n\nRequested by {author.mention}', color = discord.Color.green())
    embed.add_field(name='🇺🇸 Dolares', value=f'${usd} USD', inline=True)
    embed.add_field(name='🇦🇷 Pesos Argentinos', value=f'${convert} ARS', inline=True)
    embed.set_thumbnail(url='https://pbs.twimg.com/media/Et_Da3QXcAMm8jE?format=jpg&name=medium')
    embed.set_footer(text=f'$1 USD = ${venta} ARS | {fecha[0 : 10]}')

    await ctx.send(embed=embed)
    time.sleep(.15)
    await ctx.message.delete()


@bot.command(description='Convierte pesos argentinos a dolares a valor blue')
@bot_has_permissions(manage_messages=True)
async def usdars(ctx, usd : float):
    venta = dolar.dolar_blue()[1]
    venta = round(float(venta), 3)
    author = ctx.message.author

    embed = discord.Embed(title='Dolares a Pesos Argentinos', description=f'A precio Dolar Blue\n\nRequested by {author.mention}', color = discord.Color.green())
    embed.add_field(name='🇺🇸 Dolares', value=f'${usd} USD', inline=True)
    embed.add_field(name='🇦🇷 Pesos Argentinos', value=f'${usd * venta} ARS', inline=True)
    embed.set_footer(text=f'$1 USD = ${venta} ARS')

    await ctx.send(embed=embed)
    time.sleep(.15)
    await ctx.message.delete()


@bot.command(description='Convierte el valor de algo a lo que pasaria costar por los impuestos')
@bot_has_permissions(manage_messages=True)
async def tax(ctx, pesos : float):
    imp = 1.65
    total = round(pesos * imp, 2)
    author = ctx.message.author
    fotito = 'https://pbs.twimg.com/media/Et_Da3QXcAMm8jE?format=jpg&name=medium'

    
    embed = discord.Embed(title=f'Impuestos en Argentina 🇦🇷',
                          description=f'Conversion con la carga impositiva argentina\n\nRequested by {author.mention}',
                          color = discord.Color.blue())
    embed.add_field(name='Sin Impuestos', value=f'${pesos} ARS', inline=True)
    embed.add_field(name='Con Impuestos', value=f'${total} ARS', inline=True)
    embed.set_thumbnail(url=fotito)
    embed.set_footer(text=f'Taxation Is Theft')
    
    await ctx.send(embed=embed)
    time.sleep(.15)
    await ctx.message.delete()


@bot.command(description='Embed')
@bot_has_permissions(manage_messages=True)
async def price(ctx, from_crypto:str, to_crypto:str='USDT'):
    # in crypto we trust
    data = crypto_related.crypto_binancio(from_crypto,to_crypto)

    from_crypto = from_crypto.upper()
    to_crypto = to_crypto.upper()
    
    fotito = crypto_related.get_coin_img(from_crypto)
    url = crypto_related.get_url_project(from_crypto)
    full_name = crypto_related.crypto_name(from_crypto)

#   === Implementacion Candlesticks ===

    file = discord.File('src/graph.png', filename='graph.png') # Discord para los embed pide hacer esto para poder mandar una foto que no sea http
    current_day = return_days_ago()
    candles_graph(start_date=current_day, currency1=from_crypto, currency2=to_crypto, time_interval='1h')
    time.sleep(.55)


    embed = discord.Embed(title=f'Price of {full_name}',
                          url=url, description=f'1 **{from_crypto}** = {data} **{to_crypto}**',
                          color = discord.Color.orange())

    embed.set_thumbnail(url=fotito)

    embed.set_image(url='attachment://graph.png') # el attachment de la imagen local

    embed.set_footer(text='Source: Binance')

    await ctx.send(file=file, embed=embed)
    time.sleep(.15)
    await ctx.message.delete()



# ==== CONVERCIONES ====

@bot.command(description='Convierto pies a metros')
async def ft2m(ctx, numero : float):
    resultado = unidades.feet_and_meter(numero, 'ft')
    embed = discord.Embed(title='Pies a Metros', color = discord.Color.dark_magenta())
    embed.add_field(name='Conversion', value=resultado, inline=True)
    
    await ctx.send(embed=embed)


@bot.command(description='Convierto metros a pies')
async def m2ft(ctx, numero : float):
    resultado = unidades.feet_and_meter(numero, 'm')
    embed = discord.Embed(title='Metros a Pies', color = discord.Color.dark_magenta())
    embed.add_field(name='Conversion', value=resultado, inline=True)
    
    await ctx.send(embed=embed)


@bot.command(description='Convierto pulgadas a centimetros')
async def in2cm(ctx, numero : float):
    resultado = unidades.inches_and_cm(numero, '"')
    embed = discord.Embed(title='Pulgadas a Centimetros', color = discord.Color.dark_magenta())
    embed.add_field(name='Conversion', value=resultado, inline=True)
    
    await ctx.send(embed=embed)


@bot.command(description='Convierto centimetros a pulgadas')
async def cm2in(ctx, numero : float):
    resultado = unidades.inches_and_cm(numero, 'cm')
    embed = discord.Embed(title='Centimetros a Pulgadas', color = discord.Color.dark_magenta())
    embed.add_field(name='Conversion', value=resultado, inline=True)
    
    await ctx.send(embed=embed)


# ==== CALCULOS ====

@bot.command(description='Multiplico 2 numeros dados')
async def multi(ctx, num1:float, num2:float=MissingRequiredArgument):
    try:
        resultado = num1 * num2
        await ctx.send(resultado)
    except TypeError:
        await ctx.send('Tenes que pasarme 2 numeros para que te multiplique')


@bot.command(description='Divido 2 numeros dados')
async def div(ctx, num1:float, num2:float=MissingRequiredArgument):
    try:
        resultado = round(num1 / num2, 3)
        await ctx.send(resultado)
    except TypeError:
        await ctx.send('Tenes que pasarme 2 numeros para que divida')
    except ZeroDivisionError:
        await ctx.send('Estas tratando de dividir por 0')



# ==== RANDOM ====

@bot.command(description='Meme random')
@bot_has_permissions(manage_messages=True)
async def meme(ctx):
    data = memes.meme()

    embed = discord.Embed(title='MEME', color = discord.Color.dark_red())
    embed.set_image(url=data)

    await ctx.send(embed=embed)
    time.sleep(.15)
    await ctx.message.delete()




bot.run(os.environ['DISCORD_TOKEN'])