import asyncio
import discord
import pathlib
from redbot.core import Config, checks, commands
from redbot.core.bot import Red

class Stafftools(commands.Cog):
    "Staff tools."

    def __init__(self, bot: Red):
        self.bot = bot

    @commands.command()
    @checks.admin_or_permissions(manage_roles=True)
    async def snap(self, ctx):
        """Thanos snaps all non role users"""

        await ctx.send("https://tenor.com/view/thanos-infinity-gauntlet-snap-finger-snap-gif-12502580")

        snapped_users = 0
        server = ctx.guild
        for member in tuple(server.members):
            if len(member.roles) == 1:
                await server.kick(member)
                snapped_users = snapped_users + 1

        await ctx.send("It has been done, {} members parished in the mighty snap from your gauntlet.".format(snapped_users))
    