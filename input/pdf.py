import pdfplumber
import prettytable as pt
from .src import Src

class PDFSrc(Src):
    def __init__(self, filename, pages_id, fields_count=4):
        super().__init__()
        self.filename = filename
        self.pages_id = pages_id
        self.fields_count = fields_count

    def get(self) -> str:
        return extract_tables_from(self.filename, self.pages_id, self.fields_count)


def _deblank(fields):
    res = []
    for f in fields:
        res.append(f.replace('\n', ""))
    return res

def _deblank_for(table):
    res = []
    for row in table:
        row = _deblank(row)
        res.append(row)
    return res


def _create_prettytable(table, table_titles=[]):
    tb = pt.PrettyTable()
    if len(table_titles) != 0:
        tb.title = table_titles

    for row in table:
       tb.add_row(row)
    return tb

def extract_tables_from(file_name, pages_id, fields_count, test_mode=False):
    """extract tables info from pdf file

    Args:
        file_name (str): pdf file path
        pages_id (list[int]): page ids which contains table
        fields_count (int): table will be ignore if table column less than fields_count
        test_mode (bool): which test mode

    Returns:
        ([[str]]): tables which contains by pages_id
    """
    res = []
    pdf = pdfplumber.open(file_name)
    for i in pages_id:
        page = pdf.pages[i-1]
        tables = page.extract_tables()
        for table in tables:
            # judge suitable table format
            if len(table) == 0 or len(table[0]) < fields_count:
                continue
            
            table = _deblank_for(table)
            if test_mode:
                print(_create_prettytable(table))
        res.append(table)
    return res
                

if __name__ == "__main__":
    extract_tables_from('main.pdf', [11], 4, True)