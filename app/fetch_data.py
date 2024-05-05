import discord
import asyncio
import pandas as pd
import altair as alt
import os

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 757271564977832079
THREAD_ID = 1205565888183668736
CSV_DATA_PATH = "data/cacajournal.csv"
messages = []

class MyBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, intents=intents)
        
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        await self.extract_messages_from_thread(THREAD_ID)
        await self.close()  # Close the bot after fetching the messages

    async def extract_messages_from_thread(self, thread_id):
        print("Bot is ready and will now try to fetch messages from the thread.")
        thread = await self.fetch_channel(thread_id)
        if isinstance(thread, discord.Thread):
            print(f"Found the thread: {thread.name}, fetching messages...")
            async for message in thread.history(limit=None):
                messages.append([message.author.name, message.content, message.created_at])
        else:
            print("Provided ID does not belong to a thread.")

    async def close(self):
        await super().close()
        print("Bot has been closed.")

# Run the bot
def get_discord_data():
    bot = MyBot()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.start(TOKEN))
    df = pd.DataFrame(messages, columns=["name", "message", "timestamp"]).query("message == '💩'")
    df["date"] = pd.to_datetime(df["timestamp"].dt.date)
    df["hour"] = df["timestamp"].dt.hour
    df.to_csv("data/cacajournal.csv", index=False)


def load_data_from_csv():
    """Load data from a CSV file."""
    return pd.read_csv(CSV_DATA_PATH)