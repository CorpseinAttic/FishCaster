import discord from discord.ext import commands import json import math

Load user data from a JSON file

def get_user_data(user_id): try: with open("user_data.json", "r") as f: data = json.load(f) return data.get(str(user_id), {}) except FileNotFoundError: return {}

class Inventory(commands.Cog): def init(self, bot): self.bot = bot

@commands.command(name="inventory")
async def inventory(self, ctx, page: int = 1):
    user_id = str(ctx.author.id)
    user_data = get_user_data(user_id)
    inventory = user_data.get("fish_inventory", [])

    if not inventory:
        return await ctx.send("Your inventory is empty. Go fishing!")

    per_page = 5
    total_pages = math.ceil(len(inventory) / per_page)
    if page < 1 or page > total_pages:
        return await ctx.send(f"Invalid page. Please choose a page between 1 and {total_pages}.")

    start = (page - 1) * per_page
    end = start + per_page
    page_fish = inventory[start:end]

    embed = discord.Embed(title=f"{ctx.author.name}'s Fish Inventory — Page {page}/{total_pages}", color=discord.Color.blue())
    for idx, fish in enumerate(page_fish, start=start+1):
        name = fish.get("name", "Unknown")
        weight = fish.get("weight", 0)
        rarity = fish.get("rarity", "Unknown").capitalize()
        value = fish.get("value", 0)
        embed.add_field(name=f"{idx}. {name}", value=f"{weight}kg — *{rarity}* — ${value}", inline=False)

    await ctx.send(embed=embed)

async def setup(bot): await bot.add_cog(Inventory(bot))

