#!/usr/bin/python3
import storage
from cmds import bot
from hbtn_api.correction import ask_correction
from hbtn_api.correction import get_results
from messages.formats import embeded_project_fmt

@bot.command()
async def correction(ctx, task_id):
    if storage.bot_active is False:
        return
    res = ask_correction(task_id)
    error = not res.get('success', True)
    msg = res.get('msg')
    info = embeded_project_fmt(desc=msg, error=error)
    emj = await ctx.send(embed=info)
    await emj.add_reaction("😯")

@bot.command()
async def results(ctx):
    if storage.bot_active is False:
        return
    res = get_results(storage.result_id)
    error = not res.get('success', True)
    msg = res.get('msg')
    info = embeded_project_fmt(desc=msg, error=error)
    emj = await ctx.send(embed=info)
    await emj.add_reaction("🙄")