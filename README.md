# Flask RSI Data Collector

This script collects Relative Strength Index (RSI) data for cryptocurrency pairs from Binance using the Binance API. The collected data is stored in an SQLite database and can be visualized using a Flask web application.
the design in simple (i am not good at web design :P).

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Contributing](#contributing)

## Prerequisites

Docker
_________________________
or 
_________________________
Flask==2.2.2

pandas==1.5.2

ccxt==2.5.83

TA-Lib==0.4.25

## Installation (Docker)

`git clone https://github.com/Abdelhamid-ben/rsi.git`
`cd rsi`

Build :
docker build -t mid .

Start :
`docker run -p 8080:8080 rsiapp`

## Configuration

You can change in the app.py the time frame (default 4h)

Example : 
1h > 1 hours timeframe

2h > 2 hours timeframe

15m > 15 timeframe


## Contributing

Well it will take a lot of time to build the container, that;s because i had a problem with TA-LIB library, it requires compilation and more libs, so if you have any idea how to avoid that, welcome.


