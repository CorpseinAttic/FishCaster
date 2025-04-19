import discord
from discord.ext import commands
from location_data import locations  # make sure you named your location file right

@commands.command(name="travelaccess")
async def travel_access(ctx):
    user_id = str(ctx.author.id)
    user_data = get_user_data(user_id)  # replace with your method of loading user data
    unlocked_locations = user_data.get("unlocked_locations", [])
    user_level = user_data.get("level", 0)

    embed = discord.Embed(title="Fishing Locations", color=discord.Color.blue())

    for loc in locations:
        name = loc["name"]
        level_required = loc["level_required"]
        cost = loc["cost"]

        is_unlocked = name in unlocked_locations
        status = "✅ Unlocked" if is_unlocked else "❌ Locked"
        level_ok = user_level >= level_required

        line = f"Level {level_required} | Cost: ${cost:,} | {status}"
        if not level_ok and not is_unlocked:
            line += " (Too low level)"

        embed.add_field(name=name, value=line, inline=False)

    await ctx.send(embed=embed)
