import csv
'''
CSV文件列名：商品编号，商品名称，划线价，销售价，税费，利润，高级会员，蓝钻会员，红钻会员。其中最后三列为推荐供应奖的三
个级别，红钻以上与红钻一致。
'''
Array = []
csv_file = csv.reader(open('changeprice.csv', 'r'))
for stu in csv_file:
    Array.append((stu[0], stu[2], stu[3], stu[4], stu[5], stu[6], stu[7], stu[8]))

commont_arr = []
csv_file1 = csv.reader(open('pinglun.csv', 'r'))
for stu in csv_file1:
    commont_arr.append((stu[0], stu[1], stu[2]))


off_sale = []
on_sale = []
suppliy_price = []
Honsale = []
csv_file2 = csv.reader(open('change.csv', 'r'))
for stu in csv_file2:
    if stu[0] != "":
        off_sale.append(stu[0])
    if stu[1] != "":
        on_sale.append((stu[1], stu[2], stu[3], stu[4], stu[5]))
        suppliy_price.append((stu[1], stu[6], stu[7], stu[8]))
    if stu[9] != "":
        Honsale.append((stu[9], stu[10], stu[11], stu[12]))


hoshii = []
csv_file3 = csv.reader(open('hoshii.csv', 'r'))
for stu in csv_file3:
    hoshii.append((stu[0], stu[1], stu[2]))