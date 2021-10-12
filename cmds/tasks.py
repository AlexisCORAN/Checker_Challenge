#!/usr/bin/python3
import storage
from cmds import bot
from hbtn_api.task import task_info
from messages import CURR_PROJECT_TITLE
from messages.formats import tasks_fmt
from messages.formats import embeded_project_fmt

@bot.command()
async def tasks(ctx):
    """
    This command lists the tasks of a project
    """
    if storage.bot_active is False:
        return
    
    if storage.project is None:
        msg = '**You must select a project first**'
        info = embeded_project_fmt(desc=msg)
        await ctx.send(embed=info)
        return

    title = CURR_PROJECT_TITLE.format(storage.project.get('name'))
    _id = storage.project.get('id')
    desc = tasks_fmt(storage.project.get('tasks'))
    info = embeded_project_fmt(title, _id=_id, desc=desc, error=False)
    await ctx.send(embed=info)
