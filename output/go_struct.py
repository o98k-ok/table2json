from .sink import Sink

class Field(object):
    def __init__(self, name, tpe, tags, doc) -> None:
        ## tags {"json":["id", "omitempty"]}
        self.name = name
        self.type = self.type_mapping(tpe)
        self.tags = tags
        self.doc = doc

    def type_mapping(self, tpe) -> str:
        typeMap = {
            "String": "string",
            "Integer": "int",
            "Float": "float32",
            "Double": "float32"
        }

        res_type = "interface{}"
        if tpe in typeMap:
            res_type = typeMap[tpe] 
        return res_type

    def merge_tags(self) -> str:
        res = []
        for key, tags in self.tags.items():
            one_tag = '{}:"{}"'.format(key, ",".join(tags))
            res.append(one_tag)
        return " ".join(res)
        
    def marshal(self) -> str:
        return "{} {} `{}` // {}".format(self.name, self.type, self.merge_tags(), self.doc)

    def __str__(self) -> str:
        return self.marshal()

class GolangStruct(object):
    def __init__(self, name, fields) -> None:
        self.name  =  name
        self.fields = fields

    def __str__(self) -> str:
        main = "\n".join(["\t" + i.marshal() for i in self.fields])
        return "type {} struct {{\n{}\n}}".format(self.name, main)


class GolangSink(Sink):
    def __init__(self, structs) -> None:
        super().__init__()
        self.structs = structs
    
    def set(self) -> str:
        return "\n\n".join([i.__str__() for i in self.structs])


if __name__ == "__main__":
    a = Field('id', 'String', {"json":["id"]}, '竞价请求⼴告位唯⼀标识，竞价系统提供')
    b = Field('id', 'String', {"json":["id"], "schma":["name", "optional"]}, '竞价请求⼴告位唯⼀标识，竞价系统提供')
    # print(GolangStruct("struct1", [a, b]))

    struct = GolangStruct("struct1", [a, b])
    print(GolangSink([struct, struct]).set())

