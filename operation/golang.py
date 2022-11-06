from output.go_struct import *
from .operation import Operation


class Golang(Operation):
    def __init__(self) -> None:
        pass

    def do(self, tables:list[list]) -> list[GolangStruct]:
        return format(tables)

def format(tables) -> list[GolangStruct]:
    res = []
    for i in range(len(tables)):
        name = "CustomStruct{}".format(i)

        fields = []
        for row in tables[i]:
            fields.append(gen_field(row))

        if len(fields) == 0:
            continue

        res.append(GolangStruct(name, fields))
    return res


def underline_to_camel(underline_format):
    camel_format = ''
    if isinstance(underline_format, str):
        for _s_ in underline_format.split('_'):
            camel_format += _s_.capitalize()
    return camel_format

def gen_field(row) -> Field:
    field_name = underline_to_camel(row[0])
    if row[2] != "是":
        tags = {"json":[row[0], "omitempty"]}
    else:
        tags = {"json":[row[0]]}
    return Field(field_name, row[1], tags, row[3])