# Flask RSI Data Collector

This script serves as a dynamic and real-time dashboard for monitoring the Relative Strength Index (RSI) data of various cryptocurrency pairs on Binance. Leveraging the Binance API, the script systematically gathers comprehensive OHLCV (Open/High/Low/Close/Volume) data for all available Cryptocurrencies to USDT pairs, including popular examples like BTC/USDT and ALT/USDT.

Designed with simplicity in mind, the script utilizes the powerful ccxt library to seamlessly interact with the Binance API. The acquired data is intelligently structured into a Python DataFrame, facilitating efficient manipulation and organization of the information. This DataFrame acts as the foundation for the talib.RSI calculation, providing real-time insights into the relative strength of the selected cryptocurrency pairs.

The calculated RSI values are not only processed but also persistently stored in an SQLite database. This ensures a continuous and up-to-date record of RSI trends over time. The culmination of this data is visualized through a straightforward Flask web application.

The web application, while intentionally kept simple in design, offers a user-friendly interface (responsive and i am not good at web design :P) for exploring and interpreting the RSI data. The integration of Flask facilitates seamless communication between the backend and frontend, enabling users to effortlessly access and comprehend the dynamic RSI metrics.

It's important to note that the script is crafted to run indefinitely, ensuring the continuous collection and analysis of cryptocurrency data. While a time.sleep option is provided, allowing users to manage resource consumption, the script's adaptability and efficiency are designed to support prolonged and uninterrupted operation.

In summary, this script amalgamates the power of the Binance API, ccxt, Python's data manipulation capabilities, and Flask's web framework to deliver a robust, real-time RSI monitoring tool for cryptocurrency enthusiasts. Whether tracking market trends or exploring investment opportunities, this script provides a reliable and user-friendly solution.


## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#LICENSE)

  
## Prerequisites
Ensure you have the following dependencies installed:

Option 1: Docker

Docker
Option 2: Manual Installation

Flask==2.2.2

pandas==1.5.2

ccxt==2.5.83

TA-Lib==0.4.25


## Installation

Option 1: Docker

Clone the repository:

`git clone https://github.com/Abdelhamid-ben/rsi.git`

`cd rsi`

Build the Docker image:

`docker build -t rsiapp`

`docker run -p 8080:8080 rsiapp`


Option 2: Manual Installation

Install Python dependencies:

`pip install -r requirements.txt`

Run the application:

`python app.py`

## Configuration

Adjust the timeframe in the app.py file according to your preference. The default is set to 4 hours. Examples include:

1h for a 1-hour timeframe.

2h for a 2-hour timeframe.

15m for a 15-minute timeframe.


## Contributing

Building the container might take a significant amount of time due to TA-LIB library requirements, including compilation and additional dependencies. If you have ideas on optimizing this process or any other improvements, contributions are welcome!

A new simple script that sends telegramsignals (BUY/SELL) will be published soon.

Thank you.


## LICENSE

MIT License

Copyright (c) 2023 Abdelhamid BEN MESSAOUD

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



