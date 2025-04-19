import discord
from discord.ext import commands
import json

def load_user_data():
    try:
        with open("user_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_user_data(data):
    with open("user_data.json", "w") as f:
        json.dump(data, f, indent=4)

class Lock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="lock")
    async def lock(self, ctx, index: int):
        user_id = str(ctx.author.id)
        data = load_user_data()
        user_data = data.get(user_id, {})
        inventory = user_data.get("inventory", [])

        if not inventory:
            return await ctx.send("Your inventory is empty.")

        if index < 1 or index > len(inventory):
            return await ctx.send(f"Invalid fish index. Use `w.inventory` to see valid numbers.")

        fish = inventory[index - 1]

        # Toggle lock
        if fish.get("locked"):
            fish["locked"] = False
            response = f"Unlocked **{fish['name']}**."
        else:
            fish["locked"] = True
            response = f"Locked **{fish['name']}**."

        # Save changes
        user_data["inventory"] = inventory
        data[user_id] = user_data
        save_user_data(data)

        await ctx.send(response)

async def setup(bot):
    await bot.add_cog(Lock(bot))
