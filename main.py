import discord
from random import randrange

# get token from file
f = open('token.txt', 'r')
token = f.readline()

# list of possible bosses
bossList = [
    'Ambassador',
    'Araxxi',
    'The Barrows Brothers',
    'Barrows: Rise of the Six',
    'Black stone dragon',
    'Chaos Elemental',
    'Commander Zilyana',
    'Corporeal Beast',
    'Dagannoth Kings',
    'General Graardor',
    'Giant Mole',
    'Gregorovic',
    'Har-Aken',
    'Helwyr',
    'Kalphite King',
    'Kalphite Queen',
    'King Black Dragon',
    'Kree\'arra',
    'K\'ril Tsutsaroth',
    'Legiones',
    'The Magister',
    'Nex',
    'Nex: Angel of Death',
    'Queen Black Dragon',
    'Raksha, the Shadow Colossus',
    'Rex Matriarchs',
    'Solak',
    'Seiryu the Azure Serpent',
    'Telos',
    'The Twin Furies',
    'TzTok-Jad',
    'Vindicta & Gorvek',
    'Vorago'
]

client = discord.Client()

@client.event
async def on_ready():
    print('Started bot as user {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!reaper'):
        commands = message.content.split()
        if(commands[1].lower() == 'task'):
            task = bossList[randrange(len(bossList))]
            print(task)
            image = ''.join(e for e in task if e.isalnum())
            image = 'images/' + image.lower() + '.png'
            print(image)
            #await message.channel.send('Collect souls from {task} for me.')
            await message.channel.send(file=discord.File(image), content="Collect souls from " + task + " for me.")

client.run(token)
# https://discord.com/api/oauth2/authorize?client_id=840438597089624065&permissions=34816&scope=bot