import pandas as pd

def read_user_ids_from_csv(path: str):
    df = pd.read_csv(path)
    if "user_id" not in df.columns:
        raise ValueError("CSV precisa conter a coluna 'user_id'")
    return df
