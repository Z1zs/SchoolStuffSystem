from enum import Enum
from Spider import dep_dict
from typing import List, Dict, Tuple


class Title(Enum):
    manager = 1
    vice_manager = 2
    worker = 3


chinese_title = {Title.manager: "主管", Title.vice_manager: "副主管", Title.worker: "员工"}


class PrivateMessage:
    def __init__(self):
        self.edu_dict = {"学士": None, "硕士": None, "博士": None}
        self.info = {"年龄": None, "性别": None, "手机号": None, "邮箱": None, "身份证号": None, "学历": self.edu_dict,
                     "地址": None, "薪资": None, "职称": None, "出生日期": None, "其他": None}

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

    def get_info(self, cls):
        if cls in self.info:
            return self.info[cls]
        return None


class Stuff:
    def __init__(self, name: str, employee_id: str):
        # 姓名和工号，后者默认为身份证号，保证不与其他人相同
        self.name = name
        self.employee_id = employee_id
        # 职位信息，用字典表示，key:部门编号(str)|value:职位名称(Enum.Title)
        self.title_dict = {}
        self.info = PrivateMessage()

    def set_title(self, dep_id: str, title: Title):
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
    def __init__(self, name: str, dep_id: str, parent: str = None, lv: int = 0):
        # 部门名称和编号
        self.name = name
        self.dep_id = dep_id
        self.level = lv  # 记录结点层数
        # 上下级部门
        self.child_list = []
        # 职工列表
        self.stuff_id_list = []
        self.manager_id = None
        self.vice_manager_id_list = []

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def get_id(self):
        return self.dep_id

    def get_manager(self):
        return self.manager_id

    def get_vice_manager(self):
        return self.vice_manager_id_list

    def get_stuff(self):
        return self.stuff_id_list

    def set_manager(self, stuff_id: str):
        if stuff_id in self.stuff_id_list:
            self.manager_id = stuff_id
            return True, self.manager_id
        return False, "职工 " + stuff_id + " 不存在！"

    def add_vice_manager(self, stuff_id: str):
        if stuff_id in self.stuff_id_list:
            self.vice_manager_id_list.append(stuff_id)
            return True, stuff_id
        return False, "职工 " + stuff_id + " 不存在！"

    def add_stuff(self, stuff_id: str):
        if stuff_id in self.stuff_id_list:
            return False, "职工 " + stuff_id + " 已存在！"
        self.stuff_id_list.append(stuff_id)
        return True, stuff_id

    def remove_stuff(self, stuff_id: str):
        if stuff_id not in self.stuff_id_list:
            return False, "职工 " + stuff_id + " 不存在！"
        self.stuff_id_list.remove(stuff_id)
        if self.manager_id == stuff_id:
            self.manager_id = None
        if stuff_id in self.vice_manager_id_list:
            self.vice_manager_id_list.remove(stuff_id)
        return True, stuff_id

    def dismiss_manager(self):
        _id = self.manager_id
        self.manager_id = None
        return _id

    def dismiss_vice_manager(self, stuff_id: str):
        if stuff_id in self.vice_manager_id_list:
            self.vice_manager_id_list.remove(stuff_id)
            return True, stuff_id
        return False, "职工 " + stuff_id + " 不是副主管！"

    def get_subid(self):
        # 得到self.level级的子id
        idlt = self.dep_id.split('.')
        if len(idlt) != self.level + 1:
            return False
        return idlt[self.level]

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

    def add_child_dep(self, child_dep):
        if child_dep in self.child_list:
            return False, self.name + "." + child_dep.name + "已存在!"
        self.child_list.append(child_dep)
        child_dep.level = self.level + 1
        return True, child_dep

    def remove_child_dep(self, child_dep):
        if child_dep not in self.child_list:
            return False, self.name + "." + child_dep.name + " 不存在!"
        for cd in self.child_list:
            if cd.dep_id == child_dep.dep_id:
                self.child_list.remove(cd)
                return True, cd

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
        self.stuff_list = []

    def add_dep(self, parent_dep: Department, dep_name: str):
        if parent_dep.dep_id == "0.1":
            winfo = "不能为回收部添加下级部门！"
            return False, winfo
        # parent_dep是self的成员
        dep_id = parent_dep.dep_id + "." + parent_dep.attribute_subid()
        parent_dep.add_child_dep(Department(dep_name, dep_id))
        return dep_id

    def get_dep_stuff_update(self, _dep: Department):
        for emp_id in _dep.stuff_id_list:
            _flag, stuff = self.get_stuff(emp_id)
            if not _flag:
                # 职员不存在
                _dep.remove_stuff(emp_id)
        return _dep

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
        return True, self.get_dep_stuff_update(tmp_dep)

    def remove_dep(self, dep_id: str):
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
        parent_dep.remove_child_dep(_dep)

        _flag, recycle_dep = self.get_dep("0.1")
        recycle_dep.child_list.append(_dep)
        _dep.parent_id = recycle_dep.dep_id
        return True, _dep

    def add_stuff(self, stuff: Stuff, dep_id: str = "0"):
        # 初始时设置为该部门普通职员
        flag, dep = self.get_dep(dep_id)
        if not flag:
            return False, dep
        if stuff in self.stuff_list:
            winfo = "该职员已存在，请尝试set_title方法！"
            return False, winfo
        self.stuff_list.append(stuff)
        stuff.set_title(dep_id, Title.worker)
        return dep.add_stuff(stuff.employee_id)  # 部门只储存工号

    def get_stuff(self, emp_id: str):
        if emp_id is None:
            return None
        for stuff in self.stuff_list:
            if stuff.employee_id == emp_id:
                return self.get_stuff_title_update(stuff)  # 顺便刷新一下title_dict，因为有些部门可能已经被删除
        return None

    def get_stuff_title_update(self, stuff: Stuff):
        for dep_id in stuff.title_dict.keys():
            _flag, _dep = self.get_dep(dep_id)
            if not _flag:
                # 如果部门不存在，从title_dict中删除
                stuff.title_dict.pop(dep_id)
        return stuff

    def set_title(self, emp_id: str, dep_id: str, title: Title):
        stuff = self.get_stuff(emp_id)
        if stuff is None:
            winfo = "职工 " + emp_id + " 不存在！"
            return False, winfo
        _flag, _dep = self.get_dep(dep_id)
        if not _flag:
            winfo = "第" + str(_dep) + "个subid没有找到！"
            print(winfo)
            return False, winfo
        if title == Title.manager:
            stuff.set_title(dep_id, title)
            return _dep.set_manger(emp_id)
        elif title == Title.vice_manager:
            stuff.set_title(dep_id, title)
            return _dep.add_vice_manager(emp_id)
        winfo = "职位不存在！"
        print(winfo)
        return False, winfo

    # 解除职务
    def dismiss_title(self, emp_id: str, dep_id: str):
        stuff = self.get_stuff(emp_id)
        if stuff is None:
            winfo = "职工 " + emp_id + " 不存在！"
            return False, winfo
        _flag, _dep = self.get_dep(dep_id)
        if not _flag:
            winfo = "第" + str(_dep) + "个subid没有找到！"
            print(winfo)
            return False, winfo
        if stuff.title_dict[dep_id] == Title.manager:
            _dep.dismiss_manager(emp_id)
        elif stuff.title_dict[dep_id] == Title.vice_manager:
            _dep.dismiss_vice_mannager(emp_id)
        winfo = emp_id + " 未在部门 " + dep_id + " 任职！"
        print(winfo)
        return False, winfo

    # 调离部门
    def leave_dep(self, dep_id: str, emp_id: str):
        stuff = self.get_stuff(emp_id)
        if stuff is None:
            winfo = "职工 " + emp_id + " 不存在！"
            return False, winfo
        _flag, _dep = self.get_dep(dep_id)
        if not _flag:
            winfo = "第" + str(_dep) + "个subid没有找到！"
            print(winfo)
            return False, winfo
        _dep.remove_stuff(emp_id)
        stuff.leave_dep(dep_id)

    # 解雇职工
    def remove_stuff(self, emp_id: str):
        stuff = self.get_stuff(emp_id)
        if stuff is None:
            winfo = "职工不存在！"
            print(winfo)
        # 删除部门任职记录
        for dep_id in stuff.title_dict.keys():
            _flag, _dep = self.get_dep(dep_id)
            if _flag:
                _dep.remove_stuff(emp_id)
        self.stuff_list.remove(stuff)


dep_name2id = {}

s = SchoolSystem()
for dep_key in dep_dict.keys():
    # 添加一级部门
    dep_name2id[dep_key] = s.add_dep(s.root_dep, dep_key)
    for sub_key in dep_dict[dep_key].keys():
        # 添加子部门
        flag, dep = s.get_dep(dep_name2id[dep_key])
        if flag:
            dep_name2id[sub_key] = s.add_dep(dep, sub_key)

            if dep_dict[dep_key][sub_key]!=[]:
                # 子部门之下还有三级部门
                sub_flag, sub_dep = s.get_dep(dep_name2id[sub_key])
                if flag:
                    for sub_sub_dep in dep_dict[dep_key][sub_key]:
                        dep_name2id[sub_sub_dep] = s.add_dep(sub_dep, sub_sub_dep)

print(s.root_dep)
print(s.root_dep.child_list)
