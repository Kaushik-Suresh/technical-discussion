import gc
import investpy

def add(x,y):
    return x+y

def eth():
    from_dt = "01/01/2000"
    to_dt = "14/04/2022"

    data_axis = investpy.get_crypto_historical_data(
        crypto="ethereum", from_date=from_dt, to_date=to_dt
    )
    data_axis.reset_index(inplace=True)
    print("{}-{}".format("Ethereum", "ETH"))
    print("\t\t Data Shape:", data_axis.shape)
    print("\t\tMaximum trx date:", data_axis["Date"].max())
    print("\t\tMinimum trx date:", data_axis["Date"].min())

    data_axis[["Date", "Open", "High", "Low", "Close", "Volume"]].to_csv(
        "Ethereum Historical Data.csv", index=False
    )

    return int(data_axis.shape[0])


def matic():
    from_dt = "01/01/2000"
    to_dt = "14/04/2022"

    print("\n\n\n")
    data_axis = investpy.get_crypto_historical_data(
        crypto="polygon", from_date=from_dt, to_date=to_dt
    )
    data_axis.reset_index(inplace=True)
    print("{}-{}".format("Matic", "MAT"))
    print("\t\t Data Shape:", data_axis.shape)
    print("\t\tMaximum trx date:", data_axis["Date"].max())
    print("\t\tMinimum trx date:", data_axis["Date"].min())

    data_axis[["Date", "Open", "High", "Low", "Close", "Volume"]].to_csv(
        "Matic Historical Data.csv", index=False
    )

    print("\n\n\n")
    return data_axis.shape[0]


def sol():

    from_dt = "01/01/2000"
    to_dt = "14/04/2022"

    data_axis = investpy.get_crypto_historical_data(
        crypto="solana", from_date=from_dt, to_date=to_dt
    )
    data_axis.reset_index(inplace=True)
    print("{}-{}".format("Solana", "SOL"))
    print("\t\t Data Shape:", data_axis.shape)
    print("\t\tMaximum trx date:", data_axis["Date"].max())
    print("\t\tMinimum trx date:", data_axis["Date"].min())

    data_axis[["Date", "Open", "High", "Low", "Close", "Volume"]].to_csv(
        "Solana Historical Data.csv", index=False
    )

    return data_axis.shape[0]


if __name__ == "__main__":
    gc.collect()
    e = eth()
    m = matic()
    s = sol()
    print(e)
    print(m)
    print(s)
