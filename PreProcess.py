import json
import random
from typing import List

from DataStructure import SchoolSystem, Title
from MyFaker import faker_employee_list

f2 = open('dep.json', 'r')
dep_dict = json.load(f2)


# 部门初始化
def init_dep(school_sys: SchoolSystem):
    name2id = {school_sys.root_dep.name: "0"}
    for dep_key in dep_dict.keys():
        # 添加一级部门
        name2id[dep_key] = school_sys.add_dep(school_sys.root_dep, dep_key)
        for sub_key in dep_dict[dep_key].keys():
            # 添加子部门
            flag, dep = school_sys.get_dep(name2id[dep_key])
            if flag:
                name2id[sub_key] = school_sys.add_dep(dep, sub_key)

                if len(dep_dict[dep_key][sub_key]) > 0:
                    # 子部门之下还有三级部门
                    sub_flag, sub_dep = school_sys.get_dep(name2id[sub_key])
                    if sub_flag:
                        for sub_sub_dep in dep_dict[dep_key][sub_key]:
                            name2id[sub_sub_dep] = school_sys.add_dep(sub_dep, sub_sub_dep)
    return name2id


# 职工初始化
def init_employee(school_sys: SchoolSystem, id_list: List[str]):
    # employee有随机性
    seed = 42
    random.seed(seed)

    for emp in faker_employee_list:
        tmp_ids = set(random.choices(id_list, k=random.randint(2, 5)))
        for dep_id in tmp_ids:
            flag, _ = school_sys.add_employee_by_dep_id(emp, dep_id)

            lucky_title = random.choices(Title, weights=[1, 1, 1], k=1)[0]
            school_sys.set_title_by_id(emp.employee_id, dep_id, lucky_title)

        seed += 1
        random.seed(seed)  # 更新seed使得每个employee的title数量不同
