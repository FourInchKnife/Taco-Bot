import discord
import json
with open("key.json","r") as file:
    token = json.loads(file.read())[0]

class Botto(discord.Client):
    async def on_ready(self):
        await self.change_presence(status=discord.Status.invisible)
        print("Logged in as {}".format(str(self.user.name)))
    async def on_message(self, message):
        if "taco" in message.content.lower() or "🌮" in message.content:
            await message.add_reaction("🌮")

bot = Botto()
bot.run(token)
