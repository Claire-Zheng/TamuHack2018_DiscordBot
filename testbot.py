import discord
from discord.ext import commands

bot = commands.Bot(description="Short desc of your bot", command_prefix="!")


@bot.command()
async def ping():
    await bot.say("Pong!")

@bot.command(pass_context=True)
async def say(ctx, *, something):
	await bot.say(something)
	await bot.delete_message(ctx.message)

@bot.command()
async def kms():
    await bot.add_reaction("Should I kill myself? One react and I'll do it.", :weary:)
    
bot.run('NDA2OTAzMTEzMzYzMDk1NTUy.DU54Yw.KV6VHd46qBTlIIgKMEmvvRQbfcw')
