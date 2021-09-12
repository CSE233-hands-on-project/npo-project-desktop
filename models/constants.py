from . import dbconnection as db


def get_color(name): return "#" + db.submit_query("SELECT hexval FROM colors WHERE name = %s", (name, ))[0][0]


def get_prompt(name): return db.submit_query("SELECT value FROM prompts WHERE name = %s", (name, ))[0][0]


def get_error(name): return db.submit_query("SELECT description FROM errors WHERE name = %s", (name, ))[0][0]


def get_font(name):
    return str(db.submit_query(
        "SELECT fontname FROM fonts WHERE name = %s", (name, )
    )[0][0]) + " " + str(db.submit_query(
        "SELECT fontsize FROM fonts WHERE name = %s", (name, )
    )[0][0])

# TODO: Implement integration with localization where "name" gets translated values instead of defaults
