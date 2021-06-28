# Taken from klib
# More data cleaning functionality can be found here: https://github.com/akanz1/klib

import pandas as pd
import re


def clean_column_names(data: pd.DataFrame, hints: bool = True) -> pd.DataFrame:
    """ Cleans the column names of the provided Pandas Dataframe and optionally \
        provides hints on duplicate and long column names.

    Parameters
    ----------
    data : pd.DataFrame
        Original Dataframe with columns to be cleaned
    hints : bool, optional
        Print out hints on column name duplication and colum name length, by default \
        True

    Returns
    -------
    pd.DataFrame
        Pandas DataFrame with cleaned column names
    """

    # Handle CamelCase
    for i, col in enumerate(data.columns):
        matches = re.findall(re.compile("[a-z][A-Z]"), col)
        column = col
        for match in matches:
            column = column.replace(match, match[0] + "_" + match[1])
            data.rename(columns={data.columns[i]: column}, inplace=True)

    data.columns = (
        data.columns.str.replace("\n", "_")
        .str.replace("(", "_")
        .str.replace(")", "_")
        .str.replace("'", "_")
        .str.replace('"', "_")
        .str.replace(".", "_")
        .str.replace("-", "_")
        .str.replace(r"[!?:;/]", "_", regex=True)
        .str.replace("+", "_plus_")
        .str.replace("*", "_times_")
        .str.replace("<", "_smaller")
        .str.replace(">", "_larger_")
        .str.replace("=", "_equal_")
        .str.replace("ä", "ae")
        .str.replace("ö", "oe")
        .str.replace("ü", "ue")
        .str.replace("ß", "ss")
        .str.replace("%", "_percent_")
        .str.replace("$", "_dollar_")
        .str.replace("€", "_euro_")
        .str.replace("@", "_at_")
        .str.replace("#", "_hash_")
        .str.replace("&", "_and_")
        .str.replace(r"\s+", "_", regex=True)
        .str.replace(r"_+", "_", regex=True)
        .str.strip("_")
        .str.lower()
    )

    dupl_idx = [i for i, x in enumerate(data.columns.duplicated()) if x]
    if dupl_idx:
        dupl_before = data.columns[dupl_idx].tolist()
        data.columns = [
            col if col not in data.columns[:i] else col + "_" + str(i)
            for i, col in enumerate(data.columns)
        ]
        if hints:
            print(
                f"Duplicate column names detected! Columns with index {dupl_idx} and "
                f"names {dupl_before}) have been renamed to "
                f"{data.columns[dupl_idx].tolist()}."
            )

    long_col_names = [x for x in data.columns if len(x) > 25]
    if long_col_names and hints:
        print(
            "Long column names detected (>25 characters). Consider renaming the "
            f"following columns {long_col_names}."
        )

    return data
