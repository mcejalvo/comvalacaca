
from plot import *
import threading

st.set_page_config(layout="wide")
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
    df.to_csv("data/cacajournal.csv")
    return df

def main():
    # df = load_data_from_csv()    
    
    if st.button("Cargar últimas caquitas"):
        # This will re-run the get_discord_data() and bypass cache
        df = get_discord_data()
    else:
        df = load_data_from_csv()

    st.title('Torre Caca de Control')
    with st.expander("Ver detalle caquitas"):
        st.dataframe(df[["name", "message", "timestamp"]])
    st.header("¿Horas preferidas para la Cacación?")
    st.altair_chart(bar_distribution_per_person_chart(df), use_container_width=True)



if __name__ == "__main__":
    main()