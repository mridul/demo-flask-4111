import os

from sqlalchemy import *

connection_string = os.getenv('connection_string')

engine = create_engine(connection_string)


def get_names():
    result_proxy = engine.execute("select * from public.temp")
    names = []
    # (id, name)
    for record in result_proxy.fetchall():
        names.append(record[1])

    return names
