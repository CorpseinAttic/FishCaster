# w.travelto

import discord
from discord.ext import commands
from LocationData import locations
import json

# Load or save user data (simplified example, you might use a database instead)
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

class Travel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="travelto")
    async def travelto(self, ctx, *, location_name: str):
        user_id = ctx.author.id
        user = get_user_data(user_id)
        level = user.get("level", 1)
        balance = user.get("balance", 0)
        unlocked = user.get("unlocked_locations", [])

        # Find location
        location = next((l for l in locations if l["name"].lower() == location_name.lower()), None)
        if not location:
            return await ctx.send("Location not found.")

        if location["name"] in unlocked:
            return await ctx.send("You've already unlocked this location!")

        if level < location["level_required"]:
            return await ctx.send(f"You need to be level {location['level_required']} to unlock this location.")

        if balance < location["cost"]:
            return await ctx.send(f"You need ${location['cost']:,} to unlock this location.")

        # Deduct cost and unlock
        user["balance"] -= location["cost"]
        unlocked.append(location["name"])
        user["unlocked_locations"] = unlocked
        save_user_data(user_id, user)

        await ctx.send(f"You've successfully unlocked **{location['name']}**!")

async def setup(bot):
    await bot.add_cog(Travel(bot))
