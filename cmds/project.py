#!/usr/bin/python3
import storage
from cmds import commands
from cmds import bot
from hbtn_api.project import project_info
from messages import CURR_PROJECT_TITLE
from messages.formats import embeded_project_fmt

@bot.command()
async def project(ctx, *, arg=None):
    if storage.bot_active is False:
        return
    
    if arg is None:
        if storage.project is None:
            msg = '**You must select a project using:** `$project <project_id>`'
            info = embeded_project_fmt(desc=msg)
            await ctx.send(embed=info)
            return

        title = CURR_PROJECT_TITLE.format(storage.project.get('name'))
        _id = storage.project.get('id')
        info = embeded_project_fmt(title, _id=_id, error=False)
        await ctx.send(embed=info)
        return

    args = arg.split()
    if len(args) > 1:
        msg = '**Usage:** `$project <project_id>`'
        info = embeded_project_fmt(desc=msg)
        await ctx.send(embed=info)
        return

    proj_id = args[0]
    res = project_info(proj_id)

    if res.get('success') is False:
        msg = res.get('msg')
        info = embeded_project_fmt(desc=msg)
        await ctx.send(embed=info)
        return

    error = not res.get('success', True)
    msg = res.get('msg')
    info = embeded_project_fmt(storage.project.get('name'), storage.project.get('id'), desc=msg, error=False)
    await ctx.send(embed=info)
