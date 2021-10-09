import discord
from cmds import bot
from messages.formats import embeded_project_fmt


async def error_msg(ctx):
    msg = '**Just put the command name.**'
    info = embeded_project_fmt(desc=msg)
    emj = await ctx.send(embed=info)
    await emj.add_reaction("í¹„")


@bot.group(invoke_without_command=True)
async def help(ctx):
    msg = "Use $help <command> for extended information on a command."
    em = discord.Embed(title="Help", color=16312092, description=msg)
    em.add_field(name="Start", value="$start")
    em.add_field(name="Stop", value="$stop")
    em.add_field(name="Project", value="$project")
    em.add_field(name="Profile", value="$profile")
    em.add_field(name="Tasks", value="$tasks")
    em.add_field(name="Correction", value="$correction")
    em.add_field(name="Results", value="$results")

    emj = await ctx.send(embed=em)
    await emj.add_reaction("í¶˜")


@help.command()
async def start(ctx, *, args=None):
    if args is None:
        msg = "This command initializes the bot."
        em = discord.Embed(title="Start", color=16312092, description=msg)
        em.add_field(name="Syntax:", value="$start")
        emj = await ctx.send(embed=em)
        await emj.add_reaction("í¶˜")
    else:
        await error_msg(ctx)


@help.command()
async def stop(ctx, *, args=None):
    if args is None:
        msg = "This command stops the bot."
        em = discord.Embed(title="Stop", color=16312092, description=msg)
        em.add_field(name="Syntax:", value="$stop")
        emj = await ctx.send(embed=em)
        await emj.add_reaction("í¶˜")
    else:
        await error_msg(ctx)


@help.command()
async def project(ctx, *, args=None):
    if args is None:
        msg = "This command without ID returns the name of project and
        with ID returns project with the tasks."
        em = discord.Embed(title="Project", color=16312092, description=msg)
        em.add_field(name="Syntax:", value="$project")
        emj = await ctx.send(embed=em)
        await emj.add_reaction("í¶˜")
    else:
        await error_msg(ctx)


@help.command()
async def tasks(ctx, *, args=None):
    if args is None:
        msg = "This command lists the tasks of a project."
        em = discord.Embed(title="Tasks", color=16312092, description=msg)
        em.add_field(name="Syntax:", value="$tasks")
        emj = await ctx.send(embed=em)
        await emj.add_reaction("í¶˜")
    else:
        await error_msg(ctx)


@help.command()
async def correction(ctx, *, args=None):
    if args is None:
        msg = "This command makes a correction to a task with its ID."
        em = discord.Embed(title="Correction", color=16312092, description=msg)
        em.add_field(name="Syntax:", value="$correction")
        emj = await ctx.send(embed=em)
        await emj.add_reaction("í¶˜")
    else:
        await error_msg(ctx)


@help.command()
async def results(ctx, *, args=None):
    if args is None:
        msg = "This command returns the result of a correction."
        em = discord.Embed(title="Results", color=16312092, description=msg)
        em.add_field(name="Syntax:", value="$results")
        emj = await ctx.send(embed=em)
        await emj.add_reaction("í¶˜")
    else:
        await error_msg(ctx)


@help.command()
async def profile(ctx, *, args=None):
    if args is None:
        msg = "This command returns email, user, link to your account github
        and your profile photo."
        em = discord.Embed(title="Profile", color=16312092, description=msg)
        em.add_field(name="Syntax:", value="$profile")
        emj = await ctx.send(embed=em)
        await emj.add_reaction("í¶˜")
    else:
        await error_msg(ctx)
