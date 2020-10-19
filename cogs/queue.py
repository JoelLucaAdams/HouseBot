from discord.ext import commands
from discord.ext.commands import Context

import logging

kitchenQueue = {'nothing': []}
bathroomQueue = {'nothing': []}


def setup(bot):
    """
    Setup the cogs in this extension
    """
    bot.add_cog(Queue(bot))


def getQueue(serverName: str, queueType: str):
    """
    Gets the queue type and returns a queue
    """
    if queueType is "k":
        queue = kitchenQueue
    elif queueType is "b":
        queue = bathroomQueue
    else:
        raise Exception("Incorrect parameters")

    if serverName in queue.keys():
        return queue.get(serverName)
    else:
        queue[serverName] = []
        return queue.get(serverName)


class Queue(commands.Cog):
    """
    Commands for house
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def use(self, ctx: Context, arg):
        """
        Adds the person to the kitchen(k) or bathroom(b) queue
        """
        s = ctx.message.author

        q = getQueue(ctx.guild, arg)
        if arg is "k":
            name = "kitchen"
        elif arg is "b":
            name = "bathroom"
        else:
            raise Exception("Incorrect parameters")

        if len(q) < 1:
            q.append(s)
            logging.info('{0} add {1}'.format(ctx.guild, s))
            await ctx.send(s.mention + ' is now in the ' + name)
        else:
            await ctx.send(q[0].mention + ' is already in the ' + name)

    @commands.command()
    async def done(self, ctx: Context, arg):
        """
        Removes people from the kitchen(k) or bathroom(b) queue
        """
        s = ctx.message.author

        q = getQueue(ctx.guild, arg)
        if arg is "k":
            name = "kitchen"
        elif arg is "b":
            name = "bathroom"
        else:
            raise Exception("Incorrect parameters")

        if s in q:
            q.remove(s)
            logging.info('{0} remove {1}'.format(ctx.guild, s))
            await ctx.send(s.mention + ' is no longer in the ' + name)
        else:
            await ctx.send(s.mention + ' is not in the ' + name)

    @commands.command()
    async def resetQueue(self, ctx: Context, arg):
        """
        resets queues using: (a)-all, (k)-kitchen, (b)-bathroom
        """
        if arg is 'a':
            getQueue(ctx.guild, 'k').clear()
            getQueue(ctx.guild, 'b').clear()
            await ctx.send('cleared bathroom and kitchen queues')
        elif arg is 'k':
            getQueue(ctx.guild, 'k').clear()
            await ctx.send('cleared kitchen queue')
        elif arg is 'b':
            getQueue(ctx.guild, 'b').clear()
            await ctx.send('cleared bathroom queue')
        else:
            raise Exception("Incorrect parameters")
