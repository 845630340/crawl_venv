# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#
#     w = QWidget()
#     w.resize(250, 150)
#     w.move(300, 300)
#     w.setWindowTitle('Simple')
#     w.show()
#
#     sys.exit(app.exec_())

import csv

list1 = [[1, 2, 3], 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
rows = zip(list1, list2)

with open('some.csv', "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
print('finishing the csv file...')
