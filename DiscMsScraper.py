from discord.ext import commands
from allMangas import mangaPlus, names, dic
from topTen import top10, resultado

"""names, final, dic  are global variables from allMangas.py"""

def read_token():
    with open("token.txt", 'r') as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

mangaPlus()
top10()

bot = commands.Bot(command_prefix='!')


@bot.command()
async def search(ctx, *, message: str):
    res = []
    try:
        for key, value in dic.items():
            if message.lower() in key.lower():
                res.append(f'{key}: {value}')
        await ctx.send('\n'.join(res))
    except:
        await ctx.send(f"Error! No manga named {message}. Type !names to see manga titles.")

@bot.command()
async def commands(ctx):
    await ctx.send("""**!search**, **!names**, **!top10**

**!names** - to see manga titles.
**!search** - <manga name> EX: !search naruto, !search one piece.
**!top10** - top 10 most viewed.
""")

@bot.command()
async def top10(ctx):
    await ctx.send('\n'.join(resultado))

@bot.command()
async def names(ctx):
    new_names = []
    for i in dic.keys():
        new_names.append(i)
    await ctx.send('\n'.join(new_names))

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'{error}, use **!commands** to see commands.')

bot.run(token)