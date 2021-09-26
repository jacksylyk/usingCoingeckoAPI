from pycoingecko import CoinGeckoAPI


def coin_func(n):
    cg = CoinGeckoAPI()

    one_coin = cg.get_coins_markets(vs_currency='usd')

    list = []
    i = 0
    for x in one_coin:
        i = i + 1
        list.append(x['name'])
        if i == n:
            break

    return list


