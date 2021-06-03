import os
import socket
import json
import asyncio
import datetime
import discord

TOKEN = ""
bot = discord.Client()


@bot.event
async def on_ready():
    ch = await bot.fetch_channel(850032445696376883)
    first_embed = discord.Embed()
    first_embed.set_author(name="Rocks Global Server - Status")
    first_embed.add_field(name="Currently:", value="undefined", inline=False)
    first_embed.add_field(name="Last checked:", value="undefined", inline=False)
    first_embed.set_footer(text="this is not server-specific nor does it track bugs")
    initial_message = await ch.send(embed=first_embed)
    print(f'I am {bot.user}')

    while True:


        s = socket.socket()

        success = True
        try:
            s.connect(("athemm.rocks", 9339))

        except:
            success = False
        s.close()


        if success:
            new_embed = discord.Embed()
            new_embed.set_author(name="Rocks Global Server - Status")
            new_embed.add_field(name="Currently:", value="**Up**", inline=False)
            new_embed.add_field(name="Last checked:", value=str(datetime.datetime.now()) + " **UTC+0**", inline=False)
            new_embed.set_footer(text="this is not server-specific nor does it track bugs")
            await initial_message.edit(embed=new_embed)
        else:
            new_embed = discord.Embed()
            new_embed.set_author(name="Rocks Global Server - Status")
            new_embed.add_field(name="Currently:", value="**Down :(**", inline=False)
            new_embed.add_field(name="Last checked:", value=str(datetime.datetime.now()) + " **UTC+0**", inline=False)
            new_embed.set_footer(text="this is not server-specific nor does it track bugs")
            await initial_message.edit(embed=new_embed)
        await asyncio.sleep(5)
bot.run(TOKEN)
