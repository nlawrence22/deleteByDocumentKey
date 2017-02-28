from handler import Read_CSV
from handler import Delete_Duplicates

reader = Read_CSV()
handler = Delete_Duplicates()

items = reader.read()
handler.delete(items)


print "done"


