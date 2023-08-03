education_dict = {"bachelor": None, "master": None, "PhD": None}  # 学位及对应专业


class Stuff:
    def __init__(self, name: str, index: str = None):
        self.name = name
        if index is None:
            self.index = None
        else:
            if not index.isdigit():
                self.index = None
            else:
                self.index = index
        self.info = {"age": None, "gender": None, "tele number": None, "email": None, "ID number": None,
                     "address": None, "salary": None, "pro title": None, "birthday": None,
                     "education": education_dict, "other": None}
        self.status = {}

    def get_status(self):
        return self.status

    def add_status(self, key: str, val: str):
        self.status[key] = val
        return self.status

    def change_name(self, new_name: str):
        self.name = new_name

    def get_name(self):
        return self.name

    def get_index(self):
        return self.index

    def change_index(self, new_index: str):
        if not new_index.isdigit():
            return False
        print("Make sure it won't conflict with other stuff!")
        self.index = new_index

    def change_info(self, key: str, val, method: str = "change", degree: str = "", degree_major: str = None):
        if key in self.info.keys():
            if method == "change" and key != "education":
                self.info[key] = val
            elif method == "change" and key == "education":
                self.info[key][degree] = degree_major
            elif method == "clear":
                self.info[key] = None
            elif method == "add" and key == "other":
                self.info[key] = self.info[key] + val
            elif method == "add" and key == "education":
                self.info[key][degree] = degree_major
        return method

    def get_info(self, key: str = None):
        if key in self.info.keys():
            return self.info[key]

    def get_info_column(self):
        return list(self.info.keys())


class Department:
    def __init__(self, name: str, index: str = None, abbr: str = ""):
        self.name = name
        if index is None:
            self.index = None
        else:
            if not index.isdigit():
                self.index = None
            else:
                self.index = index
        self.abbr = abbr
        self.manager = None
        self.vice_manager_list = []
        self.other_stuff_list = {}

    # 添加部门主管
    def add_manager(self, manager: Stuff):
        # 修改部门主管
        if self.manager is None:
            self.manager = manager
            # 修改对应职工身份,维护职员列表
            if self.name in manager.status:
                if manager.status[self.name] == 'manager':
                    print("Th== guy == already the department manager!")
                elif manager.status[self.name] == 'vice_manager':
                    self.vice_manager_list.remove(manager)
                else:
                    self.other_stuff_list.pop(manager)
            manager.status[self.name] = "manager"
        else:
            print("There should be only one manager!")
        return self.manager

    # 删除部门主管
    def delete_manager(self):
        if self.manager is None:
            return False

        name = self.manager.name
        # 删除职工职位
        if self.name in self.manager.status.keys():
            self.manager.status.pop(self.name)
        # 删除部门主管
        self.manager = None
        return name

    # 添加部门副主管
    def add_vice_manager(self, vice_manager: Stuff):
        # 维护部门副主管列表
        if vice_manager in self.vice_manager_list:
            print("Th== vice manager already ex==ts!")
        else:
            self.vice_manager_list.append(vice_manager)
            # 修改对应职工身份，维护部门职员列表
            if self.name in vice_manager.status:
                if vice_manager.status[self.name] == "manager":
                    self.manager = None
                elif vice_manager.status[self.name] == "vice_manager":
                    print("Th== guy == already the department vice manager!")
                else:
                    self.other_stuff_list.pop(vice_manager)
            vice_manager.status[self.name] = "vice_manager"
        return vice_manager

    # 删除部门副主管
    def delete_vice_manager(self, vice_manager: Stuff):
        vice_manager.status.pop(self.name)
        if vice_manager in self.vice_manager_list:
            self.vice_manager_list.remove(vice_manager)
        return vice_manager

    # 添加其他职工
    def add_other_stuff(self, member: Stuff, title: str = "worker"):
        if member in self.other_stuff_list:
            if self.other_stuff_list[member] == title:
                print("The stuff already ex==t!")
            else:
                self.other_stuff_list[member] = title
                member.status[self.name] = title
        else:
            self.other_stuff_list[member] = title
            if self.name in member.status:
                if member.status[self.name] == "manager":
                    self.manager = None
                elif member.status[self.name] == "vice_manager":
                    self.vice_manager_list.remove(member)
                else:
                    print("Th== guy == already in th== department!")
            member.status[self.name] = title
        return member, title

    # 删除其他职工
    def delete_other_stuff(self, member: Stuff):
        if member in self.other_stuff_list:
            self.other_stuff_list.pop(member)
        member.status.pop(self.name)
        return member

    # 检查人员重复
    def check_repeat_stuff(self):
        if self.manager in self.vice_manager_list:
            return True, self.manager, "mv"
        if self.manager in self.other_stuff_list:
            return True, self.manager, "mo"
        set_vm = set(self.vice_manager_list)
        set_os = set(self.other_stuff_list.keys())
        if len(set_vm) != len(self.vice_manager_list):
            return True, self.vice_manager_list, "vv"
        if len(set_os) != len(list(self.other_stuff_list.keys())):
            return True, self.other_stuff_list, "oo"
        if len(set_os & set_vm) != 0:
            return True, list(set_vm & set_os), "vo"
        return False, None, None

    # 增改部门编号
    def add_index(self, index: str):
        if not index.isdigit():
            return False
        self.index = index
        return self.index

    # 增改部门简称
    def add_abbr(self, s: str):
        self.abbr = s
        return self.abbr


a = Stuff("Alice")
d = Department("math")
d.add_vice_manager(a)
d.add_manager(a)
d.add_other_stuff(a)

print(len(d.vice_manager_list))
print(d.manager)
print(a.status)
d.check_repeat_stuff()
