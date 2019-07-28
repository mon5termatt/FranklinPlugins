"""Package for stafftools cog."""
from .stafftools import stafftools


async def setup(bot):
    """Load stafftools cog."""
    cog = stafftools(bot)
    await cog.initialize()
    bot.add_cog(cog)
