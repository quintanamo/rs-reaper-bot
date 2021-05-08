import discord
import random
import math

# get token from file
f = open('token.txt', 'r')
token = f.readline()

# list of possible bosses
bossList = {
    'Ambassador': {'min': 2, 'max': 2},
    'Araxxi': {'min': 3, 'max': 4},
    'The Barrows Brothers': {'min': 4, 'max': 15},
    'Barrows: Rise of the Six': {'min': 3, 'max': 4},
    'Black stone dragon': {'min': 2, 'max': 2},
    'Chaos Elemental': {'min': 2, 'max': 5},
    'Commander Zilyana': {'min': 10, 'max': 15},
    'Corporeal Beast': {'min': 5, 'max': 10},
    'Dagannoth Kings': {'min': 10, 'max': 15},
    'General Graardor': {'min': 10, 'max': 15},
    'Giant Mole': {'min': 3, 'max': 8},
    'Gregorovic': {'min': 5, 'max': 10},
    'Har-Aken': {'min': 1, 'max': 2},
    'Helwyr': {'min': 5, 'max': 10},
    'Kalphite King': {'min': 10, 'max': 15},
    'Kalphite Queen': {'min': 4, 'max': 10},
    'King Black Dragon': {'min': 4, 'max': 14},
    'Kree\'arra': {'min': 10, 'max': 15},
    'K\'ril Tsutsaroth': {'min': 10, 'max': 15},
    'Legiones': {'min': 10, 'max': 15},
    'The Magister': {'min': 3, 'max': 7},
    'Nex': {'min': 5, 'max': 10},
    'Nex: Angel of Death': {'min': 3, 'max': 6},
    'Queen Black Dragon': {'min': 5, 'max': 10},
    'Raksha, the Shadow Colossus': {'min': 3, 'max': 4},
    'Rex Matriarchs': {'min': 10, 'max': 15},
    'Solak': {'min': 2, 'max': 4},
    'Seiryu the Azure Serpent': {'min': 2, 'max': 2},
    'Telos': {'min': 3, 'max': 4},
    'The Twin Furies': {'min': 5, 'max': 10},
    'TzTok-Jad': {'min': 1, 'max': 2},
    'Vindicta & Gorvek': {'min': 5, 'max': 10},
    'Vorago': {'min': 3, 'max': 4}
}

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
            bosses = list(bossList.keys())
            task = bosses[random.randrange(len(bosses))]
            numberToKill = random.randint(bossList[task]['min'], bossList[task]['max'])
            if(len(commands) > 2 and commands[2].lower() == 'extend'):
                numberToKill = (1.5 * numberToKill) + 2
                numberToKill = math.floor(numberToKill)
            numberString = 'souls'
            if numberToKill == 1:
                numberString = 'soul'
            image = ''.join(e for e in task if e.isalnum())
            image = 'images/' + image.lower() + '.png'
            print(image)
            #await message.channel.send('Collect souls from {task} for me.')
            await message.channel.send(file=discord.File(image), content="Collect " + str(numberToKill) + " " + numberString + " from " + task + " for me.")

client.run(token)
# https://discord.com/api/oauth2/authorize?client_id=840438597089624065&permissions=34816&scope=bot