from typing import Dict

Title = ["主管", "副主管", "员工"]


class PrivateMessage:
    def __init__(self):
        self.edu_dict = {"学士": None, "硕士": None, "博士": None}
        self.info = {"年龄": None, "性别": None, "手机号": None, "邮箱": None, "身份证号": None, "学历": self.edu_dict,
                     "地址": None, "薪资": None, "职称": None, "出生日期": None, "其他": None}

    # 设置信息
    def set_info_dict(self, info_dict: Dict[str, str]):
        key_list = [key for key in self.info.keys() if key in info_dict.keys()]
        for key in key_list:
            self.info[key] = info_dict[key]

    # 按键值设置信息
    def set_info(self, cls: str, new_info: str):
        if cls in self.edu_dict.keys():
            self.edu_dict[cls] = new_info
            self.info["学历"] = self.edu_dict
            return True, {"学历": self.edu_dict}
        elif cls in self.info.keys() and cls != "学历":
            self.info[cls] = new_info
            return True, {cls: new_info}
        else:
            return False, cls + "不存在！"

    # 获取信息
    def get_info(self, cls):
        if cls in self.info:
            return self.info[cls]
        return None


class Employee:
    def __init__(self, name: str, employee_id: str):
        # 姓名和工号，后者默认为身份证号，保证不与其他人相同
        self.name = name
        self.employee_id = employee_id
        # 职位信息，用字典表示，key:部门编号(str)|value:职位名称(Enum.Title)
        self.title_dict = {}
        self.info = PrivateMessage()

    def set_info(self, _info: PrivateMessage):
        self.info = _info

    def set_title(self, dep_id: str, title: str):
        self.title_dict[dep_id] = title

    def get_dep_title(self, dep_id):
        if dep_id in self.title_dict:
            return self.title_dict[dep_id]
        return None

    def get_info(self):
        return self.info

    def get_all_title(self):
        return self.title_dict

    def leave_dep(self, dep_id: str):
        if dep_id in self.title_dict:
            self.title_dict.pop(dep_id)
            return True
        return False

    def __str__(self):
        return self.employee_id + ":" + self.name + " " + str(self.title_dict)

    def __repr__(self):
        return self.employee_id + ":" + self.name + str(self.title_dict)

    def __eq__(self, other):
        return self.employee_id == other.employee_id

    def __hash__(self):
        return hash(self.employee_id)


class Department:
    def __init__(self, name: str, dep_id: str, lv: int = 0):
        # 部门名称和编号
        self.name = name
        self.dep_id = dep_id
        self.level = lv  # 记录结点层数
        # 上下级部门
        self.child_list = []
        # 职工列表
        self.employee_id_list = []
        self.manager_id = None
        self.vice_manager_id_list = []

    # 设置部门名称
    def set_name(self, new_name):
        self.name = new_name

    # 获取部门名称
    def get_name(self):
        return self.name

    # 获取部门编号
    def get_id(self):
        return self.dep_id

    # 获取部门主管id
    def get_manager(self):
        return self.manager_id

    # 获取部门副主管id列表
    def get_vice_manager(self):
        return self.vice_manager_id_list

    # 获取部门职工id列表
    def get_employee(self):
        return self.employee_id_list

    # 设置主管
    def set_manager(self, employee_id: str):
        if employee_id == self.manager_id:
            return None
        ex_id = self.manager_id
        if employee_id in self.employee_id_list:
            self.manager_id = employee_id
            return ex_id
        return None

    # 添加副主管
    def add_vice_manager(self, employee_id: str):
        if employee_id in self.vice_manager_id_list:
            return False, "已经是副主管！"
        if employee_id == self.manager_id:
            return False, "已经是主管,请先将其免职！"
        if employee_id in self.employee_id_list:
            self.vice_manager_id_list.append(employee_id)
            return True, employee_id
        return False, "职工 " + employee_id + " 不存在！"

    # 添加员工
    def add_employee(self, employee_id: str):
        if employee_id in self.employee_id_list:
            return False, "职工 " + employee_id + " 已存在！"
        self.employee_id_list.append(employee_id)
        return True, employee_id

    # 删除员工
    def remove_employee(self, employee_id: str):
        if employee_id not in self.employee_id_list:
            return False, "职工 " + employee_id + " 不存在！"
        self.employee_id_list.remove(employee_id)
        if self.manager_id == employee_id:
            self.manager_id = None
        if employee_id in self.vice_manager_id_list:
            self.vice_manager_id_list.remove(employee_id)
        return True, employee_id

    # 撤销主管
    def dismiss_manager(self):
        _id = self.manager_id
        self.manager_id = None
        return _id

    # 撤销副主管
    def dismiss_vice_manager(self, employee_id: str):
        if employee_id in self.vice_manager_id_list:
            self.vice_manager_id_list.remove(employee_id)
            return True, employee_id
        return False, "职工 " + employee_id + " 不是副主管！"

    # 获取部门同级编号
    def get_subid(self):
        # 得到self.level级的子id
        idlt = self.dep_id.split('.')
        if len(idlt) != self.level + 1:
            return False
        return idlt[self.level]

    # 为下级部门分配编号
    def attribute_subid(self):
        subid_list = []
        for child in self.child_list:
            if child.get_subid():
                subid_list.append(child.get_subid())
            else:
                winfo = "获取" + str(child) + "的subid时出错"
                print(winfo)
                return False, winfo
        # 遍历直到找到可供分配的subid
        i = 1
        while True:
            if str(i) not in subid_list:
                return str(i)
            i += 1
            if i > 200:
                winfo = "找不到可供分配的子域名"
                return winfo

    # 添加下级部门
    def add_child_dep(self, child_dep):
        if child_dep in self.child_list:
            return False, self.name + "." + child_dep.name + "已存在!"
        self.child_list.append(child_dep)
        child_dep.level = self.level + 1
        return True, child_dep

    # 删除下级部门
    def remove_child_dep(self, child_dep):
        if child_dep not in self.child_list:
            return False, self.name + "." + child_dep.name + " 不存在!"
        for cd in self.child_list:
            if cd.dep_id == child_dep.dep_id:
                self.child_list.remove(cd)
                return True, cd

    # 判断是否为根部门
    def is_root_dep(self) -> bool:
        return self.level == 0

    def __hash__(self):
        return hash(self.dep_id)

    def __eq__(self, other):
        return self.dep_id == other.dep_id

    def __str__(self):
        return self.name + "-" + self.dep_id

    def __repr__(self):
        return self.name + "-" + self.dep_id


class SchoolSystem:
    def __init__(self):
        # 系统根节点
        self.root_dep = Department("同济大学", "0")
        self.add_dep(self.root_dep, "回收")
        self.employee_list = []

    # 添加部门
    def add_dep(self, parent_dep: Department, dep_name: str):
        if parent_dep.dep_id == "0.1":
            return False
        # parent_dep是self的成员
        _dep_id = parent_dep.dep_id + "." + parent_dep.attribute_subid()
        parent_dep.add_child_dep(Department(dep_name, _dep_id))
        return _dep_id

    # 查找部门
    def get_dep(self, dep_id: str) -> [bool, Department]:
        hierarchy_id = dep_id.split('.')
        tmp_id_loc = 0
        tmp_list = [self.root_dep]
        tmp_dep = self.root_dep
        while tmp_id_loc != len(hierarchy_id):
            # 遍历寻找subid符合的子部门
            _flag = False
            for _dep in tmp_list:
                if _dep.get_subid() == hierarchy_id[tmp_id_loc]:
                    # 找到
                    _flag = True
                    tmp_id_loc += 1  # 再下一级域名
                    tmp_list = _dep.child_list  # 下一级子节点
                    tmp_dep = _dep  # 记录当前节点
                    break
            if not _flag:
                # 未找到
                winfo = "第" + str(tmp_id_loc) + "个subid没有找到！"
                print(winfo)
                return False, tmp_id_loc
        return True, tmp_dep

    # 将部门所有职员对应职位清除
    def dep_dismiss_all_employee(self, _dep: Department):
        if len(_dep.child_list) > 0:
            for child_dep in _dep.child_list:
                # 递归处理所有子部门
                self.dep_dismiss_all_employee(child_dep)
        for emp_id in _dep.employee_id_list:
            _employee = self.get_employee(emp_id)
            if _dep.dep_id in _employee.title_dict:
                _employee.title_dict.pop(_dep.dep_id)

    # 删除部门，该部门与下属部门被添加到回收部门(这样做是为了避免解雇所有员工，因为他们可能有其他职务)
    # 删除部门的静态方法，不推荐使用
    def remove_dep(self, parent_dep: Department, _dep: Department):
        if _dep not in parent_dep.child_list:
            return False, "子部门不存在！"
        # 部门一旦不存在，需要删除该部门及所有子部门的职工title
        self.dep_dismiss_all_employee(_dep)
        parent_dep.remove_child_dep(_dep)

        _flag, recycle_dep = self.get_dep("0.1")
        recycle_dep.child_list.append(_dep)
        return True, _dep

    # 删除部门的动态方法
    def remove_dep_by_id(self, dep_id: str):
        # 找到要删除的节点
        _flag, _dep = self.get_dep(dep_id)
        if not _flag:
            return _flag, _dep
        # 找到父节点
        hid = dep_id.split('.')
        hid.pop()
        pid = '.'.join(hid)
        _flag, parent_dep = self.get_dep(pid)
        if not _flag:
            return _flag, parent_dep
        # 部门一旦不存在，需要删除该部门及所有子部门的职工title
        self.dep_dismiss_all_employee(_dep)
        parent_dep.remove_child_dep(_dep)

        _flag, recycle_dep = self.get_dep("0.1")
        recycle_dep.child_list.append(_dep)
        return True, _dep

    # 查找职员
    def get_employee(self, emp_id: str):
        if emp_id is None:
            return None
        for _employee in self.employee_list:
            if _employee.employee_id == emp_id:
                return _employee
        return None

    # 添加职员到某部门，默认为根部门
    # 添加职员的静态方法，不推荐使用
    def add_employee_by_dep(self, _employee: Employee, _dep: Department):
        if _employee not in self.employee_list:
            self.employee_list.append(_employee)
        _employee.set_title(_dep.dep_id, "员工")
        return _dep.add_employee(_employee.employee_id)  # 部门只储存工号

    # 添加职员的动态方法，需要查找，默认为根部门
    def add_employee_by_dep_id(self, _employee: Employee, dep_id: str = "0"):
        # 初始时设置为该部门普通职员
        _flag, _dep = self.get_dep(dep_id)
        if not _flag:
            return False, _dep
        if _employee.employee_id in _dep.employee_id_list:
            return False, "职工已存在！"
        if _employee not in self.employee_list:
            self.employee_list.append(_employee)
        _employee.set_title(_dep.dep_id, "员工")
        return _dep.add_employee(_employee.employee_id)  # 部门只储存工号

    # 设置职务，不可以降职
    # 设置职务的静态方法，不需要查找，不推荐使用
    def set_title(self, employee: Employee, _dep: Department, title: str):
        dep_id = _dep.dep_id
        emp_id = employee.employee_id
        if title == "主管":
            employee.set_title(dep_id, title)
            # 修改前任主管信息,因为主管只能有一个
            ex_manager_id = _dep.set_manager(emp_id)
            if ex_manager_id is not None:
                ex_manager = self.get_employee(ex_manager_id)
                if dep_id in ex_manager.title_dict:
                    ex_manager.set_title(dep_id, "员工")
        elif title == "副主管":
            # 副主管可以有多个
            flag, _ = _dep.add_vice_manager(emp_id)
            if flag:
                employee.set_title(dep_id, title)
        else:
            return False, "职位不存在"

    # 设置职务的动态方法，需要查找
    def set_title_by_id(self, emp_id: str, dep_id: str, title: str):
        employee = self.get_employee(emp_id)
        if employee is None:
            winfo = "职工 " + emp_id + " 不存在！"
            return False, winfo
        _flag, _dep = self.get_dep(dep_id)
        if not _flag:
            winfo = "第" + str(_dep) + "个subid没有找到！"
            print(winfo)
            return False, winfo
        if title == "主管":
            employee.set_title(dep_id, title)
            # 修改前任主管信息,因为主管只能有一个
            ex_manager_id = _dep.set_manager(emp_id)
            if ex_manager_id is not None:
                ex_manager = self.get_employee(ex_manager_id)
                if dep_id in ex_manager.title_dict:
                    ex_manager.set_title(dep_id, "员工")
        elif title == "副主管":
            # 副主管可以有多个
            flag, _ = _dep.add_vice_manager(emp_id)
            if flag:
                employee.set_title(dep_id, title)
        else:
            return False, "职位不存在"

    # 解除职务
    # 解除职务的静态方法，不需要查找，不推荐使用
    def dis_dismiss_title(self, employee: Employee, _dep: Department):
        dep_id = _dep.dep_id
        emp_id = employee.employee_id
        if employee.title_dict[dep_id] == "主管":
            _dep.dismiss_manager()
            employee.set_title(dep_id, "员工")
        elif employee.title_dict[dep_id] == "副主管":
            _dep.dismiss_vice_manager(emp_id)
            employee.set_title(dep_id, "员工")
        winfo = emp_id + " 未在部门 " + dep_id + " 任职！"
        print(winfo)
        return False, winfo

    # 解除职务的动态方法，需要查找
    def dismiss_title_by_id(self, emp_id: str, dep_id: str):
        employee = self.get_employee(emp_id)
        if employee is None:
            winfo = "职工 " + emp_id + " 不存在！"
            return False, winfo

        _flag, _dep = self.get_dep(dep_id)
        if not _flag:
            winfo = "第" + str(_dep) + "个subid没有找到！"
            print(winfo)
            return False, winfo
        # 从emp维护
        if employee.title_dict[dep_id] == "主管":
            _dep.dismiss_manager()
            employee.set_title(dep_id, "员工")
        elif employee.title_dict[dep_id] == "副主管":
            _dep.dismiss_vice_manager(emp_id)
            employee.set_title(dep_id, "员工")
        # 从dep维护
        if _dep.manager_id == emp_id:
            _dep.dismiss_manager()
        if emp_id in _dep.vice_manager_id_list:
            _dep.dismiss_vice_manager(emp_id)
        winfo = emp_id + " 未在部门 " + dep_id + " 任职！"
        print(winfo)
        return False, winfo

    # 调离部门
    # 调离部门的静态方法，无需查找，不推荐使用
    def leave_dep(self, employee: Employee, _dep: Department):
        _dep.remove_employee(employee.employee_id)
        employee.leave_dep(_dep.dep_id)

    # 调离部门动态方法
    def leave_dep_by_id(self, emp_id: str, dep_id: str):
        employee = self.get_employee(emp_id)
        if employee is None:
            winfo = "职工 " + emp_id + " 不存在！"
            return False, winfo
        _flag, _dep = self.get_dep(dep_id)
        if not _flag:
            winfo = "第" + str(_dep) + "个subid没有找到！"
            print(winfo)
            return False, winfo
        _dep.remove_employee(employee.employee_id)
        employee.leave_dep(_dep.dep_id)

    # 调离某部门及下级部门
    # 调离某部门及下级部门的静态方法
    def leave_dep_totally(self, employee: Employee, _dep: Department):
        for child_dep in _dep.child_list:
            self.leave_dep_totally(employee, child_dep)
        _dep.remove_employee(employee.employee_id)
        employee.leave_dep(_dep.dep_id)

    # 调离某部门及下级部门的动态方法
    def leave_dep_totally_by_id(self, emp_id: str, dep_id: str):
        employee = self.get_employee(emp_id)
        if employee is None:
            winfo = "职工 " + emp_id + " 不存在！"
            return False, winfo
        _flag, _dep = self.get_dep(dep_id)
        if not _flag:
            winfo = "第" + str(_dep) + "个subid没有找到！"
            print(winfo)
            return False, winfo
        self.leave_dep_totally(employee, _dep)

    # 解雇职工
    def remove_employee(self, emp_id: str):
        employee = self.get_employee(emp_id)
        if employee is None:
            winfo = "职工不存在！"
            print(winfo)
            return None
        # 删除部门任职记录
        for dep_id in employee.title_dict.keys():
            _flag, _dep = self.get_dep(dep_id)
            if _flag:
                _dep.remove_employee(emp_id)
        self.employee_list.remove(employee)

    # 获取某部门全体职工信息(不包括下级部门)
    def get_emp_list_by_id(self, dep_id: str):
        # 获取部门
        flag, dep = self.get_dep(dep_id)
        if not flag:
            return None
        # 获取职工id列表
        emp_id_list = dep.employee_id_list
        # 逐个添加职工
        emp_list = []
        manager = []
        vice_list = []
        for emp_id in emp_id_list:
            emp = self.get_employee(emp_id)
            if emp is None:
                continue
            if emp_id == dep.manager_id:
                manager = [emp]
            elif emp_id in dep.vice_manager_id_list:
                vice_list.append(emp)
            else:
                emp_list.append(emp)
        # 先主管，再副主管，再普通员工，排好序
        manager.extend(vice_list)
        manager.extend(emp_list)
        return manager

    # 获取某部门全体职工信息(包括下级部门)
    def get_all_emp_list(self, dep_id: str):
        flag, dep = self.get_dep(dep_id)
        if not flag:
            return None
        emp_list = self.get_emp_list_by_id(dep_id)
        for child in dep.child_list:
            emp_list.extend(self.get_all_emp_list(child.dep_id))
        return emp_list

    # 按姓名查找职工
    def search_emp_by_name(self, emp_name: str):
        emp_list = []
        for emp in self.employee_list:
            if emp.name == emp_name:
                emp_list.append(emp)
        return emp_list
