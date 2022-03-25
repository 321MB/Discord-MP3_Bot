import discord  
#Async lib, works with callbacks 
#callback: function is called when somthing happens

import BotToken

Token = BotToken.Token

from discord.ext import commands



Alive_check = ["bot","mp3bot", "MP3bot", "MP3Bot", "MP3 bot", "mp3 bot", 'BOT', "MP3BOT","Bot","Mp3bot","Mp3 Bot"]

client = discord.Client()

@client.event	#event register
async def on_ready(): #called when bot is ready to be used
	print('Login succes!! as {0.user}'.format(client))

@client.event     #event for a messege   

async def on_message(message):  
	msg = message
	if msg.author == client.user: #check if not own message
		return
	#if msg.content.startswith(tuple(Alive_check)):
	#	await msg.channel.send('still here...')
	if any(word in msg.content for word in Alive_check): #check if message contains mp3bot
		await msg.channel.send('still here...')

client.run(Token)#bot login