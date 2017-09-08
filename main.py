'''
TODO
浏览器不重启
模块文档
跨平台
封装函数，私密的函数前面加_
多线程 一个浏览器 一个下载器
按一个键保存序号，就像有道划词
pdf
浏览器废弃的代码

gui
    PyQt4 wxPython PyGOvject Pyside PyGTK


'''

from driver import net
from Loadder import lod

num = '600519'

net.get_rep_info(num)
lod.load()

print("Sucessful")

from db.DAO import report
set = report.unloaded_reps()
for row in set:
    print(row)



if __name__ == '__main__':
    pass



