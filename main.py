import discord from discord.ext import commands import os from fish import catch_fish from upgrades import check_rod_bonus from best_hatch import update_best_hatch

intents = discord.Intents.default() intents.message_content = True

bot = commands.Bot(command_prefix="w.", intents=intents)

user_data = {}  # This will hold temporary user data like best hatch and inventory

@bot.event async def on_ready(): print(f"Logged in as {bot.user}")

@bot.command() async def fish(ctx): user_id = str(ctx.author.id) if user_id not in user_data: user_data[user_id] = { "has_location": False, "best_hatch": None, "rod_level": 1 }

if not user_data[user_id]["has_location"]:
    await ctx.send("Aye! You must be new, go to the shop to buy your first area for free before fishing!")
    return

rod_bonus = check_rod_bonus(user_data[user_id]["rod_level"])
fish_data = catch_fish(rod_bonus)

if fish_data:
    update_best_hatch(user_data[user_id], fish_data)
    await ctx.send(f"Fishing...\nYou caught a **{fish_data['name']}**!\n"
                   f"Rarity: *{fish_data['rarity']}* | Size: `{fish_data['weight']}kg` | Value: `${fish_data['value']}`")
else:
    await ctx.send("Fishing...\nYou caught nothing this time!")

bot.run(os.getenv("DISCORD_TOKEN"))

