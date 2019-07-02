import discord
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import dataIO
from copy import deepcopy
import asyncio
import logging
import os

log = logging.getLogger("red.admin")
class StaffTools:
    """Various tools for Wardens staff, enjoy or don't, I don't care."""

    def __init__(self, bot):
        self.bot = bot
        self._settings = dataIO.load_json('data/stafftools/settings.json')

    def _save_settings(self):
        dataIO.save_json('data/admin/settings.json', self._settings)

    @commands.command(no_pm=True, pass_context=True)
    @checks.admin_or_permissions(manage_roles=True)
    async def exile(self, ctx, user: discord.Member = none):
        """Exile someone from the community"""

        if user is None:
            await self.bot.say("You need to specify a member to exile.")
            return

        prem_role = self._role_from_string(ctx.message.server, "Premium")
        plat_role = self._role_from_string(ctx.message.server, "Platinum")
        exile_role = self._role_from_string(ctx.message.server, "Exiled")
        try:
            if prem_role in user.roles:
                await self.bot.remove_roles(user, prem_role)
            if plat_role in user.roles:
                await self.bot.remove_roles(user, plat_role)

            await self.bot.add_roles(user, exile_role)
            await self.bot.say("{} has been sent to exiled! https://tenor.com/view/supernatural-spn-sam-sammy-jared-padalecki-gif-5417529".format(user.name))
        except discord.Forbidden:
            await self.bot.say("I don't have permissions to do this.")
