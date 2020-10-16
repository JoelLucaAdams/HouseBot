from discord.ext import commands
from discord.ext.commands import Context


def setup(bot):
    """
    Setup the cogs in this extension
    """
    bot.add_cog(Utilities(bot))


class Utilities(commands.Cog):
    """
    General Utilities
    """
    @commands.command()
    async def ping(self, ctx: Context):
        """
        Status check
        """
        import time
        start_time = time.time()
        message = await ctx.send('pong. `DWSP latency: ' + str(round(ctx.bot.latency * 1000)) + 'ms`')
        end_time = time.time()
        await message.edit(content='pong. `DWSP latency: ' + str(round(ctx.bot.latency * 1000)) + 'ms` '
                                                                                                  '`Response time: ' + str(
            round(end_time - start_time, 3)) + 'ms`')
