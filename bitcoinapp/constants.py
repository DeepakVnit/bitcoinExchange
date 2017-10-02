product_mapping = {}
product= ["LTC","ETH","ZEC","Dash","XRP","XMR"]
product_mapping["LTC"] = "Litecoin"
product_mapping["ETH"] = "Ethereum"
product_mapping["ZEC"] = "Zcash"
product_mapping["Dash"] = "Dash"
product_mapping["XRP"] = "Ripple"
product_mapping["XMR"] = "Monero"

markets = [""]
indianmarkets = ["BTCXIndia","Unocoin","ETHEXIndia"]

generateAvgUrl = "https://min-api.cryptocompare.com/data/generateAvg"

marketinfo = [
    {
        "product": [
                    {
                        "productsymbol":"XRP",
                        "productname": "Ripple"
                     }
                 ],
        "exchange": "BTCXIndia",
        "currency": ["INR"]

    },
    {
        "product": [
                    {
                        "productsymbol":"BTC",
                        "productname": "Bitcoin"
                    }
                ],
        "exchange":"Unocoin",
        "currency": ["INR"],
    },

    {
        "product": [
                    {
                        "productsymbol":"BTC",
                        "productname": "Bitcoin"
                    },
                    {
                        "productsymbol":"LTC",
                        "productname": "Litecoin"
                    }
                ],
        "exchange":"ETHEXIndia",
        "currency": ["INR"],
    },
]