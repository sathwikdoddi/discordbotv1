import discord
import random
import requests
import os
from discord.ext import commands
from discord.ext.commands import Bot

# Link to add bot: https://discord.com/api/oauth2/channelize?client_id=709233313176485910&permissions=8&scope=bot

client = commands.Bot(command_prefix = '!')

#jokes and memes classes
def tell_joke():
	url = 'https://icanhazdadjoke.com/'
	response = requests.get(url, headers={"Accept": "application/json"})
	data = response.json()
	return str(data['joke'])

def get_meme():
	url = 'https://meme-api.herokuapp.com/gimme'
	response = requests.get(url, headers={"Accept": "application/json"})
	data = response.json()
	return str((data['url']))


#blackjack classes
class Card:
    def __init__(self, value, points, suit):
        self.value = value
        self.points = value
        if value in ["J", "Q", "K"]:
            self.points = 10
        elif value == "A":
            self.points = 11
        self.suit = suit

    def get_value(self):
        return self.value

    def get_points(self):
        return self.points

    def change_points(self, point_val):
        self.points = point_val

    def string( self ):
        return str(self.value) + " of " + self.suit

    def print_card(self):
        return str(self.value) + " of " + self.suit + " with " + str(self.points) + " points"

class Deck:
    def __init__(self):
        self.deck = []
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        for suit in suits:
            for card in cards:
                if card in ["J", "Q", "K"]:
                    points = 10
                elif card == "A":
                    points = 11
                else:
                    points = int(card)
                self.deck.append(Card(card, points, suit))

    def sum_cards(self, list_cards):
        sum = 0
        for card in self.deck:
            sum += card.get_points()
        return sum

    def draw(self, num):
        cards = []
        for i in range(0,num):
            c = random.choice(self.deck)
            cards.append(c)
            self.deck.remove(c)
        return cards

class Hand:
    def __init__(self):
        self.deck = []
        self.not_done = True

    def add_card(self, cards):
        for card in cards:
            self.deck.append(card)

    def sum_cards(self):
        sum = 0
        for card in self.deck:
            sum += card.get_points()
        return sum

    def dealer_print(self):
        return self.deck[0].string()

    def print_cards(self):
        ret_str = ""
        for card in self.deck:
            ret_str += card.string() + ", "
        return ret_str[0:len(ret_str) - 2]

    def ask_A(self):
        num_A = []
        for c in range(0, len(self.deck)):
            if self.deck[c].get_value() == "A" and self.deck[c].get_points() == 11:
                num_A.append(c)
        for i in num_A:
            print ("Your cards are " + str(self.print_cards()) + ", Total is " +  str(self.sum_cards()) + "\n")
            val = str(input("Change an A from 11 points to 1 point? (Y or N): "))
            if val != "Y" and val != "N":
                print ("Please answer with Y or N")
            elif val == "Y":
                self.deck[i].change_points(1)

            print ("Your cards are " + str(self.print_cards()) + ", Total is " +  str(self.sum_cards()) + "\n")

    def done(self):
        self.not_done = False

    def get_done(self):
        return self.not_done

    def get_cards(self):
        return self.deck

#Events and Status
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!help"))
    print('Bot is active!')

@client.event
async def on_member_join(member):
    await member.send(f'You have joined a server with my presence')

#Commands/Command-like Events
#8ball
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#coinflip
@client.command(aliases=['coinflip'])
async def _coinflip(ctx):
    flipoutcome = ["heads",
                "tails",]
    await ctx.send(f'The outcome was {random.choice(flipoutcome)}')

#insults
@client.command(aliases=['attack'])
async def _attack(message):
  users = [client.get_user(499343877556273152), client.get_user(653974870379724835), client.get_user(618917655906222126), client.get_user(418403028463517708)]
  attackPerson = random.choice(users)
  insults = ["Your fat",
				"Lose Weight Fat piece of crap",
				"You were a mistake",
				"No one loves you",
				"You are retarded",
				"No one loves you and you are not loved",
				"Your momma so fat, when the doctor checked her weight she said Hey! That's my phone number!"]
  await attackPerson.send(f'{random.choice(insults)}')

@client.command(aliases=['attackSathwik'])
async def _attackDoddi(message):
	user = client.get_user(499343877556273152)
	insults = ["Your fat",
				"Lose Weight Fat piece of crap",
				"You were a mistake",
				"No one loves you",
				"You are retarded",
				"No one loves you and you are not loved",
				"Your momma so fat, when the doctor checked her weight she said Hey! That's my phone number!"]
	await user.send(f'{random.choice(insults)}')

@client.command(aliases=['attackJaithra'])
async def _attackJaithra(message):
	user = client.get_user(653974870379724835)
	insults = ["Your fat",
				"Lose Weight Fat piece of crap",
				"You were a mistake",
				"No one loves you",
				"You are retarded",
				"No one loves you and you are not loved",
				"Your momma so fat, when the doctor checked her weight she said Hey! That's my phone number!"]
	await user.send(f'{random.choice(insults)}')

@client.command(aliases=['attackManas'])
async def _attackMoonas(message):
	user = client.get_user(618917655906222126)
	insults = ["Your fat",
				"Lose Weight Fat piece of crap",
				"You were a mistake",
				"No one loves you",
				"You are retarded",
				"No one loves you and you are not loved",
				"Your momma so fat, when the doctor checked her weight she said Hey! That's my phone number!"]
	await user.send(f'{random.choice(insults)}')

@client.command(aliases=['attackRamsey'])
async def _attackRamsey(message):
	user = client.get_user(418403028463517708)
	insults = ["Your fat",
				"Lose Weight Fat piece of crap",
				"You were a mistake",
				"No one loves you",
				"You are retarded",
				"No one loves you and you are not loved",
				"Your momma so fat, when the doctor checked her weight she said Hey! That's my phone number!"]
	await user.send(f'{random.choice(insults)}')

@client.command(aliases=['attackMe'])
async def _attackMe(message):
	insults = ["Your fat",
				"Lose Weight Fat piece of crap",
				"You were a mistake",
				"No one loves you",
				"You are retarded",
				"No one loves you and you are not loved",
				"Your momma so fat, when the doctor checked her weight she said Hey! That's my phone number!"]
	await message.author.send(f'{random.choice(insults)}')

#bet on coinflip
@client.command(aliases=['betcoin'])
async def _betcoin(ctx, *, bet):
    flipoutcomes = ["heads", "tails"]
    actualoutcome = random.choice(flipoutcomes)

    if bet == actualoutcome:
        await ctx.send(f'Congratulations! You were correct, the outcome was {actualoutcome}')
    else:
        await ctx.send(f'YOU LOSE SUCKER, THE OUTCOME WAS {actualoutcome}')

    if actualoutcome == flipoutcomes[0]:
        await ctx.send(f'https://usathss.files.wordpress.com/2015/10/us-quarter.gif')
    else:
        await ctx.send(f'https://www.nicepng.com/png/full/146-1464848_quarter-tail-png-tails-on-a-coin.png')

#whoami
@client.command(aliases=['whoami'])
async def _whoami(message):
    bottomline = ["and you are not loved...",
                "and no one likes you...",
                "and you are gay...",
                "and you have no friends...",
                "and I love you...",
                "and you are a psychopath...",
                "and you are one of the boys :)...",
                "and everyone loves you...",
                "and no hate shall affect you...",
                "and your a piece of crap..."]
    await message.send(f'You are {message.author}\n{random.choice(bottomline)}')

#Event Messages
@client.event
async def on_message(message):
  #jokes and stuff
    channel = message.channel
    content = message.content
    if content == '!joke':
      joke = tell_joke()
      await channel.send(joke)

    if content.lower() == 'go corona':
      await channel.send('Corona Go!')

    if content == '!meme':
      meme = get_meme()
      await channel.send(meme)
  #blackjack
    if message.content == "!blackjack":
        global deck, dealer_cards, players, player_cards
        deck = Deck()
        dealer_cards = Hand()
        dealer_cards.add_card(deck.draw(2))
        players = [dealer_cards]

        player_cards = Hand()
        player_cards.add_card(deck.draw(2))
        players.append(player_cards)
        await message.channel.send("Blackjack starting, type !dealcards to see cards")
    elif message.content == ("!dealcards"):
        sum = -1
        while players[0].not_done:
            sum = players[0].sum_cards()
            if sum >= 17:
                players[0].done()
            else:
                players[0].add_card(deck.draw(1))
        if player_cards.sum_cards() == 21 and len(player_cards.get_cards()) == 2:
            player_sum = players[1].sum_cards()
            dealer_sum = players[0].sum_cards()
            if player_sum != dealer_sum or len(players[1].get_cards()) != len(players[1].get_cards()):
                await message.channel.send("BLACKJACK! You Win! Type !score to see your score.")
            else:
                await message.channel.send("You tied! Type !score to see your score")
        else:
            await message.channel.send("Your cards are " + player_cards.print_cards() + ", Total Score: " + str(player_cards.sum_cards()) + "\nDealer has " + players[0].dealer_print() + "\nType !hit to hit and !slide to stay")
    elif message.content == ("!slide"):
        player_sum = players[1].sum_cards()
        dealer_sum = players[0].sum_cards()
        print (player_sum, dealer_sum)
        if player_sum > 21:
            await message.channel.send("You lose to dealer... Type !score to see score")
        elif dealer_sum > 21 or player_sum > dealer_sum:
            await message.channel.send("You beat the dealer! Type !score to see score")
        elif player_sum == dealer_sum:
            await message.channel.send("You tie with the dealer Type !score to see score")
        elif dealer_sum > player_sum:
            await message.channel.send("You lose to dealer... Type !score to see score")
        else:
            await message.channel.send("I don't know.......")
    elif message.content == ("!hit"):
        players[1].add_card(deck.draw(1))
        sum = players[1].sum_cards()
        if sum > 21:
            players[1].ask_A()
            sum = players[1].sum_cards()
            if sum > 21:
                players[1].done()
                await message.channel.send("Bust! You lose! Type !score to see score")
        elif sum == 21 and len(players[1].get_cards()) == 2:
            await message.channel.send("BLACKJACK! Type !score to see score")
            players[1].done()
        elif sum < 21:
            await message.channel.send("Your cards are " + player_cards.print_cards() + ", Total Score: " + str(player_cards.sum_cards()) + "\nDealer has " + players[1].dealer_print() + "\nType !hit to hit and !slide to stay")
    elif message.content == ("!score"):
        player_sum = players[1].sum_cards()
        dealer_sum = players[0].sum_cards()
        await message.channel.send("Scores: You: " + str(player_sum) + " vs. Dealer: " + str(dealer_sum) + "\nType !blackjack to play again")

    await client.process_commands(message)

#Runs the Bot
client.run('NzA5MjMzMzEzMTc2NDg1OTEw.Xrl6CA.PQVDKv0fuZErpaReL-OjNQaEU74')
