import numpy as np, matplotlib.pyplot as plt, btc_tracker


class BTC:

    timeline = {}
    history = []

    def __init__(self):
        self.initialize()

    def initialize(self):
        raw_data = btc_tracker.find_historic_data(True)
        self.timeline = self.parse_raw_data(raw_data)

    def parse_raw_data(self, raw_data):
        data = {}
        II = 0
        prices = []
        for point in raw_data:
            values = point.replace('"','').replace('}','').replace('{','').split(':')
            try:
                date = values[0]
                price = values[1]
                data[date] = float(price.replace("'",''))
                prices.append(float(price.replace("'",'')))
                II += 1
            except IndexError:
                pass
        self.history = prices
        return data, prices

    def see_history(self):
        f = plt.figure()
        # plt.title(dA+' to '+dB)
        plt.plot(np.diff(np.array(self.history),0))
        plt.plot(self.history)
        plt.show()

    def load_live_data(self, data, show):
        d0 = []
        d1 = []
        d2 = []
        for point in data.keys():
            d0.append(data[point].pop())
            d1.append(data[point].pop())
            d2.append(data[point].pop())
        if show:

            plt.plot(np.arange(len(d0)),np.array(d0))
            plt.plot(np.arange(len(d1)),np.array(d1))
            plt.show()


def main():
    coins = BTC()
    coins.see_history()


if __name__ == '__main__':
    main()