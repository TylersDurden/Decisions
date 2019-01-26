import urllib, time, sys, fUtility, btc, os


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
    open(filename, 'a').write(dump)
    print str(len(data)) + " Price-Points Dumped to " + filename
    return 0


def running_log(N, delay):
    today = time.localtime()
    date = str(today.tm_mon)+'/'+str(today.tm_yday)+'/'+str(today.tm_year)
    differential = {}
    t0 = time.time()
    print "| Adding to BTC_TRACKER LOG | DATE:"+date+"|"
    log_name = 'log'+str(today.tm_mon)+str(today.tm_yday)+str(today.tm_year)+'.txt'
    ii = 0
    data_points = {}
    while ii < N:
        try:
            top3_mkt_btc = get_current_price()
            data_points[ii] = top3_mkt_btc.values()
            differential[ii] = top3_mkt_btc.values().pop() - top3_mkt_btc.values().pop()
            now = str(time.time()-t0)
            print '\033[1m\033[37m'+" < MARKET PRICES >"+'\033[32m'
            for mkt in top3_mkt_btc.keys():
                print mkt+" "+top3_mkt_btc[mkt]
                os.system('echo "' + mkt+" "+top3_mkt_btc[mkt]+'" >> '+log_name)
            print '\033[1m\033[38m Market Spread [Euro-USD] : '+str(differential[ii])+'\033[0m'
            print '\033[0m\033[1m '+date+' + '+now+'s\033[0m'

            ii += 1
        except KeyboardInterrupt:
            ii = N
        time.sleep(delay)
    return data_points, differential


def main():
    # btc_history = find_historic_data(True)
    BTC = btc.BTC()
    BTC.load_live_data(running_log(100,20), True)
    # title = 'livelog.txt'
    # historic_data_dump(data_points.values(), title)

    if '-update_history' in sys.argv:
        # Get historic data
        start = '2013-01-01'
        yesterday = get_last_market_close_date()
        historic_data = get_historic_price(start, yesterday)
        print str(len(historic_data)) + " Historic Price Points Collected"
        historic_data_dump(historic_data, 'history190125.txt')


if __name__ == '__main__':
    main()