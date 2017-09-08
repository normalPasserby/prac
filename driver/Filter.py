


# filte elem and change report name and url

# # remove bad elem
# def get_valid_elem(elems):
#     def contain(text):
#         words = ['摘要', '取消']
#         for word in words:
#             if word in text:
#                 return True
#         return False
#
#     new = []
#     for elem in elems:
#         if contain(elem.getText()):
#             continue
#         new.append(elem)
#     return new



import re
#
def get_true_load_url(partical_url):
    regex = re.compile(r'(\d){4,10}')
    mo1 = regex.search(partical_url)
    regex = re.compile(r'(\d){4}-\d\d-\d\d')
    mo2 = regex.search(partical_url)
    root_url = 'http://www.cninfo.com.cn'
    load_url = '/cninfo-new/disclosure/szse_main/download/' + mo1.group() + '?announceTime=' + mo2.group()
    url = root_url + load_url
    return url

# xxxx20xx年度报告
def get_formal_name(filename, stock_name):
    regex = re.compile(r'20\d\d.*')
    name = regex.search(filename)
    return stock_name + name.group()
