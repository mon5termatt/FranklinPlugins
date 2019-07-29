from redbot.core.bot import Red
from .stafftools import Stafftools


def setup(bot: Red):
    tools = Stafftools(bot)
    bot.add_cog(tools)