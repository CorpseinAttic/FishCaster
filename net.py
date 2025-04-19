# w.net.py
import discord
from discord.ext import commands
import random
from NetData import net_levels
from fish_data import get_random_fish
from utils import get_user_data, save_user_data

class NetFishing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="net")
    async def net(self, ctx):
        user_id = str(ctx.author.id)
        user = get_user_data(user_id)

        net_level = user.get("net_level", 0)
        if net_level == 0:
            return await ctx.send("You don't have a net! Buy one from the shop first.")

        max_capacity = net_levels[net_level]["capacity"]
        fish_caught = []

        for _ in range(max_capacity):
            fish = get_random_fish()  # This should return a fish dict with name, rarity, value, weight
            fish_caught.append(fish)

        user.setdefault("fish_inventory", []).extend(fish_caught)
        save_user_data(user_id, user)

        embed = discord.Embed(
            title=f"You cast your net and caught {len(fish_caught)} fish!",
            color=discord.Color.blue()
        )

        for fish in fish_caught[:10]:  # Show only first 10 fish in message
            embed.add_field(
                name=f"{fish['name']} ({fish['rarity']})",
                value=f"Weight: {fish['weight']}kg | Value: ${fish['value']:,}",
                inline=False
            )

        if len(fish_caught) > 10:
            embed.set_footer(text="Only showing first 10 fish...")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(NetFishing(bot))
