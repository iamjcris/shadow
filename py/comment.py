def parse_date_european(date_string: str) -> dict[str, int]:

#Docstrings
    """
    Description
    :param date_string: A date string in the format 'd/m/Y'
    :type date_string: str
    :return: a dictionary with date as key and number of days as value
    """

    #it split the date string using the "/" separator
    parts: list[str] = date_string.split('/')

    #make sure that there was a valid amount of parts like (d/m/y)
    if len(parts) == 3:
        #return each part in the form of dictionary
        return {
            'day': int(parts[0]),
            'month': int(parts[1]),
            'year': int(parts[2]),
        }
    else:
        raise ValueError(f'Invalid date string: {date_string}')

#Example usage
date: dict[str, int] = parse_date_european('24/10/25')
print(date)
