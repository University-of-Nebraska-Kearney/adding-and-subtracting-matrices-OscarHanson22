"""
NOTE on RANGES (closed, open-ended, open)
(start, end) -> any value | start <= value <= end
(None, end) -> any value <= end
(start, None) -> any value >= start
(None, None) -> any value
"""

def is_in_range(value, start, end):
    """ 
    Returns if the value is between start and end. 
    Start and end can be None to reflect different types of ranges. 
    """
    if start is None and end is None:
        return True
    if start is None and end is not None:
        return value <= end
    if end is None and start is not None:
        return value >= start
    return start <= value <= end

def range_string(start, end):
    """ 
    Returns a string representation of the range defined by start and end. 
    Start and end can be None to reflext different types of ranges.
    """
    if start is None and end is None:
        return ""
    if start is None and end is not None:
        return f"less than or equal to {end}"
    if end is None and start is not None:
        return f"greater than or equal to {start}"
    return f"between {start} and {end}"

def _user_input_number(cast, type_name, start, end):
    """ 
    Helper function used by user input functions. 
    Captures user input, casts it, optionally ensures it is in a range, and handles bad input.
    """
    if start is not None and end is not None and start > end:
        raise ValueError("Start value must be less than end value.")
    
    while True:
        response = input()
        try:
            response_number = cast(response)
            if is_in_range(response_number, start, end):
                return response_number
            else:
                print(f"Please choose {type_name} {range_string(start, end)}.")
        except ValueError:
            print(f"Please choose {type_name}.")

def user_input_int(start=None, end=None):
    """ Returns a user-given integer value in the range from start to end. """
    return _user_input_number(int, "an integer", start, end)

def user_input_float(start=None, end=None):
    """ Returns a user-given float value in the range from start to end. """
    return _user_input_number(float, "a value", start, end)