import discord
import json

with open("keys.json","r") as file:
    token = json.loads(file.read())["bot_token"]

class Botto(discord.Client):
    def __init__(self):
        super().__init__()
        self.owner=600130839870963725
    async def shutdown(self,message):
        if message.author.id != self.owner:
            await message.channel.send("No.")
            return
        await self.close()
    async def on_ready(self):
        await self.change_presence(status=discord.Status.invisible)
        print("Logged in as {}".format(str(self.user.name)))
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.content.startswith("!shutdown"):
            await self.shutdown(message)
        elif message.content.startswith("!phaseup"):
            await self.phaseup(message)
        else:
            if "taco" in message.content:
                await message.add_reaction("🌮")


bot = Botto()
bot.run(token)
