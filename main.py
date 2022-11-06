import input.pdf as src
import output.go_struct as sink
import operation.golang as golang
import pipeline

if __name__ == "__main__":
    filename = "testdata/main.pdf"
    inpt = src.PDFSrc(filename, [8, 9, 10, 11])
    outpt = sink.GolangSink()
    op = golang.Golang()

    pipe = pipeline.Pipeline(inpt, outpt, op)
    pipe.run()

