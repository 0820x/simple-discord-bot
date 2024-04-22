import discord
from discord.ext import commands
intents = discord.Intents.all()
x7v1 = commands.Bot(command_prefix="!", intents=intents)
x7v1.remove_command("help")
@x7v1.event
async def on_ready():
    print("connected")
    await x7v1.change_presence(activity=discord.Streaming(name="@skid.fed", url="https://twitch.tv/"))
@x7v1.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="`!kick <@>`\n`!ban <@>`\n`!unban <id>`")
    await ctx.send(embed=embed)
MOD_MEMBER_IDS = [1215631473810345995]
@x7v1.command()
async def kick(ctx, member: discord.Member, *, reason="No reason"):
  if ctx.author.id in MOD_MEMBER_IDS:
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member.mention} for {reason}")
  else:
    ctx.send("you're not a mod")
@x7v1.command()
async def ban(ctx, member: discord.Member, *, reason="No reason"):
  if ctx.author.id in MOD_MEMBER_IDS:
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention} for {reason}")
  else:
    ctx.send("you're not a mod")
@x7v1.command()
async def unban(ctx, *, member):
  if ctx.author.id in MOD_MEMBER_IDS:
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return
  else:
    ctx.send("you're not a mod")
x7v1.run("MTIzMTk3MDk1NTM2Mjk1OTM3MQ.GbM17M.z2owKH5Zs0cOen_HJfhgGIf9tsU82GdJicC0WQ")
