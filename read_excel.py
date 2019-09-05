import xlrd

def excel_to_list(data_file,sheet):
    data_list = [] #新建个空列表 来装数据
    wb = xlrd.open_workbook(data_file)
    sh = wb.sheet_by_name(sheet)
    title = sh.row(0)
    for i in  range(1,sh.nrows):
        d = dict(zip(title,sh.row(i)))
        data_list.append(d)
    return data_list  # 列表嵌套字典格式，每个元素是一个字典


def get_test_Data(data_list,test_case):
    for data_case in data_list:

        if test_case == data_case['case_name']:
            return test_case



if __name__ == "__main__":
    data_list = excel_to_list("test_coupon.xlsx","test_coupon_exited")
    print(data_list)
    test_case = get_test_Data(data_list,"test_coupon_exit")
    print(test_case)

