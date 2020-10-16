from discord.ext import commands
from discord.ext.commands import Context

import logging

queues = {'dummy': []}

prevMessages = {'dummy': None}


def setup(bot):
    """
    Setup the cogs in this extension
    """
    bot.add_cog(Anyone(bot))


def getQueue(serverName: str):
    """
    Get the relevant queue for the server
    """
    if serverName in queues.keys():
        return queues.get(serverName)
    else:
        queues[serverName] = []
        return queues.get(serverName)


class Anyone(commands.Cog):
    """
    Commands for kitchen
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def use(self, ctx: Context):
        """
        Adds the person to the kitchen queue
        """
        k = ctx.guild.name + ctx.channel.name

        s = ctx.message.author
        q = getQueue(ctx.guild)
        if s not in q:
            if len(q) < 1:
                q.append(s)
                logging.info('{0} add {1}'.format(ctx.guild, s))
                prevMessages[k] = await ctx.send(
                    s.mention + ' is now in the kitchen')
        else:
            prevMessages[k] = await ctx.send(
            'someone is already in the kitchen')

    @commands.command()
    async def done(self, ctx: Context):
        """
        Removes people from the kitchen queue
        """
        k = ctx.guild.name + ctx.channel.name

        s = ctx.message.author
        q = getQueue(ctx.guild)
        if s in q:
            q.remove(s)
            logging.info('{0} remove {1}'.format(ctx.guild, s))
            prevMessages[k] = await ctx.send(s.mention + ' is no longer in the kitchen.')
        else:
            prevMessages[k] = await ctx.send(s.mention + ' is not in the kitchen.')
