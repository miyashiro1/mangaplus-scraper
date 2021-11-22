from discord.ext import commands

"""names, final, dic  are global variables from allMangas.py"""

bot = commands.Bot(command_prefix='!')

nameLinksRead = open(r'C:****\allMangas_name.txt')
nameLinksRead = nameLinksRead.read()
nameLinks = nameLinksRead.split(',')

topRead = open(r'C:\******\top10.txt')
topRead = topRead.read()
top = topRead.split(',')

namesRead = open(r'C:\*****\names.txt')
namesRead = namesRead.read()
names1 = namesRead.split(',')

@bot.command()
async def names(ctx):
    await ctx.send('\n'.join(names1[:50]))
    await ctx.send('\n'.join(names1[50:]))

@bot.command()
async def search(ctx, *, message: str):
    try:
        for item in nameLinks:
            if message.lower() in item.lower():
                await ctx.send(item)
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
    await ctx.send('\n'.join(top))


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'{error}, use **!commands** to see commands.')

print('------ Bot running ------')

if __name__ == '__main__':
    import config
    bot.run(config.token)

