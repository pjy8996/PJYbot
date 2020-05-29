import asyncio
import discord

app = discord.Client()

token = "NzE1NTQwOTYzMzIxNDQ2NDEy.XtBocg.kHPLc7MvWeV-NKsoO7YR7P9fsUY"

@app.event
async def on_ready():
    print("===================\n다음으로 로그인합니다")
    print("봇이름 :" ,app.user.name)
    print("봇CLIENT :" ,app.user.id)
    print("===================")
    game = discord.Game("Airk Gy ER#7777 (곰용) 제작")
    await app.change_presence(status=discord.Status.online, activity=game)

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "곰용아":
        await message.channel.send("넹!")

app.run(token)
