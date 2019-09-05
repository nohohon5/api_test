import xlrd

wb = xlrd.open_workbook("test_coupon.xlsx")
sh = wb.sheet_by_name("test_coupon_exited") #按工作簿定位工作表
print(sh.nrows)
print(sh.ncols)
print(sh.cell(0,0).value)
print(sh.row(0))
# 将数据和标题组装成字典，使数据更清晰
print(dict(zip(sh.row(0),sh.row(1))))
# 遍历excel,打印所有的数据
for i in range(sh.nrows):
    print(sh.row(i))
