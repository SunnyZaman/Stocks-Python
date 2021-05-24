import pandas as pd
class Stocks:
    def __init__(self,
                 company: str,
                 cost: int,
                 ):
        self.company = company
        self.cost = cost
    def toJson(self):
        return {
            'Company': self.company,
            'Cost': self.cost
        }

def main():
    data = {'Company': ['Tesla', 'Apple', 'Amazon',
                        'Tesla Co'], 'Cost': [20, 21, 19, 18]}
    df = pd.DataFrame(data)
    # print(df)
    companies = ['Tesla', 'Apple', 'Amazon']
    stocksArray = []
    for row in df.itertuples():
        for company in companies:
            if company  in row.Company:
                index = next((i for i, item in enumerate(stocksArray) if item.company == company), -1)
                if index == -1:
                    stocksArray.append(
                        Stocks(
                            company,
                            row.Cost
                        )
                    )
                else:
                    stocksArray[index].cost = int(stocksArray[index].cost) + int(row.Cost)
                print(index)
                pass
    newDF = pd.DataFrame.from_records([s.toJson() for s in stocksArray])
    print("df: ", newDF)
    return


if __name__ == "__main__":
    main()
