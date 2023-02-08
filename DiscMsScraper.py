import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '!', intents=intents)


with open(r'C:\Users\dzn16\OneDrive\Área de Trabalho\teste\allMangas_name.txt', encoding="utf8") as a:
    contents = a.read()
    nameLinks = contents.split(',')

with open(r'C:\Users\dzn16\OneDrive\Área de Trabalho\teste\top10.txt', encoding="utf8") as b:
    contents = b.read()
    top = contents.split(',')

with open(r'C:\Users\dzn16\OneDrive\Área de Trabalho\teste\names.txt', encoding="utf8") as f:
    contents = f.read()
    names1 = contents.split(',')


# command to search all the manga names
# I have to slice the list like this because message in discord have a max lenght of 2000
slice_list = len(names1) // 50
@bot.command()
async def names(ctx):
    temp = 0
    slice = 50

    loop_lista = (len(names1) // 50)

    for i in range((len(names1) // 50)):
        await ctx.send('\n'.join(names1[temp:slice]))
        temp += 50
        slice += 50

# command to search for manga


@bot.command()
async def search(ctx, *, message: str):
    try:
        for item in nameLinks:
            if message.lower() in item.lower():
                await ctx.send(item)
    except:
        await ctx.send(f"Error! No manga named {message}. Type !names to see manga titles.")

# command to check all the commands

@bot.command()
async def commands(ctx):
    await ctx.send("""**!search**, **!names**, **!top10**

**!names** - to see manga titles.
**!search** - <manga name> EX: !search naruto, !search one piece.
**!top10** - top 10 most viewed.
""")

# command for top 10


@bot.command()
async def top10(ctx):
    await ctx.send('\n'.join(top))


# this check if someone tried a command that doesn't exist.
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'{error}, use **!commands** to see commands.')

print('------ Bot running ------')

if __name__ == '__main__':
    import config
    bot.run(config.token)

