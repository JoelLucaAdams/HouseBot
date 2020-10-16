from discord.ext import commands
from discord.ext.commands import Context


class General(commands.Cog):
    """
    General commands for everyone.
    """

    @commands.command()
    async def source(self, ctx: Context):
        """
        Print a link to the source code
        """
        await ctx.send(content='Created by `Joel Adams`\n'
                               'ungaBunga link')

    @commands.command()
    async def info(self, ctx: Context):
        """
        Display some info about how the bot works
        """
        await ctx.send('Just creates a queue system for the kitchen. There\'s nothing more to it')

    @commands.command()
    async def feedback(self, ctx: Context):
        """
        Report feedback or issues with the bot
        """
        await ctx.send('If the bot is broken or you have any feedback you\'d like to submit please create a issue on '
                       'GitHub: ''')
