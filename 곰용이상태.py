import asyncio
import discord

app = discord.Client()

token = "NzE1NTQwOTYzMzIxNDQ2NDEy.XtBocg.kHPLc7MvWeV-NKsoO7YR7P9fsUY"

@app.event
async def on_ready():
    print("===================\n다음으로 로그인합니다")
    print("봇이름 :" ,app.user.name)
    print("봇 CLINT :" ,app.user.id)
    print("===================")
    game = discord.Game("Airk Gy ER#7777 (곰용) 제작")
    await app.change_presence(status=discord.Status.online, activity=game)

@app.event
async def on_message(message, false=None):
    if message.content.startswith("!봇상태"):
        embed=discord.Embed(title="```                 곰용봇 상태                ```", description="(봇-개발자-상태)", color=0x00ff56)
        embed.set_author(name="개발자 자체 PC(본쳬) 부품 온도", url="", icon_url="https://cdn.discordapp.com/attachments/704981754116833340/715941522012635156/download20200504131630.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/704981754116833340/715941524751384707/download20200504193638.png")
        embed.add_field(name="CPU온도", value="**평균 : 34°**", inline=false)
        embed.add_field(name="GPU온도", value="**평균 : 27°**", inline=false)
        embed.add_field(name="PC자체온도", value="**평균 : 38°**", inline=false)
        embed.add_field(name="RAM온도", value="**평균 : 21°**", inline=false)
        embed.set_footer(text="봇-제작 by.곰용")
        await message.channel.send(embed=embed)

app.run(token)
