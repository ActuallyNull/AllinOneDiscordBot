import HypixelApi
import discord
from discord.ext import commands, tasks
import time
import os
import requests
import random
import ElonMuskJet
from dotenv import load_dotenv

# importing environmental vars
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
APP_ID = os.getenv("APP_ID")
PUB_KEY = os.getenv("PUBLIC_KEY")
GUILD_ID = os.getenv("GUILD_ID")
GENERAL_CHAN_ID = os.getenv("CHANNEL_GENERAL_ID")
#finished importing .env vars

intents = discord.Intents.all()
activity = discord.Activity(name="being awesome losers", type = discord.ActivityType.streaming)

bot = discord.Bot(intents=intents, activity=activity)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    channel = bot.get_channel(956302622170701946)
    HypixelApi.apiRequestGeneral()
    await channel.send(HypixelApi.apiRequestSpecific('date'))
    checkSkyblockDay.start()

@bot.slash_command(description="says \"Hello!\"")
async def hello(ctx):
    await ctx.respond("Hello!")

async def printMessages():
        channel = bot.get_channel(956302622170701946)
        await channel.send("<@520374895394291714> Time for Fallen Star Cult, " + HypixelApi.apiRequestSpecific('date'))

@tasks.loop(seconds=10)
async def checkSkyblockDay():
    data = HypixelApi.apiRequestGeneral()
    sbDay = data['day']
    happened = False
    if sbDay == 7:
        await printMessages()
        happened = True
        while happened == True:
            time.sleep(1200)
            happened = False
    elif sbDay == 14:
        await printMessages()
        happened = True
        while happened == True:
            time.sleep(1200)
            happened = False
    elif sbDay == 21:
        await printMessages()
        happened = True
        while happened == True:
            time.sleep(1200)
            happened = False
    elif sbDay == 28:
        await printMessages()
        happened = True
        while happened == True:
            time.sleep(1200)
            happened = False
    else:
        print('it is not time 😔 ' + HypixelApi.apiRequestSpecific('date') + " " + HypixelApi.apiRequestSpecific('time'))



@bot.slash_command(description="gives you the weather no shit sherlock")
async def weather(ctx, place: str):
    repsonse = requests.get('http://api.weatherstack.com/current?access_key=1261911b962a009e45e7d4e65d687c92&query=' + place + "&units=m")
    datajson = repsonse.json()
    await ctx.respond("weather for " + place)
    percentSign = "%"
    txt = u'In %s,%s it is the %s. It is %s℃ and %s. It feels like %s℃, the humidity levels are %s%%, there is a %s%% chance of precipitation, the clouds cover %s%% of the sky, you can see for %skm with a wind speed of %skm/m' % (datajson['location']['name'],datajson['location']['country'],datajson['location']['localtime'],datajson['current']['temperature'],datajson['current']['weather_descriptions'],datajson['current']['feelslike'],datajson['current']['humidity'],datajson['current']['precip'],datajson['current']['cloudcover'],datajson['current']['visibility'],datajson['current']['wind_speed'])
    fullTxt = txt.format(percentSign, percentSign)
    await ctx.respond(fullTxt)
    weatherIconStr = u'%s' % (datajson['current']['weather_icons'])
    await ctx.respond(weatherIconStr)

@bot.slash_command(description="tracks elon musk's cool private jet")
async def trackelonmusk(ctx):
    await ctx.respond(ElonMuskJet.flight_data)

@bot.slash_command(guild_ids=[GUILD_ID], description="Kills bot and makes it unusable")
async def close(ctx):
    await ctx.respond("i fricking died bro :sob:")
    await bot.close()


@bot.slash_command(description="addition cmon you know math")
async def add(ctx, num1: int, num2: int):
  sum = num1 + num2
  await ctx.respond(f"{num1} plus {num2} is {sum}.", ephemeral = True)

@bot.command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}")

@bot.slash_command(description="Sends the best team in this year's world cup")
async def betterteam(ctx):
    await ctx.respond("The best team is obviously Morocco!")
    await ctx.respond("What did you think, that I wasn't biased?", ephemeral = True)

@bot.slash_command(description="Copies you")
async def copyme(ctx, txt: str):
    await ctx.respond(txt)

@bot.slash_command(description="Annoy someone",guild_ids=[GUILD_ID])
async def send_message(ctx, user_id: str, message: str):
    user = bot.get_user(int(user_id))
    try:
        await user.send(message)
        await ctx.respond("Message sent successfully!", ephemeral = True)
    except:
        await ctx.respond("Failed to send message. User probably has closed DMs", ephemeral = True)

@bot.slash_command(name="katana", description="sends you a katana you can copy and paste to stab your friends!")
async def katana(ctx):
    await ctx.respond("▬▬ι═══════ﺤ  Now go, dear adventurer, and vanquish your foes!")


@bot.slash_command(description="long katana")
async def long_katana(ctx):
    await ctx.respond("▬▬ι══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════ﺤ Here is your **extra** long katana. Why do you need this exactly?")

@bot.slash_command(name="whoami",description="testing")
async def whoishe (ctx,user:discord.Member):
  role = discord.utils.get(ctx.guild.roles, name="CoolPeople")
  user_id = ctx.author.id
  if role in user.roles:
        await ctx.respond(f"<@{user_id}> is one of the cool kids :sunglasses:")
  else:
    await ctx.respond("Somone who is **not** one of the cool kids")
    
@bot.slash_command(name="betteroption", description="Chooses the better option between two options given by the user")
async def betterOption(ctx, option1: str, option2: str):
    randomizer = random.randint(1,2)

    if option1 == "Technoblade":
        await ctx.respond(f"Legends never die, Technoblade is the best, May he defeat God in his final battle :pig: :dove:")
    elif option2 == "Technoblade":
        await ctx.respond(f"Legends never die, Technoblade is the best, May he defeat God in his final battle :pig: :dove:")
    elif option1 == "technoblade":
        await ctx.respond(f"Legends never die, Technoblade is the best, May he defeat God in his final battle :pig: :dove:")
    elif option2 == "technoblade":
        await ctx.respond(f"Legends never die, Technoblade is the best, May he defeat God in his final battle :pig: :dove:")
    elif option1 == "Morocco":
        await ctx.respond(f"MOROCCO FOREVER :flag_ma::flag_ma::flag_ma:")
    elif option2 == "Morocco":
        await ctx.respond(f"MOROCCO FOREVER :flag_ma::flag_ma::flag_ma:")
    elif option1 == "morocco":
        await ctx.respond(f"MOROCCO FOREVER :flag_ma::flag_ma::flag_ma:")
    elif option2 == "morocco":
        await ctx.respond(f"MOROCCO FOREVER :flag_ma::flag_ma::flag_ma:")
    elif randomizer == 1:
        await ctx.respond(f"Obviously {option1} is the better option from both of them")
    elif randomizer == 2:
        await ctx.respond(f"Obviously {option2} is the better option from both of them")
    else:
        await ctx.respond("Try something else maybe?", ephemeral = True)
@bot.event
async def on_message(message):
    channel = bot.get_channel(956302622170701946)
    if message.content.startswith("help"):
        i = 1
        while i < 1000:
            await message.author.send("lmao")
            i += 1
        await message.author.send('no')
    if message.content.startswith("die"):
        await channel.send("*dies*")
        await bot.close()

if __name__ == '__main__':
    bot.run(TOKEN)