import pandas as pd


class ExcelWriter:

    def __init__(self, data) -> None:
        self.df = pd.DataFrame(data)

    def save(self, filename='dict1.xlsx'):
        self.df.to_excel(filename, index=False)


if __name__ == "__main__":
    dict1 = {"number of storage arrays": 45, "number of ports":2390}
    dict2 = {"number of storage arrays": 99, "number of ports":5555}
    list3 = [dict1, dict2]

    excel = ExcelWriter(list3)
    print(excel.df)
    excel.write_excel()



