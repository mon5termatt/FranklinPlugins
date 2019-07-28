from redbot.core import commands

class Mycog(commands.Cog):
    @commands.command(no_pm=True, pass_context=True)
    @checks.admin_or_permissions(manage_roles=True)
      async def snap(self, ctx):

        await ctx.send("https://tenor.com/view/thanos-infinity-gauntlet-snap-finger-snap-gif-12502580")
        snapped_users = 0
        server=ctx.message.server
        for member in tuple(server.members):
            if len(member.roles) == 1:
                await self.bot.kick(member)
                snapped_users = snapped_users + 1

        await ctx.send("It has been done, {} members parished in the mighty snap from your gauntlet.".format(snapped_users))