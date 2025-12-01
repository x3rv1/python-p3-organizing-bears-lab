# Select all female bears, return name and age
select_all_female_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE sex = 'F';
"""

# Select all bears’ names in alphabetical order
select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT
        name
    FROM bears
    ORDER BY name ASC;
"""

# Select all alive bears’ names and ages, ordered youngest to oldest
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT
        name,
        age
    FROM bears
    WHERE alive = 1
    ORDER BY age ASC;
"""

# Select the oldest bear, return name and age
select_oldest_bear_and_returns_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    ORDER BY age DESC
    LIMIT 1;
"""

# Select the youngest bear, return name and age
select_youngest_bear_and_returns_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    ORDER BY age ASC
    LIMIT 1;
"""