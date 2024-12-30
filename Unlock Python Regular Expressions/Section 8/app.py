import openpyxl

workbook = openpyxl.load_workbook(r"Section 8\Employees.xlsx")

print(workbook.sheetnames)
# ['EmployeeData', 'Skills']

sheet = workbook["EmployeeData"]
print(sheet.dimensions)
# A1:G21

for row in sheet.values:
    print(row)
# ('ID', 'FirstName', 'LastName', 'Department', 'Phone', 'Address', 'Salary')
# (1, 'Luke', 'Phillip', 'Sales', 5564567890, '1st Address, Miami', 25000)
# (2, 'Jack', 'Darren', 'IT', 3444567891, '2nd Address, Chicago', 33600)
# (3, 'Ken', 'Wood', 'IT', 5524567892, '3rd Address, LA', 41150)
# (4, 'John', 'Wilson', 'Marketing', 1124567893, '4th Address, Chicago', 50000)
# (5, 'Emily', 'Larson', 'Marketing', 1234567894, '5th Address, Miami', 48700)
# (6, 'Anna', 'Sullivan', 'Sales', 3324567895, '6th Address, Miami', 29000)
# (7, 'Richard', 'Smith', 'Logistics', 6894567896, '7th Address, New York', 66000)
# (8, 'Ronnie', 'Moore', 'Sales', 8974567897, '8th Address, New York', 87000)
# (9, 'Andrew', 'Drake', 'IT', 6654567898, '9th Address, Las Vegas', 66900)
# (10, 'Wayne', 'Barker', 'Logistics', 9884567899, '10th Address, Las Vegas', 89000)
# (11, 'Gina', 'Baker', 'Logistics', 1154567900, '11th Address, Chicago', 31800)
# (12, 'Andy', 'Williams', 'HR', 1094567901, '12th Address, Chicago', 65500)
# (13, 'Jack', 'Wood', 'Logistics', 2044567902, '13th Address, New York', 90300)
# (14, 'Jane', 'Phills', 'HR', 1664567903, '14th Address, New York', 77700)
# (15, 'Ron', 'Johnson', 'Sales', 1664567904, '15th Address, New York', 26250)
# (16, 'Jackie', 'Stanley', 'Sales', 6894567905, '16th Address, Las Vegas', 38400)
# (17, 'Charles', 'Meyer', 'Marketing', 1154567906, '17th Address, Las Vegas', 47000)
# (18, 'Charlie', 'Smith', 'Marketing', 9884567907, '18th Address, Las Vegas', 49000)
# (19, 'Wayne', 'Andrews', 'Sales', 3324567908, '19th Address, LA', 52000)
# (20, 'Adrian', 'Harrison', 'IT', 1234567909, '20th Address, LA', 21160)


data = []
# Iterating over sheet.values and appending the data as strings
for row in sheet.values:
    a, b, c, d, e, f, g = row
    data.append("{};{};{};{};{};{};{}".format(a, b, c, d, e, f, g))

# Joining the strings in the data list using the \n as a delimiter
employees = "\n".join(data)
print(employees)
# ID;FirstName;LastName;Department;Phone;Address;Salary
# 1;Luke;Phillip;Sales;5564567890;1st Address, Miami;25000
# 2;Jack;Darren;IT;3444567891;2nd Address, Chicago;33600
# 3;Ken;Wood;IT;5524567892;3rd Address, LA;41150
# 4;John;Wilson;Marketing;1124567893;4th Address, Chicago;50000
# 5;Emily;Larson;Marketing;1234567894;5th Address, Miami;48700
# 6;Anna;Sullivan;Sales;3324567895;6th Address, Miami;29000
# 7;Richard;Smith;Logistics;6894567896;7th Address, New York;66000
# 8;Ronnie;Moore;Sales;8974567897;8th Address, New York;87000
# 9;Andrew;Drake;IT;6654567898;9th Address, Las Vegas;66900
# 10;Wayne;Barker;Logistics;9884567899;10th Address, Las Vegas;89000
# 11;Gina;Baker;Logistics;1154567900;11th Address, Chicago;31800
# 12;Andy;Williams;HR;1094567901;12th Address, Chicago;65500
# 13;Jack;Wood;Logistics;2044567902;13th Address, New York;90300
# 14;Jane;Phills;HR;1664567903;14th Address, New York;77700
# 15;Ron;Johnson;Sales;1664567904;15th Address, New York;26250
# 16;Jackie;Stanley;Sales;6894567905;16th Address, Las Vegas;38400
# 17;Charles;Meyer;Marketing;1154567906;17th Address, Las Vegas;47000
# 18;Charlie;Smith;Marketing;9884567907;18th Address, Las Vegas;49000
# 19;Wayne;Andrews;Sales;3324567908;19th Address, LA;52000
# 20;Adrian;Harrison;IT;1234567909;20th Address, LA;21160
