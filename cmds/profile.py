#!/usr/bin/python3
import storage
import discord
from cmds import bot
from hbtn_api.profile import profile_info
from hbtn_api.profile import profile_picture
from hbtn_api.profile import profile_name
from hbtn_api.profile import profile_github
from hbtn_api.profile import profile_email
from messages.formats import embeded_project_fmt


@bot.command()
async def profile(ctx):
    if storage.bot_active is False:
        return

    gh = profile_github()
    email = profile_email()
    url = 'https://github.com/{}'.format(gh)
    msg = '**E-mail:** ' + str(email) + '\n**Gihub:** ' + str(gh) 
    info = embeded_project_fmt(title=profile_name(), desc=msg, error=False, url=url)
    await ctx.send(profile_picture())
    emj = await ctx.send(embed=info)
    await emj.add_reaction("👥")