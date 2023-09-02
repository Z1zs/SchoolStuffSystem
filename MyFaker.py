import random
from typing import Dict

from faker import Faker

from DataStructure import PrivateMessage, Employee

# 批量生成1k个假职工
'''
"年龄": None, "性别": None, "手机号": None, "邮箱": None, "身份证号": None, "学历": self.edu_dict,
"地址": None, "薪资": None, "职称": None, "出生日期": None, "其他": None
'''
faker = Faker(locale="zh_CN")
Faker.seed(42)
random.seed(42)


# 从字典中提取个人信息
def extract_private_message(_pf: Dict[str, str]):
    sex = "男" if _pf['sex'] == 'M' else "女"
    ssn = _pf['ssn']
    birth_year = ssn[6:10]
    birth_month = ssn[10:12]
    birth_day = ssn[12:14]
    birthdate = f"{birth_year}-{birth_month}-{birth_day}"
    _info_dict = {"性别": sex, "手机号": faker.phone_number(), "邮箱": _pf['mail'], "身份证号": _pf['ssn'],
                  "地址": _pf['address'], "薪资": random.randint(4000, 20000), "出生日期": birthdate,
                  "年龄": 2023 - int(birth_year), "职称": random.choice(["教授", "副教授", "讲师"])}

    mess = PrivateMessage()
    mess.set_info_dict(_info_dict)

    _employee_ = Employee(pf['name'], pf['ssn'])
    _employee_.set_info(mess)
    return _employee_


length = 1000
faker_employee_list = []
while len(faker_employee_list) < length:
    pf = faker.profile()
    _employee = extract_private_message(pf)
    faker_employee_list.append(_employee)
