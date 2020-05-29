import asyncio
import discord
from discord.ext import commands
import random

app = commands.Bot(command_prefix='PBOT')

token = "NzE1NTQwOTYzMzIxNDQ2NDEy.XtBocg.kHPLc7MvWeV-NKsoO7YR7P9fsUY"
calcResult = 0

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("파이썬 봇 실행중")
    await app.change_presence(status=discord.Status.online, activity=game)

@app.command(pass_context=True)
async def randomNum(ctx, num1, num2):
    picked = random.randint(int(num1), int(num2))
    await ctx.send('뽑힌 숫자는 : '+str(picked))

@app.event
async def on_message(message):
    await app.process_commands(message)
    if message.author.bot:
        return None
    if message.content == "PBOT출력":
        await message.channel.send("Python Bot에 의해 출력됨.")
    if message.content.startswith("PBOT1부터10"):
        for x in range(10):
            await message.channel.send(x+1)
    if message.content.startswith("곰용계산"):
        global calcResult
        param = message.content.split()
        try:
            if param[1].startswith("더하기"):
                calcResult = int(param[2])+int(param[3])
                await message.channel.send("**더하기결과** : "+str(calcResult))
            if param[1].startswith("빼기"):
                calcResult = int(param[2])-int(param[3])
                await message.channel.send("**빼기결과** : "+str(calcResult))
            if param[1].startswith("곱하기"):
                calcResult = int(param[2])*int(param[3])
                await message.channel.send("**곱하기결과** : "+str(calcResult))
            if param[1].startswith("나누기"):
                calcResult = int(param[2])/int(param[3])
                await message.channel.send("**나누기결과** : "+str(calcResult))
        except IndexError:
            await message.channel.send("무슨 숫자를 계산할지 알려주세요.")
        except ValueError:
            await message.channel.send("숫자로 넣어주세요.")
        except ZeroDivisionError:
            await message.channel.send("You can't divide with 0.")

app.run(token)
