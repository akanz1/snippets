# Replace parts of strings in a list


def replace_substring(strings_list, dictionary):
    """Replace parts of strings in a list according to the key-value mapping of a dictionary.

    Example:
    -------
    lst = ['gloomy', 'carpet', 'house', 'mystery']
    mapping = {'my': 'your', 'car': 'train'}

    rename_substrings_from_dict(lst, mapping)
    >>> ['glooyour', 'trainpet', 'house', 'yourstery']

    Parameters
    ----------
    strings_list : List
        List of strings
    dictionary : Dict
        Mapping of the (sub-)strings

    Returns
    -------
    New list with updated strings
    """

    for i, string in enumerate(strings_list):
        for key, value in dictionary.items():
            string = string.replace("".join([key, "_"]), "".join([value, "_"]))
            strings_list[i] = string
    return strings_list
