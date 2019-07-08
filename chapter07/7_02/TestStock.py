from Stock import Stock

def main():
    stock = Stock("INTC", "Intel Corporation", 20.5, 20.35)
    print("价格改变的百分比是{:.2}%".format(stock.getChangePercent()))

if __name__ == "__main__":
    main()