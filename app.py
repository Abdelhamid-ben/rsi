#ABDELHAMID BEN MESSAOUD
#https://github.com/Abdelhamid-ben
#TA-Lib==0.4.25
from flask import Flask, render_template
import pandas as pd
import talib
import ccxt
import sqlite3
import time
binance_exchange = ccxt.binance()
app = Flask(__name__)
def clear_database():
    try:
        conn = sqlite3.connect('rsi_data.db')
        cursor = conn.cursor()
        
        # Delete all records from the rsi_data table
        cursor.execute("DELETE FROM rsi_data")
        
        conn.commit()
        conn.close()
        print("Database cleared successfully.")
    except Exception as e:
        print("Error clearing the database:", str(e))
# Function to update RSI data in the SQLite database
clear_database()
def update_rsi_data():
    while True:
        timeinterval = '4h'  # Define your time interval
        symbols = binance_exchange.load_markets()
        for symbol in symbols:
            if symbol.endswith('/USDT'):
                try:
                    ohlcv = binance_exchange.fetch_ohlcv(symbol, timeframe=timeinterval, limit=200)
                    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                    df['close'] = df['close'].astype(float)
                    rsi = talib.RSI(df['close'])
                    rsi = rsi.iloc[-1]
                    rsi = round(rsi, 4)

                    if rsi != 0:
                        # Check if symbol exists in the database
                        conn = sqlite3.connect('rsi_data.db')
                        cursor = conn.cursor()
                        cursor.execute("SELECT * FROM rsi_data WHERE symbol=?", (symbol,))
                        existing_data = cursor.fetchone()
                        
                        if existing_data:
                            # Symbol exists, update the RSI value
                            cursor.execute("UPDATE rsi_data SET rsi=? WHERE symbol=?", (rsi, symbol))
                        else:
                            # Symbol does not exist, insert a new record
                            cursor.execute("INSERT INTO rsi_data (symbol, rsi) VALUES (?, ?)", (symbol, rsi))
                        
                        conn.commit()
                        conn.close()
                except Exception as e:
                    print(f"Error for {symbol}: {str(e)}")


        print("finish")
       # time.sleep(4 * 60 * 60)  # Sleep for 4 hours before updating again

# Define the route to display RSI data
@app.route('/')
def index():
    # Fetch the most recent RSI data from the database
    conn = sqlite3.connect('rsi_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT symbol, rsi FROM rsi_data ") ##WHERE rsi < 30 OR rsi > 70
    rsi_data = cursor.fetchall()
    conn.close()
    return render_template('index.html', rsi_data=rsi_data)


if __name__ == '__main__':
    # Start a separate thread to update RSI data periodically
    import threading
    update_thread = threading.Thread(target=update_rsi_data)
    update_thread.start()    
    app.run(debug=True, host='0.0.0.0', port=1337)

