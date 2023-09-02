import os
import sys

from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet

from DataStructure import SchoolSystem
from PreProcess import init_dep, init_employee
from UI import MyMainWindow

# 设置路径及APPID
basedir = os.path.dirname(__file__)
try:
    from ctypes import windll

    myappid = 'Tongji.2151773霍家灏.DepartmentSystem'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

if __name__ == '__main__':
    # 初始化
    tongji_sys = SchoolSystem()
    dep_name2id = init_dep(tongji_sys)  # 部门初始化
    init_employee(tongji_sys, list(dep_name2id.values()))  # 人员初始化
    # 运行应用程序
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(basedir, '_sys.ico')))  # 设置ui图标
    demo = MyMainWindow(tongji_sys)
    apply_stylesheet(app, theme="dark_lightgreen.xml")
    demo.show()
    sys.exit(app.exec_())
