import discord
import asyncio
import requests


client = discord.Client()

token = "ODAxNjgwODIwNjYxMzg3Mjk4.YAkNcg.AKJzQPoRqfmPd0zBI8yljlZ9Yak"

@client.event
async def on_ready():

    print(client.user.name)
    print('봇이 시작되었습니다')
    game = discord.Game("명령어가 궁금하면 -명령어")
    await client.change_presence(status=discord.Status.online, activity=game)
    twitch = "kw_on_h_j"
    name = "마크하는권혁준"
    channel = client.get.channel(802371363347103777)
    a = 0
    while True 
        headers = {'Client-ID' : '801680820661387298'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch, headers=권혁준 트위치)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                await channel.send(name + "님이 방송중입니다")
                a = 1
            except:
                a = 0
            await asyncio.sleep(5)


@client.event
async def on_message(message):
    if message.content == "-안녕":
        await message.channel.send("안녕!!")

    if message.content == "-만나서 반가워":
        await message.channel.send("나도 정말 반가워!!")

    if message.content == "-마인크래프트":
        await message.channel.send("개꿀잼")   

    if message.content == "-여기서 제일 잘생긴 사람은?":
        await message.channel.send("당연히 권혁준이지!") 

    if message.content == "-여기서 제일 잘 생긴 사람은?":
        await message.channel.send("당연히 권혁준이지!")

    if message.content == "-여기서제일잘생긴사람은?":
        await message.channel.send("당연히 권혁준이지!")
    
    if message.content == "-권혁준":
        await message.channel.send("아 제 주인님")

    if message.content == "-......":
        await message.channel.send("...........")

    if message.content == "-ㅋ":
        await message.channel.send("...........")

    if message.content == "-권혁준바보":
        await message.channel.send("님이 바보 인걸로^^")

    if message.content == "-권혁준 바보":
        await message.channel.send("님이 바보 인걸로^^")

    if message.content == "-권한을 줘!":
        embed = discord.Embed(title="권혁준잘생겼다고하기", description="똑똑하다고도 하기", color=0x01ff00)
        embed.set_footer(text="그는 신이 되고싶습니다")
        await message.channel.send(embed=embed)

    if message.content == "-명령어":
        embed = discord.Embed(title="아직 작동되는 명령어는 없습니다", description="-명령어", color=0x01ff00)
        embed.set_footer(text="-권혁준")
        await message.channel.send(embed=embed)

    

    

client.run(token)
