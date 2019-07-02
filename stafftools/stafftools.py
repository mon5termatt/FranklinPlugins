import discord
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import dataIO
import asyncio
import logging
import os

class StaffTools:
    """Various tools for Wardens staff, enjoy or don't, I don't care."""

    def __init__(self, bot):
        self.bot = bot
        self._settings = dataIO.load_json('data/stafftools/settings.json')

    def _save_settings(self):
        dataIO.save_json('data/admin/settings.json', self._settings)

    def _role_from_string(self, server, rolename, roles=None):
        if roles is None:
            roles = server.roles

        roles = [r for r in roles if r is not None]
        role = discord.utils.find(lambda r: r.name.lower() == rolename.lower(),
                                  roles)
        return role

    @commands.command(no_pm=True, pass_context=True)
    @checks.admin_or_permissions(manage_roles=True)
    async def exile(self, ctx, user: discord.Member=None):
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

    @commands.command(no_pm=True, pass_context=True)
    @checks.admin_or_permissions(manage_roles=True)
    async def snap(self, ctx, user: discord.Member=None):
        """Thanos snaps all non paid users"""

        await self.bot.say("https://tenor.com/view/thanos-infinity-gauntlet-snap-finger-snap-gif-12502580")

        snapped_users = 0
        server=ctx.message.server
        for member in tuple(server.members):
            if len(member.roles) == 1:
                await self.bot.kick(member)
                snapped_users = snapped_users + 1

        await self.bot.say("It has been done, {} members parished in the mighty snap from your gauntlet.".format(snapped_users))

    @commands.command(no_pm=True, pass_context=True)
    @checks.admin_or_permissions(manage_roles=True)
    async def fmute(self, ctx):
        """Gives a user the muted role"""

        if user is None:
            await self.bot.say("You need to specify a member to mute.")
            return

        muted_role = self._role_from_string(ctx.message.server, "Muted")
        try:
            if muted_role in user.roles:
                await self.bot.remove_roles(user, muted_role)
                await self.bot.say("{} has been muted.".format(user.name))
        except discord.Forbidden:
            await self.bot.say("I don't have permissions to mute this person")
        

def setup_file():
    if not os.path.exists('data/stafftools/settings.json'):
        try:
            os.mkdir('data/stafftools')
        except FileExistsError:
            pass
        else:
            dataIO.save_json('data/stafftools/settings.json', {})

def setup(bot):
    setup_file()
    n = StaffTools(bot)
    bot.add_cog(n)