import pandas as pd

def run():
    df = pd.read_csv("sample_data.csv")
    df["age"] = df["age"] + 1
    print(df)

if __name__ == "__main__":
    run()
