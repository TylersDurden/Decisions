import numpy as np, matplotlib.pyplot as plt, btc_tracker


class BTC:

    timeline = {}

    def __init__(self):
        self.initialize()

    def initialize(self):
        raw_data = btc_tracker.find_historic_data(True)
        self.timeline = self.parse_raw_data(raw_data)


    def parse_raw_data(self, raw_data):
        data = {}
        II = 0
        for point in raw_data:
            values = point.replace('"','').replace('}','').replace('{','').split(':')
            try:
                date = values[0]
                price = values[1]
                data[date] = float(price)
                II += 1
            except IndexError:
                pass
        return data

    def see_history(self):
        f = plt.figure()
        dA = self.timeline.keys().pop(0)
        dB = self.timeline.keys().pop(len(self.timeline.keys())-1)
        plt.title(dA+' to '+dB)
        plt.plot(np.linspace(1,len(self.timeline.values()),len(self.timeline.values())), np.array(self.timeline.values()))
        plt.show()

    @staticmethod
    def load_live_data(data, show):
        d0 = []
        d1 = []
        d2 = []
        for point in data.keys():
            d0.append(data[point].pop())
            d1.append(data[point].pop())
            d2.append(data[point].pop())
        if show:
            plt.figure()
            plt.plot(np.linspace(1, len(d0), len(d0)), np.array(d0))
            plt.plot(np.linspace(1, len(d0), len(d0)), np.array(d1))
            plt.plot(np.linspace(1, len(d0), len(d0)), np.array(d2))
            plt.show()

def main():
    BTC().see_history()


if __name__ == '__main__':
    main()