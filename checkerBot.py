#!/usr/bin/python3
import discord
import json
import requests as rq
from cmds import bot
from discord.ext import commands

disc_tkn=''

@bot.event
async def on_ready():
    print('Bot loaded as {0.user}'.format(bot))


#@bot.Cog.listener()
#async def on_command_error(self, ctx, error):
#    if hasattr(ctx.command, 'on_error'):
#        return
@commands.Cog.listener()
async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
    """A global error handler cog."""

    if isinstance(error, commands.CommandNotFound):
        return  # Return because we don't want to show an error for every command not found
    elif isinstance(error, commands.CommandOnCooldown):
        message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
    elif isinstance(error, commands.MissingPermissions):
        message = "You are missing the required permissions to run this command!"
    elif isinstance(error, commands.UserInputError):
        message = "Something about your input was wrong, please check your input and try again!"
    else:
        message = "Oh no! Something went wrong while running the command!"

    await ctx.send(message, delete_after=5)
    await ctx.message.delete(delay=5)

bot.run(disc_tkn)
