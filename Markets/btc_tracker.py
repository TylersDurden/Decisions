import urllib, time, sys, fUtility


def get_current_price():
    """
    Get the current price of BTC in USD, Pound, and Euro
    and return as dict indexed by currency.
    :return {}:
    """
    btc_data = urllib.urlopen(url='https://api.coindesk.com/v1/bpi/currentprice.json').read()
    prices = []
    market = {}
    for item in btc_data.split('","'):
        try:
            price = item.split('rate":"')[1].split('\n')[0]
            prices.append(price)
        except IndexError:
            pass
    if len(prices) == 3:
        market['Euro'] = prices.pop()
        market['Pound'] = prices.pop()
        market['USD'] = prices.pop()
    return market


def find_historic_data(verbose):
    cmd = 'find -name *history* | cut -b 3-'
    history_file = fUtility.execute(cmd=cmd,save_output=False).pop()
    historic_data = fUtility.swap(history_file, False)
    if verbose:
        print str(len(historic_data)) + " Historic Data Points Retrieved from Disk"
    return historic_data


def get_historic_price(start_date,end_date):
    """
    Ex Input:
    start_date = '2013-09-01'
    end_date = '2019-01-24'

    :param start_date:
    :param end_date:
    :return:
    """
    cmd = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=' +\
        start_date+'&end='+end_date
    data = urllib.urlopen(cmd).readlines()
    price_pts = []
    for item in data:
        try:
            for price in item.split(','):
                if len(price.replace('\n','').split(':'))==2:
                    price_pts.append(price)
        except IndexError:
            pass
    price_pts.pop()
    return price_pts


def get_last_market_close_date():
    date = time.localtime()
    if date.tm_yday > 2:
        d = date.tm_yday - 1
    else:
        d = 28
    m = date.tm_mon
    if m < 10:
        m = '0' + str(m)
    y = date.tm_year
    return str(y) + '-' + str(m) + '-' + str(d)


def historic_data_dump(data, filename):
    dump = ''
    data_count = 0
    for point in data:
        dump += point+'\n'
        data_count += 1
    open(filename, 'w').write(dump)
    print str(len(data)) + " Price-Points Dumped to " + filename
    return 0


def main():
    find_historic_data()
    top3_mkt_btc = get_current_price()

    if '-update_history' in sys.argv:
        # Get historic data
        start = '2013-01-01'
        yesterday = get_last_market_close_date()
        historic_data = get_historic_price(start, yesterday)
        print str(len(historic_data)) + " Historic Price Points Collected"
        historic_data_dump(historic_data, 'history190125.txt')


if __name__ == '__main__':
    main()