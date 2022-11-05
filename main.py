import input.pdf as src
import output.go_struct as sink
import format.golang as golang

if __name__ == "__main__":
    filename = "testdata/main.pdf"
    inpt = src.PDFSrc(filename, [8, 9, 10, 11])
    info = inpt.get()
    outpt = sink.GolangSink(golang.format(info))
    print(outpt.set())