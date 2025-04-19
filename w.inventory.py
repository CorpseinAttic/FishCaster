import discord
from discord.ext import commands
import json
import math

RARITY_EMOJIS = {
    "common": "⚪",
    "uncommon": "🟢",
    "rare": "🔵",
    "epic": "🟣",
    "legendary": "🟡",
    "mythical": "✨",
    "divine": "🌟",
    "fantasia": "🌈",
    "secrecy": "❓",
    "extinct": "☠️",
    "old_aged": "⏳",
    "question": "⁉️"
}

def get_user_inventory(user_id):
    try:
        with open("user_data.json", "r") as f:
            data = json.load(f)
        return data.get(str(user_id), {}).get("inventory", [])
    except FileNotFoundError:
        return []

class Inventory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="inventory", aliases=["inv"])
    async def inventory(self, ctx):
        user_id = str(ctx.author.id)
        inventory = get_user_inventory(user_id)

        if not inventory:
            return await ctx.send("Your inventory is empty.")

        items_per_page = 10
        total_pages = math.ceil(len(inventory) / items_per_page)
        current_page = 1

        def get_page(page):
            start_index = (page - 1) * items_per_page
            end_index = start_index + items_per_page
            page_items = inventory[start_index:end_index]

            inventory_text = ""
            for i, fish in enumerate(page_items, start=start_index + 1):
                rarity = fish.get("rarity", "common").lower()
                emoji = RARITY_EMOJIS.get(rarity, "")
                lock_status = "🔒" if fish.get("locked") else ""
                inventory_text += (
                    f"**{i}.** {emoji} `{fish['name']}` | {fish['weight']}kg | "
                    f"${fish['value']:,} {lock_status}\n"
                )

            embed = discord.Embed(
                title=f"{ctx.author.name}'s Inventory",
                description=inventory_text,
                color=discord.Color.blurple()
            )
            embed.set_footer(text=f"Page {page}/{total_pages}")
            return embed

        message = await ctx.send(embed=get_page(current_page))

        if total_pages <= 1:
            return

        await message.add_reaction("◀️")
        await message.add_reaction("▶️")

        def check(reaction, user):
            return (
                user == ctx.author
                and str(reaction.emoji) in ["◀️", "▶️"]
                and reaction.message.id == message.id
            )

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60.0, check=check)
                if str(reaction.emoji) == "▶️" and current_page < total_pages:
                    current_page += 1
                    await message.edit(embed=get_page(current_page))
                    await message.remove_reaction(reaction, user)
                elif str(reaction.emoji) == "◀️" and current_page > 1:
                    current_page -= 1
                    await message.edit(embed=get_page(current_page))
                    await message.remove_reaction(reaction, user)
                else:
                    await message.remove_reaction(reaction, user)
            except:
                break

async def setup(bot):
    await bot.add_cog(Inventory(bot))
