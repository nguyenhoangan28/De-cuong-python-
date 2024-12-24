class Book:
    def __init__(self):
        self.name = ""
        self.page = 0
        self.cost = 0

    def nhap(self):
        self.name = input()
        self.page = int(input())
        self.cost = int(input())

    def xuat(self):
        return f"{self.name}\n{self.page}\n{self.cost}"


n = int(input())
books = []
for i in range(n):
    print(f"Nhap thong sach thu {i+1}:")
    book = Book()
    book.nhap()
    books.append(book)

with open("sach.txt", "w", encoding="utf-8") as f:
    for book in books:
        f.write(book.xuat() + "\n")

bookss = []
with open("sach.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        name = lines[i].strip()
        page = int(lines[i + 1].strip())
        cost = int(lines[i + 2].strip())
        bookss.append(Book(name, page, cost))

loc = []
for book in bookss:
    if book.cost > 100000 and book.page < 200:
        loc.append(book)

with open("ketqua.txt", "w", encoding="utf-8") as file:
    file.write("Danh sách các quyển sách có giá > 100.000 và số trang < 200\n")
    for book in loc:
        file.write(book.xuat() + "\n")
