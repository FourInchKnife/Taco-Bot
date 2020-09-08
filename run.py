import discord
import json
import asyncio

with open("keys.json","r") as file:
    token = json.loads(file.read())["bot_token"]

class TacoBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.owner=600130839870963725
        self.tacophrases = \
"""
**Tacos**
A taco (US: /ˈtɑːkoʊ/, UK: /ˈtækoʊ/, Spanish: [ˈtako]) is a traditional Mexican dish consisting of a small hand-sized corn or wheat tortilla topped with a filling. The tortilla is then folded around the filling and eaten by hand. A taco can be made with a variety of fillings, including beef, pork, chicken, seafood, beans, vegetables, and cheese, allowing great versatility and variety. They are often garnished with various condiments, such as salsa, guacamole, or sour cream, and vegetables, such as lettuce, onion, tomatoes, and chiles. Tacos are a common form of antojitos, or Mexican street food, which have spread around the world.

Tacos can be contrasted with similar foods such as burrito, which are often much larger and rolled rather than folded, taquitos which are rolled and fried, or chalupas/tostadas, in which the tortilla is fried before filling.

**Etymology**
Various taco ingredients

The origins of the taco are not precisely known, and etymologies for the culinary usage of the word are generally theoretical.[1] According to the Real Academia Española, publisher of Diccionario de la Lengua Española, the word taco describes a typical Mexican dish of a maize tortilla folded around food.[2] This meaning of the Spanish word "taco" is a Mexican innovation, but in other dialects "taco" is used to mean "wedge; wad, plug; billiard cue; blowpipe; ramrod; short, stocky person; [or] short, thick piece of wood." In this non-culinary usage, the word "taco" has cognates in other European languages, including the French word "tache" and the English word "tack (nail)."[citation needed]

According to one etymological theory, the culinary meaning of "taco" derives from its "plug" meaning as employed among Mexican silver miners, who used explosive charges in plug form consisting of a paper wrapper and gunpowder filling.[1]

Indigenous origins for the culinary word "taco" are also proposed. One possibility is that the word derives from the Nahuatl word "tlahco", meaning "half" or "in the middle,"[3] in the sense that food would be placed in the middle of a tortilla.[4] Furthermore, dishes analogous to the taco were known to have existed in Pre-Columbian society—for example, the Nahuatl word "tlaxcalli" (a type of corn tortilla).[3]

**Traditional Variations**
There are many traditional varieties of tacos:
Tacos al pastor made with adobada meat.

    Tacos al pastor ("shepherd style") or tacos de adobada are made of thin pork steaks seasoned with adobo seasoning, then skewered and overlapped on one another on a vertical rotisserie cooked and flame-broiled as it spins.[7][8]
    Tacos de asador ("spit" or "grill" tacos) may be composed of any of the following: carne asada tacos; tacos de tripita ("tripe tacos"), grilled until crisp; and, chorizo asado (traditional Spanish-style sausage). Each type is served on two overlapped small tortillas and sometimes garnished with guacamole, salsa, onions, and cilantro (coriander leaf). Also, prepared on the grill is a sandwiched taco called mulita ("little mule") made with meat served between two tortillas and garnished with Oaxaca style cheese. "Mulita" is used to describe these types of sandwiched tacos in the Northern States of Mexico while they are known as Gringa in the Mexican south and are prepared using wheat flour tortillas. Tacos may also be served with salsa.[7][8]
    Tacos de cabeza ("head tacos"), in which there is a flat punctured metal plate from which steam emerges to cook the head of the cow. These include: Cabeza, a serving of the muscles of the head; Sesos ("brains"); Lengua ("tongue"); Cachete ("cheeks"); Trompa ("lips"); and, Ojo ("eye"). Tortillas for these tacos are warmed on the same steaming plate for a different consistency. These tacos are typically served in pairs, and also include salsa, onion, and cilantro (coriander leaf) with occasional use of guacamole.[7][8]
    Tacos de camarones ("shrimp tacos") also originated in Baja California in Mexico. Grilled or fried shrimp are used, usually with the same accompaniments as fish tacos: lettuce or cabbage, pico de gallo, avocado and a sour cream or citrus/mayonnaise sauce, all placed on top of a corn or flour tortilla.[7][8][9]
    Tacos de cazo (literally "bucket tacos") for which a metal bowl filled with lard is typically used as a deep-fryer. Meats for these types of tacos typically include Tripa ("tripe", usually from a pig instead of a cow, and can also refer to the intestines); Suadero (tender beef cuts), Carnitas and Buche (Literally, "crop", as in bird's crop; or the esophagus of any animal.[10])[7][8]
    Tacos de lengua (beef tongue tacos),[11] which are cooked in water with onions, garlic, and bay leaves for several hours until tender and soft, then sliced and sautéed in a small amount of oil. "It is said that unless a taqueria offers tacos de lengua, it is not a real taqueria."[12]

Two fish tacos in Bonita, California

    Tacos de pescado ("fish tacos") originated in Baja California in Mexico, where they consist of grilled or fried fish, lettuce or cabbage, pico de gallo, and a sour cream or citrus/mayonnaise sauce, all placed on top of a corn or flour tortilla. In the United States, they were first popularized by the Rubio's fast-food chain, and remain most popular in California, Colorado, and Washington. In California, they are often found at street vendors, and a regional variation is to serve them with cabbage and coleslaw dressing on top.[7][8]
    Tacos dorados (fried tacos; literally, "golden tacos") called flautas ("flute", because of the shape), or taquitos, for which the tortillas are filled with pre-cooked shredded chicken, beef or barbacoa, rolled into an elongated cylinder and deep-fried until crisp. They are sometimes cooked in a microwave oven or broiled.[7][8]
    Tacos sudados ("sweaty tacos") are made by filling soft tortillas with a spicy meat mixture, then placing them in a basket covered with cloth. The covering keeps the tacos warm and traps steam ("sweat") which softens them.[7][13]

As an accompaniment to tacos, many taco stands will serve whole or sliced red radishes, lime slices, salt, pickled or grilled chilis (hot peppers), and occasionally cucumber slices, or grilled cambray onions.""".split("\n")
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
        elif message.content.startswith("!help"):
            await message.channel.send("No one can help you.\nNothing except TACOS")
        elif message.content.startswith("!shutdown"):
            await self.shutdown(message)
        elif message.content.startswith("!whatis"):
            for i in self.tacophrases:
                await message.channel.send(i)
                await asyncio.sleep(1)
        else:
            if "taco" in message.content.lower():
                await message.add_reaction("🌮")


bot = TacoBot()
bot.run(token)
