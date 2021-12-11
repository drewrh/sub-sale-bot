# Sub Sale Bot

[A Twitter bot](https://twitter.com/SubSaleBot) that posts whenever Harris Teeter deli subs go on sale.

## Requirements

- Either:
  - Windows install of Chrome installed under `C:\Program Files\Google\`
  - Instance of [Selenium's standalone Chrome browser](https://github.com/SeleniumHQ/docker-selenium) on `localhost:4444`
- Twitter API and Access tokens inside `.env`

## Usage

1. `git clone https://github.com/drewrh/sub-sale-bot.git`
2. `cd ./sub-sale-bot`
3. `pip install -r requirements.txt`
4. `python3 ./sub_sale_bot.py`
