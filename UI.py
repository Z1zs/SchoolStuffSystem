from typing import List

from PyQt5.QtCore import pyqtProperty, Qt
from PyQt5.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem, QTableWidget, QVBoxLayout, \
    QHBoxLayout, QDialog, QDialogButtonBox, QLineEdit, QFrame, QPushButton, QMessageBox, QMainWindow, QAction, \
    QGridLayout, QComboBox, QLabel, QCheckBox

from DataStructure import Department, PrivateMessage, Employee, SchoolSystem


def my_qlabel(s: str):
    s = s.center(len(s) + 10)
    lb = QLabel(s)
    lb.setAlignment(Qt.AlignCenter)
    return lb


# 显示多个候选职工对话框
class ShowSearchDlg(QDialog):
    def __init__(self, emp_list: List[Employee], parent):
        super().__init__()
        self._parent = parent
        self.emp_list = emp_list
        self.show_emp_dlg = None
        self.setWindowTitle("搜索结果")
        # 图形组件
        self.lb = QLabel("找到以下符合条件的职工,点击右侧按钮查看详情:")

        self.table = QTableWidget()
        self.table.setRowCount(len(self.emp_list))
        self.table.setColumnCount(4)
        for row, emp in enumerate(self.emp_list):
            self.table.setCellWidget(row, 0, my_qlabel(emp.name))
            self.table.setCellWidget(row, 1, my_qlabel(emp.info.info["性别"]))
            self.table.setCellWidget(row, 2, my_qlabel(emp.employee_id))
            self.table.setCellWidget(row, 3, my_qlabel("查看详情"))
        self.table.resizeRowsToContents()
        self.table.resizeColumnsToContents()
        self.table.cellClicked.connect(self.show_emp)

        # 按钮
        q_btn = QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(q_btn)
        self.buttonBox.rejected.connect(self.close)

        # 整体布局
        self._layout = QVBoxLayout()
        self._layout.addWidget(self.lb)
        self._layout.addWidget(self.table)
        self._layout.addWidget(self.buttonBox)
        self.setLayout(self._layout)
        self.setMinimumSize(600, 500)

    def show_emp(self, row, col):
        if col != 3:
            return None
        emp = self.emp_list[row]
        self.show_emp_dlg = EmpInfoPage(emp, self._parent)
        self.show_emp_dlg.exec()
        return None


# 展示职工信息对话框
class EmpInfoPage(QDialog):
    def __init__(self, emp: Employee, _parent):
        # 初始化
        super().__init__()
        self.emp = emp
        self._parent = _parent
        self.setWindowTitle("职工资料")
        # 资料索引
        self.header = ["姓名"]
        for key in Employee("0", "0").info.info.keys():
            if key != "学历":
                self.header.append(key)
        # 个人信息页
        self.up_layout = QGridLayout()
        for row, key in enumerate(self.header):
            self.up_layout.addWidget(QLabel(key), row, 0)
            if key == "姓名":
                lb = QLabel(self.emp.name)
                lb.setTextInteractionFlags(Qt.TextSelectableByMouse)
                self.up_layout.addWidget(lb, row, 1)
            else:
                lb = QLabel(str(self.emp.info.info[key]))
                lb.setTextInteractionFlags(Qt.TextSelectableByMouse)
                self.up_layout.addWidget(lb, row, 1)

        # 职位一览
        # 初始化
        tb_row = len(self.emp.title_dict.keys())
        tb_col = 3
        self.down_table = QTableWidget()
        self.down_table.setRowCount(tb_row)
        self.down_table.setColumnCount(tb_col)
        self.down_table.setHorizontalHeaderLabels(["部门编号", "部门名称", "职位"])
        # 添加职位到表格
        row = 0
        for dep_id in self.emp.title_dict.keys():
            flag, dep = self._parent.sys.get_dep(dep_id)
            if flag:
                self.down_table.setCellWidget(row, 0, my_qlabel(dep_id))
                self.down_table.setCellWidget(row, 1, my_qlabel(dep.name))
                self.down_table.setCellWidget(row, 2, my_qlabel(self.emp.title_dict[dep_id]))
                row += 1
        self.down_table.resizeColumnsToContents()
        self.down_table.resizeRowsToContents()

        # 按钮
        q_btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(q_btn)
        self.buttonBox.accepted.connect(self.close)
        self.buttonBox.rejected.connect(self.close)

        # 调整布局
        self._layout = QVBoxLayout()
        lb = QLabel("个人信息")
        lb.setFrameStyle(QFrame.Panel)
        self._layout.addWidget(lb)
        self._layout.addLayout(self.up_layout)

        self._layout.addWidget(self.down_table)
        self._layout.addWidget(self.buttonBox)
        self.setLayout(self._layout)
        self.setMinimumSize(800, 500)


# 删除部门对话框
class LeaveDepPage(QDialog):
    def __init__(self, _parent):
        # 初始化
        super().__init__()
        self._parent = _parent
        self.setWindowTitle("调离部门")
        self.label = QLabel("确定要将该员工调离当前部门吗？")
        self.ckbox = QCheckBox("同时将其调离所有下级部门")
        # 选项按钮
        q_btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(q_btn)
        self.buttonBox.accepted.connect(self._accept)
        self.buttonBox.rejected.connect(self.reject)
        # 设置布局
        self._layout = QVBoxLayout()
        self._layout.addWidget(self.label)
        self._layout.addWidget(self.ckbox)
        self._layout.addWidget(self.buttonBox)
        self.setLayout(self._layout)

    def _accept(self):
        # 将职工调离该部门
        if self.ckbox.checkState() == Qt.Unchecked:
            self._parent.sys.leave_dep_by_id(self._parent.selected_emp, self._parent.selected_dep)
        else:  # 同时调离下级部门
            self._parent.sys.leave_dep_totally_by_id(self._parent.selected_emp, self._parent.selected_dep)
        self.close()


# 删除职工对话框
class DelEmpPage(QDialog):
    def __init__(self, _parent):
        # 初始化
        super().__init__()
        self._parent = _parent
        self.setWindowTitle("解雇员工")
        self.label = QLabel("确定要将该员工从系统中删除吗？")
        # 选项按钮
        q_btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(q_btn)
        self.buttonBox.accepted.connect(self._accept)
        self.buttonBox.rejected.connect(self.reject)
        # 设置布局
        self._layout = QVBoxLayout()
        self._layout.addWidget(self.label)
        self._layout.addWidget(self.buttonBox)
        self.setLayout(self._layout)

    def _accept(self):
        self._parent.sys.remove_employee(self._parent.selected_emp)
        self.close()


# 编辑职工信息对话框
class EditEmpPage(QDialog):
    def __init__(self, _parent, old_info: str = None):
        # 初始化
        super().__init__()
        self._parent = _parent
        self.setWindowTitle("修改职工资料")
        self.key = self._parent.selected_emp_info  # 明确要修改的栏目
        # 组件
        if self.key == "职位":
            self.label = QLabel("请选择正确的" + self.key)
            self.editor = QComboBox()
            self.editor.addItems(["主管", "副主管", "员工"])
        elif self.key == "性别":
            self.label = QLabel("请选择正确的" + self.key)
            self.editor = QComboBox()
            self.editor.addItems(["男", "女"])
        else:
            self.label = QLabel("请输入正确的" + self.key)
            self.editor = QLineEdit(old_info.strip())
        # 选项按钮
        q_btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(q_btn)
        self.buttonBox.accepted.connect(self._accept)
        self.buttonBox.rejected.connect(self.reject)
        # 设置布局
        self._layout = QVBoxLayout()
        self._layout.addWidget(self.label)
        self._layout.addWidget(self.editor)
        self._layout.addWidget(self.buttonBox)
        self.setLayout(self._layout)
        self.setMinimumSize(500, 50)

    def _accept(self):
        emp = self._parent.sys.get_employee(self._parent.selected_emp)  # 获取选中的职工
        if self.key == "性别":
            emp.info.info[self.key] = self.editor.currentText()
        elif self.key == "职位":
            # 先免职再任职
            self._parent.sys.dismiss_title_by_id(self._parent.selected_emp, self._parent.selected_dep)
            self._parent.sys.set_title_by_id(self._parent.selected_emp, self._parent.selected_dep,
                                             self.editor.currentText())
        else:
            emp.info.info[self.key] = self.editor.text()
        self.close()


# 添加新职工对话框
class AddEmpPage(QDialog):
    def __init__(self, _parent):
        super().__init__()
        self._parent = _parent
        self.setWindowTitle("添加职工资料")
        # 资料索引
        self.header = ["姓名", "职位"]
        for key in Employee("0", "0").info.info.keys():
            if key != "学历":
                self.header.append(key)
        self.info = {}
        self._layout = QGridLayout()
        self.initUI()
        # 选项按钮
        q_btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(q_btn)
        self.buttonBox.accepted.connect(self._accept)
        self.buttonBox.rejected.connect(self.reject)
        # 整体布局
        self.vlayout = QVBoxLayout()
        self.vlayout.addLayout(self._layout)
        self.vlayout.addWidget(self.buttonBox)
        self.setLayout(self.vlayout)

    def initUI(self):
        # 添加各栏
        for row, key in enumerate(self.header):
            label = QLabel(str(key))
            if key == "性别":
                editor = QComboBox()
                editor.addItems(["男", "女"])
            elif key == "职位":
                editor = QComboBox()
                editor.addItems(["主管", "副主管", "员工"])
            else:
                editor = QLineEdit("")
                editor.setPlaceholderText("请输入" + key + "...")
            self.info[key] = editor
            self._layout.addWidget(label, row, 0)
            self._layout.addWidget(editor, row, 1)

    def _accept(self):
        # 错误处理
        if self.info["姓名"].text() is None or self.info["姓名"].text() == "":
            wrong_dialog = QMessageBox(self)
            wrong_dialog.setWindowTitle("Warning")
            wrong_dialog.setText("姓名不能为空")
            wrong_dialog.exec()
            return False
        if self.info["身份证号"].text() is None or self.info["身份证号"].text() == "":
            wrong_dialog = QMessageBox(self)
            wrong_dialog.setWindowTitle("Warning")
            wrong_dialog.setText("身份证号不能为空")
            wrong_dialog.exec()
            return False
        s = self.info["身份证号"].text()
        if not s.isdigit() or len(s) != 18:
            wrong_dialog = QMessageBox(self)
            wrong_dialog.setWindowTitle("Warning")
            wrong_dialog.setText("身份证号格式错误")
            wrong_dialog.exec()
            return False
        # 创建职工
        emp = Employee(self.info["姓名"].text(), self.info["身份证号"].text())
        for key in self.header:
            if key in emp.info.info:
                if key != "职位" and key != "性别":
                    emp.info.info[key] = self.info[key].text()
                else:
                    emp.info.info[key] = self.info[key].currentText()
        # 添加职工
        self._parent.sys.add_employee_by_dep_id(emp, self._parent.selected_dep)
        self._parent.sys.set_title_by_id(emp.employee_id, self._parent.selected_dep, self.info["职位"].currentText())
        self.close()


# 添加新部门对话框
class AddDepDialog(QDialog):
    def __init__(self, _parent: Department, sys: SchoolSystem):
        super().__init__()
        self._parent = _parent
        self._sys = sys
        self.setWindowTitle("插入子部门")

        q_btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(q_btn)
        self.buttonBox.accepted.connect(self._accept)
        self.buttonBox.rejected.connect(self.reject)

        self.message = QLabel("请输入子部门名称(系统自动编号):")
        self.nameedit = QLineEdit()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.message)
        self.layout.addWidget(self.nameedit)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def _accept(self):
        if self.nameedit.text() is not None:
            flag = self._sys.add_dep(self._parent, self.nameedit.text())
            if not flag:
                wrong_dialog = QMessageBox(self)
                wrong_dialog.setWindowTitle("Warning")
                wrong_dialog.setText("插入失败！")
                wrong_dialog.exec()
                return False
            self.close()
        else:
            wrong_dialog = QMessageBox(self)
            wrong_dialog.setWindowTitle("Warning")
            wrong_dialog.setText("名称不能为空！")
            wrong_dialog.exec()
            return False


# 部门列表组件
class DepTreeItem(QWidget):
    def __init__(self, root_dep: Department):
        # 数据成员
        super().__init__()
        self.root_dep = root_dep
        self.id2dep = {}
        # 图形组件
        self.tree = QTreeWidget(self)
        self.tree.setHeaderLabels(["部门列表"])
        self.root_item = QTreeWidgetItem(self.tree)
        self.root_item.setText(0, self.root_dep.name)
        self.id2dep[root_dep.dep_id] = self.root_item
        self.tree.setMinimumSize(500, 500)
        # 添加所有部门
        self.init_dep(self.root_dep, self.root_item)
        # 添加和删除键
        self.add_btn = QPushButton("插入子部门")
        self.del_btn = QPushButton("删除该部门")
        # 设置布局
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tree)
        self.layout.addWidget(self.add_btn)
        self.layout.addWidget(self.del_btn)
        self.setLayout(self.layout)

    # 将root_dep设置为property，便于更新
    def myroot_dep(self):
        return self.root_dep

    def set_myroot_dep(self, new_root_dep):
        self.root_dep = new_root_dep
        self.update()

    myroot_dep = pyqtProperty(int, myroot_dep, set_myroot_dep)

    # 层序遍历添加所有部门
    def init_dep(self, dep: Department, item: QTreeWidgetItem):
        for child_dep in dep.child_list:
            child_item = QTreeWidgetItem(item)
            child_item.setText(0, child_dep.name)
            child_item.setToolTip(0, child_dep.name)
            self.id2dep[child_dep.dep_id] = child_item
            self.init_dep(child_dep, child_item)

    # 更新传入部门的子部门
    def dep_update(self, dep: Department):
        for child_dep in dep.child_list:
            if child_dep.dep_id not in self.id2dep:
                item = self.id2dep[dep.dep_id]
                child_item = QTreeWidgetItem(item)
                child_item.setText(0, child_dep.name)
                child_item.setToolTip(0, child_dep.name)
                self.id2dep[child_dep.dep_id] = child_item

    # 删除部门
    def dep_remove(self, dep_id):
        item = self.id2dep[dep_id]
        parent = item.parent()
        parent.removeChild(item)


# 职员列表组件
class EmployeeListItem(QWidget):
    def __init__(self, dep_id: str, employee_list: List[Employee]):
        # 数据成员
        super().__init__()
        self.data = employee_list
        self.id2btn = {}
        self.dep_id = dep_id
        # 各列名称
        tmp = PrivateMessage()
        self.header = ["姓名", "工号", "职位"]
        for key in tmp.info.keys():
            if key != "学历" and key != "其他":
                self.header.append(key)
        # 创建QTable
        self.table = QTableWidget()
        self.table.setRowCount(len(self.data))
        self.table.setColumnCount(len(self.header))
        if len(self.data) > 0:
            self.setData()
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        # 显示图形页面
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

    # 设置数据
    def setData(self):
        # 添加数据
        for row, emp in enumerate(self.data):
            if emp is not None:
                for col, key in enumerate(self.header):
                    if key == "姓名":
                        self.table.setCellWidget(row, col, my_qlabel(emp.name))
                    elif key == "工号":
                        self.table.setCellWidget(row, col, my_qlabel(emp.employee_id))
                    elif key == "职位":
                        if self.dep_id in emp.title_dict:
                            self.table.setCellWidget(row, col, my_qlabel(emp.title_dict[self.dep_id]))
                        else:
                            self.table.setCellWidget(row, col, my_qlabel("None"))
                    else:
                        self.table.setCellWidget(row, col, my_qlabel(str(emp.info.info[key])))
                # self.table.setCellWidget(row, len(self.header), QPushButton("查看/编辑"))
                self.id2btn[emp.employee_id] = row
        self.table.move(0, 0)
        # 设置列标题
        self.table.setHorizontalHeaderLabels(self.header)

    # 更新数据
    def myupdate(self, dep_id: str, employee_list: List[Employee]):
        self.table.clear()

        self.data = employee_list
        self.dep_id = dep_id
        self.id2btn = {}

        self.table.setRowCount(len(self.data))
        self.table.setColumnCount(len(self.header))

        for row, emp in enumerate(self.data):
            if emp is not None:
                for col, key in enumerate(self.header):
                    if key == "姓名":
                        self.table.setCellWidget(row, col, my_qlabel(emp.name))
                    elif key == "工号":
                        self.table.setCellWidget(row, col, my_qlabel(emp.employee_id))
                    elif key == "职位":
                        if self.dep_id in emp.title_dict:
                            self.table.setCellWidget(row, col, my_qlabel(emp.title_dict[self.dep_id]))
                        else:
                            self.table.setCellWidget(row, col, my_qlabel("None"))
                    else:
                        self.table.setCellWidget(row, col, my_qlabel(str(emp.info.info[key])))
                # self.table.setCellWidget(row, len(self.header), QPushButton("查看/编辑"))
                self.id2btn[emp.employee_id] = row
        self.table.move(0, 0)
        # 设置列标题
        self.table.setHorizontalHeaderLabels(self.header)


# 显示部门简要信息
class DepInfoItem(QWidget):
    def __init__(self, dep: Department):
        # 初始化
        super().__init__()
        self.data = {"部门名称": dep.name, "部门编号": dep.dep_id, "部门主管ID": dep.manager_id}
        self.item_dict = {}
        self._layout = QHBoxLayout()
        for k in self.data.keys():
            self._layout.addWidget(QLabel(k))
            lb = QLabel(self.data[k])
            lb.setFrameStyle(QFrame.Box)
            lb.setTextInteractionFlags(Qt.TextSelectableByMouse)
            self._layout.addWidget(lb)
            self.item_dict[k] = lb

        self.setLayout(self._layout)

    # 信息更新
    def myupdate(self, new_dep: Department):
        self.data = {"部门名称": new_dep.name, "部门编号": new_dep.dep_id, "部门主管ID": new_dep.manager_id}
        self.item_dict["部门名称"].setText(new_dep.name)
        self.item_dict["部门编号"].setText(new_dep.dep_id)
        self.item_dict["部门主管ID"].setText(new_dep.manager_id)


# 主程序窗口
class MyMainWindow(QMainWindow):
    # 初始化
    def __init__(self, tongji_sys: SchoolSystem):
        # 数据成员
        super(MyMainWindow, self).__init__()
        self.sys = tongji_sys
        self.selected_dep = self.sys.root_dep.dep_id
        self.selected_emp = None
        self.selected_emp_info = None
        self.old_emp_info = None
        self.show_child_flag = False
        # 对话组件(先初始化为空防报错)
        self.add_dep_dlg = None
        self.add_emp_dlg = None
        self.del_emp_dlg = None
        self.leave_dep_dlg = None
        self.edit_emp_dlg = None
        self.show_emp_dlg = None
        self.show_search_dlg = None
        # 图形组件
        self.query = QLineEdit()
        self.query.setPlaceholderText("输入要查找的职工姓名或工号...")
        self.query_btn = QPushButton("查找")

        self.dep_dir = DepTreeItem(self.sys.root_dep)
        self.dep_dir.add_btn.clicked.connect(self.add_child_dep)
        self.dep_dir.del_btn.clicked.connect(self.delete_dep)
        self.dep_table = DepInfoItem(self.sys.root_dep)

        self.emp_table = EmployeeListItem(self.selected_dep, self.sys.get_emp_list_by_id(self.selected_dep))
        # 整体布局
        self.uup_layout = QHBoxLayout()
        self.uup_layout.addWidget(self.query, 9)
        self.uup_layout.addWidget(self.query_btn, 1)

        self.up_layout = QHBoxLayout()
        self.up_layout.addWidget(self.dep_dir, 1)
        self.up_layout.addWidget(self.emp_table, 5)

        self._layout = QVBoxLayout()
        self._layout.addLayout(self.uup_layout)
        self._layout.addLayout(self.up_layout)
        self._layout.addWidget(self.dep_table)
        # 不能直接使用setLayout方法，需要组件居中
        self.central_widget = QWidget()
        self.central_widget.setLayout(self._layout)
        self.setCentralWidget(self.central_widget)
        self.setMinimumSize(2200, 1200)
        # 加载菜单
        self._load_menu()
        # 信号和槽（显示部门职工）
        self.query_btn.clicked.connect(self.search_emp)
        self.dep_dir.tree.itemClicked.connect(self.show_selected_dep)
        self.emp_table.table.cellClicked.connect(self.get_selected_emp)
        self.emp_table.table.cellDoubleClicked.connect(self.edit_emp)

    # 加载菜单
    def _load_menu(self):
        menu = self.menuBar()

        edit_menu = menu.addMenu("人事调动")
        add_emp_action = QAction("添加职员", self)
        add_emp_action.setStatusTip("将新员工或其他部门员工添加至该部门")
        add_emp_action.triggered.connect(self.add_emp)
        edit_menu.addAction(add_emp_action)

        leave_emp_action = QAction("调离部门", self)
        leave_emp_action.setStatusTip("将员工调离该部门")
        leave_emp_action.triggered.connect(self.leave_dep)
        edit_menu.addAction(leave_emp_action)

        del_emp_action = QAction("解雇职员", self)
        del_emp_action.setStatusTip("将员工从系统中删除")
        del_emp_action.triggered.connect(self.del_emp)
        edit_menu.addAction(del_emp_action)

        other_menu = menu.addMenu("其他")
        self.show_child_action = QAction("完全显示", self)
        self.show_child_action.setStatusTip("同时显示下级部门职工")
        self.show_child_action.setCheckable(True)
        self.show_child_action.triggered.connect(self.set_flag)
        other_menu.addAction(self.show_child_action)

    # 为当前选中部门添加子部门
    def add_child_dep(self):
        if self.selected_dep == "0.1":
            wrong_dialog = QMessageBox(self)
            wrong_dialog.setWindowTitle("Warning")
            wrong_dialog.setText("该部门不能被操作！")
            wrong_dialog.exec()
            return False
        flag, dep = self.sys.get_dep(self.selected_dep)
        if not flag:
            return False
        # 将部门插入数据成员中
        self.add_dep_dlg = AddDepDialog(dep, self.sys)
        self.add_dep_dlg.exec()
        # 更新dep_dir
        self.dep_dir.dep_update(dep)

    # 删除当前选中部门
    def delete_dep(self):
        if self.selected_dep == "0.1":
            wrong_dialog = QMessageBox(self)
            wrong_dialog.setWindowTitle("Warning")
            wrong_dialog.setText("该部门不能被操作！")
            wrong_dialog.exec()
            return False
        self.sys.remove_dep_by_id(self.selected_dep)
        self.dep_dir.dep_remove(self.selected_dep)
        self.selected_dep = self.sys.root_dep.dep_id

    # 为当前选中部门添加新职员
    def add_emp(self):
        if self.selected_dep == "0.1":
            wrong_dialog = QMessageBox(self)
            wrong_dialog.setWindowTitle("Warning")
            wrong_dialog.setText("该部门不能被操作！")
            wrong_dialog.exec()
            return False
        # 获取当前部门
        flag, dep = self.sys.get_dep(self.selected_dep)
        if not flag:
            return False
        # 对话框获取新职员信息
        self.add_emp_dlg = AddEmpPage(self)
        self.add_emp_dlg.exec()
        self.show_emp_table()

    # 查找职工
    def search_emp(self):
        # 显示搜索结果，只能查看不能编辑
        if self.query.text().isdigit():  # 按工号查找
            emp = self.sys.get_employee(self.query.text())
            if emp is None:  # 未找到
                wrong_dialog = QMessageBox(self)
                wrong_dialog.setWindowTitle("Warning")
                wrong_dialog.setText("没有找到符合条件的员工！")
                wrong_dialog.exec()
                return None
            self.show_emp_dlg = EmpInfoPage(emp, self)
            self.show_emp_dlg.exec()
            return None

        else:  # 按姓名查找，可能有多个重名的，返回列表
            emp_list = self.sys.search_emp_by_name(self.query.text())
            if len(emp_list) == 0:  # 未找到
                wrong_dialog = QMessageBox(self)
                wrong_dialog.setWindowTitle("Warning")
                wrong_dialog.setText("没有找到符合条件的员工！")
                wrong_dialog.exec()
                return None
            elif len(emp_list) == 1:  # 只找到一个，直接显示
                self.show_emp_dlg = EmpInfoPage(emp_list[0], self)
                self.show_emp_dlg.exec()
                return None
            else:  # 找到多个，显示全部候选项供查看
                self.show_search_dlg = ShowSearchDlg(emp_list, self)
                self.show_search_dlg.exec()

    # 删除当前选中职员
    def del_emp(self):
        # 判断
        if self.selected_emp is None:
            wrong_dialog = QMessageBox(self)
            wrong_dialog.setWindowTitle("Warning")
            wrong_dialog.setText("请先选中要删除的职工！")
            wrong_dialog.exec()
            return None
        self.del_emp_dlg = DelEmpPage(self)
        self.del_emp_dlg.exec()
        self.show_emp_table()
        # 重置选中职员
        self.selected_emp_info = None
        self.selected_emp = None

    # 将选中职员调离当前部门
    def leave_dep(self):
        if self.selected_dep == "0.1":
            wrong_dialog = QMessageBox(self)
            wrong_dialog.setWindowTitle("Warning")
            wrong_dialog.setText("该部门不能被操作！")
            wrong_dialog.exec()
            return False
        # 判断
        if self.selected_emp is None:
            wrong_dialog = QMessageBox(self)
            wrong_dialog.setWindowTitle("Warning")
            wrong_dialog.setText("请先选中要删除的职工！")
            wrong_dialog.exec()
            return None
        # 离职
        self.leave_dep_dlg = LeaveDepPage(self)
        self.leave_dep_dlg.exec()
        self.show_emp_table()

    # 更新选中部门信息栏
    def show_selected_dep(self, item):
        # 从item找出对应部门
        for dep_id in self.dep_dir.id2dep.keys():
            if self.dep_dir.id2dep[dep_id] == item:
                self.selected_dep = dep_id
                self.show_emp_table()
                # 重置选中职员
                self.selected_emp = None
                self.selected_emp_info = None
                flag, dep = self.sys.get_dep(self.selected_dep)
                if flag:
                    self.dep_table.myupdate(dep)
                return None

    # 更新选中职员
    def get_selected_emp(self, row, col):
        self.old_emp_info = self.emp_table.table.cellWidget(row, col).text().strip()
        self.selected_emp = self.emp_table.table.cellWidget(row, 1).text().strip()
        self.selected_emp_info = self.emp_table.header[col]

    # 编辑职员信息/职位
    def edit_emp(self):
        # 要修改的职员id和信息项已经存放在selected_emp和selected_emp_info中
        if self.selected_emp_info == "工号" or self.selected_emp_info == "身份证号":
            wrong_dialog = QMessageBox(self)
            wrong_dialog.setWindowTitle("Warning")
            wrong_dialog.setText("身份证号/工号暂不支持修改,信息现为\n" + self.old_emp_info + "\n")
            wrong_dialog.setTextInteractionFlags(Qt.TextSelectableByMouse)
            wrong_dialog.exec()
            return False
        # 对话框修改相应职员信息
        self.edit_emp_dlg = EditEmpPage(self, self.old_emp_info)
        self.edit_emp_dlg.exec()
        self.show_emp_table()

    # 更新职工列表
    def show_emp_table(self):
        # 刷新一下当前部门的职工列表
        if self.show_child_flag:
            self.emp_table.myupdate(self.selected_dep, self.sys.get_all_emp_list(self.selected_dep))
        else:
            self.emp_table.myupdate(self.selected_dep, self.sys.get_emp_list_by_id(self.selected_dep))

    # 是否显示下级部门的职工
    def set_flag(self):
        # 判断当前部门
        if self.selected_dep == "0.1":
            wrong_dialog = QMessageBox(self)
            wrong_dialog.setWindowTitle("Warning")
            wrong_dialog.setText("该部门不能被操作！")
            wrong_dialog.exec()
            return False
        if not self.show_child_flag:
            # 警告信息
            warning_dlg = QMessageBox(self)
            warning_dlg.setText("该操作会将所有下级部门职员加入列表，\n可能出现卡顿，确定要继续吗？")
            yes_btn = warning_dlg.addButton("Yes,continue", QMessageBox.ActionRole)
            warning_dlg.addButton(QMessageBox.Abort)
            warning_dlg.exec()

            if warning_dlg.clickedButton() == yes_btn:  # 继续操作
                self.show_child_flag = ~self.show_child_flag
                self.show_emp_table()
            else:  # 取消操作
                self.show_child_action.setChecked(False)
                return None
        else:  # 恢复
            self.show_child_flag = ~self.show_child_flag
            self.show_emp_table()
