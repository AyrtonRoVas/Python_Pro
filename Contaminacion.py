import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='o', intents=intents)
@bot.event
async def en_lines():
    print('Tu bot {bot.user} esta en linea')
    
@bot.command()
async def e (ctx,*,mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if mensaje == 'que es la contaminacion?':
        await ctx.send('Es la alteración del medio ambiente por sustancias dañinas.')
        
    elif mensaje == 'que tipos de contaminacion existen?':
        
        await ctx.send('Aire, agua, suelo, visual, acústica y térmica.')
        
    elif mensaje == 'que causa la contaminacion del aire?':
            
        await ctx.send('Humo de fábricas, autos y quema de basura.')

    elif mensaje == 'que contamina el agua?':

        await ctx.send('Desechos industriales, basura y químicos.')

    elif mensaje == 'como se contamina el suelo?':

        await ctx.send('Con pesticidas, basura y productos tóxicos.')

    elif mensaje == 'que efectos tiene la contaminacion?':

        await ctx.send('Daños a la salud, muerte de animales y cambio climático.')

    elif mensaje == 'que es la contaminacion acustica?':

        await ctx.send('Es el exceso de ruido que afecta a personas y animales.')

    elif mensaje ==  'como afecta la contaminacion a la salud?':

        await ctx.send('Causa enfermedades respiratorias, alergias y estrés.')

    elif mensaje == 'que podemos hacer para evitar la contaminacion?':

        await ctx.send('Reciclar, usar transporte público y no tirar basura.')

    elif mensaje == 'que es reciclar?':

        await ctx.send('Reutilizar materiales para no contaminar el ambiente.')

        
token = 'MTM3NTI2ODQ3MTU5NTg2NDA2NA.GpTZFK.ANTK9h3pF_NmLhLv6IIWyA7SzLbdWpUtFz-Lww'

bot.run(token)