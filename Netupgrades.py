# netupgrade.py

import discord
from discord.ext import commands
from NetData import net_data
import json

def get_user_data(user_id):
    try:
        with open("user_data.json", "r") as f:
            data = json.load(f)
        return data.get(str(user_id), {})
    except FileNotFoundError:
        return {}

def save_user_data(user_id, user_data):
    try:
        with open("user_data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    data[str(user_id)] = user_data
    with open("user_data.json", "w") as f:
        json.dump(data, f, indent=4)

class NetUpgrade(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="netupgrade")
    async def netupgrade(self, ctx):
        user_id = ctx.author.id
        user = get_user_data(user_id)
        net_level = user.get("net_level", 0)
        net_type = user.get("net_type", "basic_nets")  # "basic_nets" or "large_nets"
        balance = user.get("balance", 0)

        net_levels = net_data[net_type]

        if net_level >= len(net_levels):
            return await ctx.send("Your net is already at the maximum level!")

        next_level = net_level + 1
        upgrade_info = net_levels[next_level]
        cost = upgrade_info["cost"]

        if balance < cost:
            return await ctx.send(f"You need ${cost:,} to upgrade to **{upgrade_info['name']}**.")

        # Deduct cost and upgrade net
        user["balance"] -= cost
        user["net_level"] = next_level
        user["net_type"] = net_type
        save_user_data(user_id, user)

        embed = discord.Embed(
            title="Net Upgraded!",
            description=f"You've upgraded to **{upgrade_info['name']}**!\n"
                        f"**New Capacity:** {upgrade_info['capacity']} fish\n"
                        f"**Cost:** ${cost:,}",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(NetUpgrade(bot))
