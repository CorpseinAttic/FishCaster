import discord
from discord.ext import commands
import json

from RodData import get_rod_info
from NetData import get_net_info

def get_user_data(user_id):
    try:
        with open("user_data.json", "r") as f:
            data = json.load(f)
        return data.get(str(user_id), {})
    except FileNotFoundError:
        return {}

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="stats")
    async def stats(self, ctx):
        user_id = str(ctx.author.id)
        user = get_user_data(user_id)

        level = user.get("level", 1)
        balance = user.get("balance", 0)
        total_value = user.get("total_value", 0)
        rod_level = user.get("rod_level", 1)
        net_level = user.get("net_level", 1)
        best_fish = user.get("best_fish", {})

        rod = get_rod_info(rod_level)
        net = get_net_info(net_level)

        embed = discord.Embed(
            title=f"{ctx.author.name}'s Stats",
            color=discord.Color.green()
        )
        embed.add_field(name="Level", value=f"**{level}**", inline=True)
        embed.add_field(name="Balance", value=f"${balance:,}", inline=True)
        embed.add_field(name="Total Value", value=f"${total_value:,}", inline=True)

        if best_fish:
            embed.add_field(
                name="Best Catch",
                value=f"{best_fish['name']} | {best_fish['weight']}kg | ${best_fish['value']:,}",
                inline=False
            )
        else:
            embed.add_field(name="Best Catch", value="None yet!", inline=False)

        embed.add_field(
            name="Rod",
            value=f"Level {rod_level} | {rod['luck_multiplier']}% More Luck",
            inline=True
        )
        embed.add_field(
            name="Net",
            value=f"Level {net_level} | {net['capacity']} Capacity",
            inline=True
        )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Stats(bot))
