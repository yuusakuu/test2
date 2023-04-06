import pandas as pd

__all__=["loading"]

def loading(path:str, col:str="Date") -> pd.DataFrame :
    return pd.read_csv(path, parse_dates=[col],index_col=col)