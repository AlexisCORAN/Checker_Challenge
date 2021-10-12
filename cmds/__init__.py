#!/usr/bin/python3
from discord.ext import commands

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

bot = commands.Bot(
    command_prefix='$',
    help_command = help_command
)

bot.remove_command("help")

from cmds.help import *
from cmds.activate import *
from cmds.profile import *
from cmds.project import *
from cmds.correction import *
from cmds.tasks import *
from cmds.auth_tkn import *


