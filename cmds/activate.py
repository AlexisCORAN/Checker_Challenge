#!/usr/bin/python3
import storage
from cmds import bot
from messages.formats import embeded_project_fmt

@bot.command()
async def start(ctx):
    if storage.bot_active is True:
        msg = "**The BOT has already been started!!**"
        info = embeded_project_fmt(desc=msg)
        await ctx.send(embed=info)
        return

    storage.bot_active = True
    storage.projects = None
    storage.project = None
    storage.task = None
    
    msg = "**BOT started!!**"
    info = embeded_project_fmt(desc=msg, error=False)
    emj = await ctx.send(embed=info)
    await emj.add_reaction("👋")

@bot.command()
async def stop(ctx):
    if storage.bot_active is False:
        return

    storage.bot_active = False
    storage.projects = None
    storage.project = None
    storage.task = None

    msg="**BOT terminated!!**"
    info = embeded_project_fmt(desc=msg)
    emj = await ctx.send(embed=info)
    await emj.add_reaction("🛑")
