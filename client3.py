################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote: dict) -> tuple:
    """Produce all the needed values to generate a datapoint

    Args:
        quote (dict): a dictionary representing a stock quote
    Returns:
        tuple: a tuple of values"""
    # getDataPoint function should return correct tuple of stock name, bid_price, ask_price and price. Note: price of a stock = average of bid and ask

    stock = quote["stock"]
    bid_price = float(quote["top_bid"]["price"])
    ask_price = float(quote["top_ask"]["price"])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price


def getRatio(price_a: float, price_b: float) -> float:
    """Get ratio of price_a and price_b

    Args:
        price_a: float value of price a

        price_b: float value of price b
    Returns:
        float: a ratio of price a and price b
    """
    # getRatio function should return the ratio of the two stock prices
    return price_a / price_b


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(
            urllib.request.urlopen(QUERY.format(random.random())).read()
        )

        ratio_dict: dict = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            ratio_dict[stock] = price
            print(
                "Quoted %s at (bid:%s, ask:%s, price:%s)"
                % (stock, bid_price, ask_price, price)
            )
        # print(ratio_dict)
        print("Ratio %s" % getRatio(ratio_dict["ABC"], ratio_dict["DEF"]))
