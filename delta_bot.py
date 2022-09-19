import discord, time, random
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

#READY
@client.event
async def on_ready():
    print("Working as {0.user} :)".format(client))

@client.event
async def on_message(ctx):
    #PREVENTS RESPONDING TO ITSELF
    if ctx.author == client.user:
        return

    #TRUTH OR TRUTH
    if ctx.content.lower() == "make truth":
        truthL = ["What is your most painful experience?", "What is your biggest regret in life?", "What is something you know you would never do?", "What is your most embarrassing childhood memory?", "If you were a character in your favorite TV show, who would you be and why?", "What dream of yours have you already achieved?", "What would you say is your biggest flaw?", "What is one secret you have never told anyone until now?", "What is your most treasured material possession?", "If you woke up tomorrow as a millionaire, what would you get first?", "Your last meal on earth, what would be on the menu?", "If you could be reincarnated as any animal after death which would you pick?", "If you met a genie, what would your three wishes be?", "What’s one thing you’d do if you knew there no consequences?", "Do you believe in any superstitions? If so, which ones?", " What do you think happens when you die?", "Have you ever been arrested?", "What is a weird food that you love?", "Have you ever stolen anything?", "What is the weirdest thing you’ve ever done in public?", "If someone went through your closet, what is the weirdest thing they’d find?", "What are some things you think about when sitting on the toilet?", "What, if any, sport do you absolutely hate against popular opinion?", "Have you ever accidentally walked into a wall or building?", "You’re in a public restroom and just pooped, then you realized your stall has no toilet paper. What do you do?", "What is the most illegal thing you’ve ever done?", "What was your favorite childhood video game?", "If you could suddenly become invisible, what would you do?", "Have you ever waved at someone thinking they saw you when really they didn’t? What did you do when you realized it?", "Describe the strangest dream you’ve ever had.", "What is your biggest and most irrational fear?", "What is the scariest movie you have ever seen?", "The world ends next week and you can do anything you want (even if it’s illegal). What would you do?", "What your favorite children's movie?", "What is the most food you’ve eaten in a single sitting?", "What is your favorite type of ice cream?"]
        count = len(truthL)
        rTruth = truthL[random.randint(0,count)]
        await ctx.channel.send(rTruth)

    #FEEDBACK COMMAND
    if ctx.content.lower() == "make feedback":
        ratings = [8.0, 9.5, 5.0, 7.0, 8.0, 8.0, 8.0, 8.0, 8.0]
        sum = 0.0
        for i in ratings:
            sum  = sum + i
            finalRating = sum/len(ratings)
        await ctx.channel.send(finalRating)

    #UPDATE LOG
    if ctx.content.lower() == "make update log":
        await ctx.channel.send("Delta Creation 1.0!")
        await ctx.channel.send("Update 1.2 - 4/12: Truth or truth command!")

#Driver
client.run(token)
