import streamlit as st
st.set_page_config(layout="wide")

from plot import *
import threading



def get_discord_data():
    def start_bot():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        bot = MyBot()
        loop.run_until_complete(bot.start(TOKEN))

    # Start the bot in a separate thread to avoid blocking Streamlit's main thread
    thread = threading.Thread(target=start_bot)
    thread.start()
    thread.join()  # Wait for the thread to finish

    # Once data is fetched, process it
    df = pd.DataFrame(messages, columns=["name", "message", "timestamp"]).query("message == '💩'")
    df["date"] = pd.to_datetime(df["timestamp"].dt.date)
    df["hour"] = pd.to_datetime(df["timestamp"]).dt.hour
    return df

def main():
    df = get_discord_data()
    st.title('Torre Caca de Control')
    st.header("¿Horas preferidas para la Cacación?")
    st.altair_chart(bar_distribution_per_person_chart(df), use_container_width=True)



if __name__ == "__main__":
    main()