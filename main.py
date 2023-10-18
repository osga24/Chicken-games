import discord
import json
import random
from datetime import datetime


bot = discord.Bot(intents = discord.Intents.all())
with open("token.json","r") as file:
    token = json.load(file)

@bot.event
async def on_ready():
    print(f">>{bot.user} IS ON<<")


#猜拳

bot_play = None
player = None

class moraView(discord.ui.View):
    @discord.ui.button(label="剪刀", style=discord.ButtonStyle.secondary, emoji="✌️")
    async def button_scissors(self, button, interaction):
        global player  # 添加這行
        if player == True:
            if bot_play == 2:
                embed=discord.Embed(color=0x6b9cff)
                embed.set_thumbnail(url="https://memeprod.sgp1.digitaloceanspaces.com/user-resource-thumbnail/38a674770ff605c7d449e302d7bcbcaa.png")
                embed.add_field(name="猜拳", value="", inline=False)
                embed.add_field(name="平手", value="唉呦 厲害喔", inline=False)
                await interaction.response.send_message(embed=embed)
                player = False
            elif bot_play == 0:
                embed=discord.Embed(color=0xff0000)
                embed.set_thumbnail(url="https://static.wikia.nocookie.net/e0d584f0-ab46-4ea6-ac2c-caf14cd14c7c/scale-to-width/755")
                embed.add_field(name="猜拳", value="", inline=False)
                embed.add_field(name="你輸了!", value="哇哈哈哈哈 輕輕鬆鬆", inline=False)
                await interaction.response.send_message(embed=embed)
                player = False
            elif bot_play == 1:
                embed=discord.Embed(color=0x00ff62)
                embed.set_thumbnail(url="https://pbs.twimg.com/media/FA5s2mlWYAMn7tr.jpg")
                embed.add_field(name="猜拳", value="", inline=False)
                embed.add_field(name="你贏了!", value="social credit +15", inline=False)
                await interaction.response.send_message(embed=embed)
                player = False

    @discord.ui.button(label="石頭", style=discord.ButtonStyle.secondary, emoji="✊")
    async def button_stone(self, button, interaction):
        global player  # 添加這行
        if player == True:
            if bot_play == 0:
                embed=discord.Embed(color=0x6b9cff)
                embed.set_thumbnail(url="https://memeprod.sgp1.digitaloceanspaces.com/user-resource-thumbnail/38a674770ff605c7d449e302d7bcbcaa.png")
                embed.add_field(name="猜拳", value="", inline=False)
                embed.add_field(name="平手", value="唉呦 厲害喔", inline=False)
                await interaction.response.send_message(embed=embed)
                player = False
            elif bot_play == 1:
                embed=discord.Embed(color=0xff0000)
                embed.set_thumbnail(url="https://static.wikia.nocookie.net/e0d584f0-ab46-4ea6-ac2c-caf14cd14c7c/scale-to-width/755")
                embed.add_field(name="猜拳", value="", inline=False)
                embed.add_field(name="你輸了!", value="哇哈哈哈哈 輕輕鬆鬆", inline=False)
                await interaction.response.send_message(embed=embed)
                player = False
            elif bot_play == 2:
                embed=discord.Embed(color=0x00ff62)
                embed.set_thumbnail(url="https://pbs.twimg.com/media/FA5s2mlWYAMn7tr.jpg")
                embed.add_field(name="猜拳", value="", inline=False)
                embed.add_field(name="你贏了!", value="social credit +15", inline=False)
                await interaction.response.send_message(embed=embed)
                player = False

    @discord.ui.button(label="布", style=discord.ButtonStyle.secondary, emoji="🤚")
    async def button_paper(self, button, interaction):
        global player  # 添加這行
        if player == True:
            if bot_play == 1:
                embed=discord.Embed(color=0x6b9cff)
                embed.set_thumbnail(url="https://memeprod.sgp1.digitaloceanspaces.com/user-resource-thumbnail/38a674770ff605c7d449e302d7bcbcaa.png")
                embed.add_field(name="猜拳", value="", inline=False)
                embed.add_field(name="平手", value="唉呦 厲害喔", inline=False)
                await interaction.response.send_message(embed=embed)
                player = False
            elif bot_play == 2:
                embed=discord.Embed(color=0xff0000)
                embed.set_thumbnail(url="https://static.wikia.nocookie.net/e0d584f0-ab46-4ea6-ac2c-caf14cd14c7c/scale-to-width/755")
                embed.add_field(name="猜拳", value="", inline=False)
                embed.add_field(name="你輸了!", value="哇哈哈哈哈 輕輕鬆鬆", inline=False)
                await interaction.response.send_message(embed=embed)
                player = False
            elif bot_play == 0:
                embed=discord.Embed(color=0x00ff62)
                embed.set_thumbnail(url="https://pbs.twimg.com/media/FA5s2mlWYAMn7tr.jpg")
                embed.add_field(name="猜拳", value="", inline=False)
                embed.add_field(name="你贏了!", value="social credit +15", inline=False)
                await interaction.response.send_message(embed=embed)
                player = False



@bot.slash_command(description="剪刀石頭布")
async def mora(ctx):
    global bot_play
    global player
    bot_play = random.randint(0, 2)
    player = True
    embed = discord.Embed(color=0xa3ffc6)
    embed.set_thumbnail(url="https://emojiisland.com/cdn/shop/products/Nerd_with_Glasses_Emoji_2a8485bc-f136-4156-9af6-297d8522d8d1_grande.png?v=1571606036")
    embed.add_field(name="猜拳", value="", inline=False)
    embed.add_field(name="點擊下面按鈕和我猜拳!", value="", inline=False)
    embed.add_field(name="贏的社會信用點數+15分 | 輸的給OsGa信義區地契乙張", value="請注意 按鈕被點擊就無法再遊玩 必須重發一次指令才可以", inline=False)
    await ctx.respond(embed=embed, view=moraView())
    print(bot_play) 
    


#how long is gg
@bot.slash_command(descripiton="測量你有多長!")
async def how_long_is_gg(ctx):
    long = random.randint(0,11)
    if long == 11:
        gg = "8=========================================D"
    else:
        gg = "8"
        for i in range(long):
            gg += "="
        gg += "D" 
    await ctx.respond(f"你的GG有這麼長:\n `{gg}`")



#time
@bot.slash_command(description="獲取現在時間")
async def time(ctx):
    current_time = datetime.now()
    current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    await ctx.respond(f"現在時間為:`{current_time_str}`")

    



bot.run(token["token"])
