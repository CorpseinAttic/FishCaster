# shop.py

import discord
from discord.ext import commands

booster_items = [
    {"name": "Chum Bucket", "price": 2000, "effect": "x1.2", "emoji": "🪣"},
    {"name": "Chunk of Fish Meat", "price": 5000, "effect": "x1.5", "emoji": "🍖"},
    {"name": "Whole Shark", "price": 10000, "effect": "x2.0", "emoji": "🦈"},
    {"name": "Luck Potion 1", "price": 3000, "effect": "+50% Luck", "emoji": "🧪"},
    {"name": "Luck Potion 2", "price": 8000, "effect": "+75% Luck", "emoji": "🧪"},
    {"name": "Luck Potion 3", "price": 12000, "effect": "+120% Luck", "emoji": "🧪"},
    {"name": "Luck Potion 4", "price": 17000, "effect": "+160% Luck", "emoji": "🧪"},
    {"name": "Lucky Bait 1", "price": 15000, "effect": "+400% Luck (One-time)", "emoji": "🎣"},
    {"name": "Lucky Bait 2", "price": 32000, "effect": "+750% Luck (One-time)", "emoji": "🎣"},
    {"name": "Lucky Bait 3", "price": 45000, "effect": "+1000% Luck (One-time)", "emoji": "🎣"},
    {"name": "Lucky Bait 4", "price": 150000, "effect": "+10,000% Luck (One-time)", "emoji": "🎣"},
    {"name": "Lucky Bait 5", "price": 350000, "effect": "+100,000% Luck (One-time)", "emoji": "🎣"},
    {"name": "Lucky Bait 6", "price": 600000, "effect": "+1,000,000% Luck (One-time)", "emoji": "🎣"},
]

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="shop")
    async def shop(self, ctx):
        embed = discord.Embed(title="Fishing Shop", color=discord.Color.gold())
        for item in booster_items:
            embed.add_field(
                name=f"{item['emoji']} {item['name']} - ${item['price']:,}",
                value=f"**Effect:** {item['effect']}",
                inline=False
            )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Shop(bot))
