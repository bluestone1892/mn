import discord
import asyncio
import os
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix="m ")

@bot.event
async def on_ready():
    print('샌즈')
    print(bot.user.id)
    await bot.change_presence(
    status=discord.Status.online,
    activity=discord.Game("접두사는 m"))

@bot.command(name="핑")
async def ping(ctx):
  embed = discord.Embed(title=':ping_pong: 퐁!', description=f'{round(round(bot.latency, 4)*1000)}ms', color=0x00aaaa)
  await ctx.send(embed=embed)
@bot.command(name= "초대링크")
async def invite(ctx):
  embed = discord.Embed(title='아쉽지만 m봇은 엠엔네이션에서만 사용할수있어요', description="( ˘︹˘ )", color=0x00aaaa)
  await ctx.send(embed=embed)
@bot.command(name= "안녕")
async def hi(ctx):
  embed = discord.Embed(title='안녕하세요!', description=" 안녕하세요!", color=0x00aaaa)
  await ctx.send(embed=embed)
@bot.command(name= "엠엔")
async def mn(ctx):
  embed = discord.Embed(title='엠엔님은 서버 주인입니다!', description="||아주 귀여브시죠!||", color=0x00aaaa)
  await ctx.send(embed=embed)


access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
