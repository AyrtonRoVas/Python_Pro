import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def en_lines():
    print('Tu bot {bot.user} esta en linea')
    
@bot.command()
async def a (ctx,*,mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if mensaje == 'hola':
        await ctx.send('Hola, ¿cómo estás?')
        
    elif mensaje == 'bien y tu?':
        
        await ctx.send('¡Yo me encuentro Genial!')
        
    elif mensaje == 'que haces?':
            
        await ctx.send('Un poco aburrido la verdad ;(')
    
    else:
        
        await ctx.send('¿No me quieres hablar? D;')
        
token = ''
        
bot.run(token)