import discord from discord.ext import commands import json

Load user data from JSON

def load_user_data(): try: with open("user_data.json", "r") as f: return json.load(f) except FileNotFoundError: return {}

class Leaderboard(commands.Cog): def init(self, bot): self.bot = bot

@commands.command(name="top")
async def global_leaderboard(self, ctx):
    data = load_user_data()
    sorted_users = sorted(data.items(), key=lambda x: x[1].get("total_value", 0), reverse=True)

    embed = discord.Embed(title="Global Leaderboard", color=discord.Color.gold())

    for i, (user_id, info) in enumerate(sorted_users[:10], start=1):
        user = self.bot.get_user(int(user_id))
        username = user.name if user else f"User ID {user_id}"
        value = info.get("total_value", 0)
        best = info.get("best_catch", "None")
        embed.add_field(name=f"#{i} - {username}", value=f"Total Value: ${value:,}\nBest Catch: {best}", inline=False)

    await ctx.send(embed=embed)

@commands.command(name="servertop")
async def server_leaderboard(self, ctx):
    data = load_user_data()
    server_users = [(uid, info) for uid, info in data.items() if str(ctx.guild.id) in info.get("servers", [])]
    sorted_users = sorted(server_users, key=lambda x: x[1].get("total_value", 0), reverse=True)

    embed = discord.Embed(title=f"{ctx.guild.name} Leaderboard", color=discord.Color.blurple())

    for i, (user_id, info) in enumerate(sorted_users[:10], start=1):
        user = self.bot.get_user(int(user_id))
        username = user.name if user else f"User ID {user_id}"
        value = info.get("total_value", 0)
        best = info.get("best_catch", "None")
        embed.add_field(name=f"#{i} - {username}", value=f"Total Value: ${value:,}\nBest Catch: {best}", inline=False)

    await ctx.send(embed=embed)

async def setup(bot): await bot.add_cog(Leaderboard(bot))

