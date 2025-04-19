import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", aliases=["commands"])
    async def help(self, ctx):
        embed = discord.Embed(
            title="**Fishing Bot Commands**",
            description="Here's a list of available commands!",
            color=discord.Color.blurple()
        )

        embed.add_field(
            name="**Fishing**",
            value=(
                "`w.fish` - Catch a fish\n"
                "`w.net` - Use your net to catch multiple fish\n"
                "`w.boost` - View active boosters"
            ),
            inline=False
        )

        embed.add_field(
            name="**Inventory**",
            value=(
                "`w.inventory` - View your fish inventory\n"
                "`w.lock [fishID]` - Lock a fish from being sold\n"
                "`w.sell` - Sell your caught fish"
            ),
            inline=False
        )

        embed.add_field(
            name="**Shop & Items**",
            value=(
                "`w.shop` - View available items and boosters\n"
                "`w.buy [item]` - Buy an item from the shop\n"
                "`w.consumable` - View your consumable inventory\n"
                "`w.use [item] [amount]` - Use a consumable item"
            ),
            inline=False
        )

        embed.add_field(
            name="**Upgrades**",
            value=(
                "`w.rodupgrade` - Upgrade your fishing rod\n"
                "`w.netupgrade` - Upgrade your net"
            ),
            inline=False
        )

        embed.add_field(
            name="**Progress**",
            value=(
                "`w.stats` - View your personal stats\n"
                "`w.leaderboard` - Global leaderboard\n"
                "`w.serverboard` - Server leaderboard"
            ),
            inline=False
        )

        embed.set_footer(text="Use the prefix 'w.' before every command!")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(HelpCommand(bot))
