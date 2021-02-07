# TODO(pebaz): Table().add(Column1='asdf', Column2=3)
# TODO(pebaz): Table().add(Other1='asdf', Column2=3)  # Works with empty
# TODO(pebaz): This ensure that a header line is printed


class Table:
    def __init__(self, margin=1, sep='|', align='center'):
        assert align in {'center', 'ljust', 'rjust'}
        self.margin = margin
        self.sep = sep
        self.align = align
        self.rows = []
        self.col_lens = []
    
    def add(self, *cells) -> None:
        row = [str(i) for i in cells]

        if not self.rows:
            self.col_lens = [len(i) for i in row]

        self.rows.append(row)

        for i in range(max(len(self.col_lens), len(row))):
            if i >= len(row):
                break
            new_col_len = len(row[i])

            if i >= len(self.col_lens):
                self.col_lens.append(new_col_len)
            col_len = self.col_lens[i]

            if new_col_len > col_len:
                self.col_lens[i] = new_col_len
    
    def show(self) -> None:
        start = f'{self.sep}{" " * self.margin}'
        separator = f'{" " * self.margin}{start}'

        for row in self.rows:
            print(start, end='')
            for i, cell in enumerate(row):
                if i >= len(self.col_lens):
                    break
                col_len = self.col_lens[i]
                line = getattr(str(cell), self.align)(col_len)
                print(line, end=separator)
            print()
