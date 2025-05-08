import pandas as pd


def process_data(data: pd.DataFrame,
                 old_name: str,
                 new_name: str) -> pd.DataFrame:
    """
    Process the data by dropping NaN values, duplicates,
    resetting index, renaming columns, and changing data types.
    data: The DataFrame to process.
    old_name: The old column name to be renamed.
    new_name: The new column name.

    return: The processed DataFrame.
    """
    data = data.dropna()
    data = data.drop_duplicates()
    data = data.reset_index(drop=True)
    data = data.rename(columns={old_name: new_name})
    data = data.astype({"column_name": "int"})

    return data
