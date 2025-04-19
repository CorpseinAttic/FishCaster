# w.location

import discord
from discord.ext import commands
from LocationData import locations

class Location(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="location")
    async def location_shop(self, ctx):
        embed = discord.Embed(
            title="Fishing Locations",
            description="Unlock new fishing spots with levels and coins!",
            color=discord.Color.blue()
        )

        for loc in locations:
            boosts = ", ".join([f"**{r.title()}**: {int(p * 100)}%" for r, p in loc['rarity_boosts'].items()])
            embed.add_field(
                name=f"{loc['name']}",
                value=(
                    f"**Level Required**: {loc['level_required']}\n"
                    f"**Cost**: ${loc['cost']:,}\n"
                    f"**Boosts**: {boosts}"
                ),
                inline=False
            )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Location(bot))
