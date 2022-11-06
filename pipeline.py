from input.src import Src
from output.sink import Sink
from operation.operation import Operation

class Pipeline(object):
    def __init__(self, input_node:Src, output_node:Sink, *args:Operation) -> None:
        self.inpt = input_node
        self.outpt = output_node
        self.ops = args

    def run(self) -> None:
        info = self.inpt.get()
        for node in self.ops:
            info = node.do(info)
        self.outpt.sink(info)