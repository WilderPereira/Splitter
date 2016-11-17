import re

package_name = 'your.package.name'
table_name = raw_input('Table name:')
class_name = raw_input('Class name: ')

db_entity_file = '''ID	VARCHAR2(118)
ID	CHAR(18)
TEST_NUM	NUMBER(9)
TEST_STR	VARCHAR2(50)
TEST_DATE	TIMESTAMP(6)'''.lower()

pojo_file = open('empty_pojo.txt', 'r')
pojo = pojo_file.read()

#Regex definitions
strings_regex = '(\w+)(\s+((VAR)?CHAR).*)'
numbers_regex = '(\w+)(\s+(number.*))'
dates_regex = '(\w+)(\s+(timestamp.*))'

#Replacements definitions
strings = 'private String \1;'
numbers = 'private BigDecimal \1;'
dates = 'private Date \1;'

db_entity_file = re.sub(r'(\w+)(\s+((var)?char).*)',r'private String \1;', db_entity_file)
db_entity_file = re.sub(r'(\w+)(\s+(number.*))',r'private BigDecimal \1;', db_entity_file)
db_entity_file = re.sub(r'(\w+)((\s+((timestamp)|(date)).*))',r'private Date \1;', db_entity_file)

pojo = re.sub('FIELDS',db_entity_file,pojo)
pojo = re.sub('PACKAGE_NAME',package_name,pojo)
pojo = re.sub('TABLE_NAME',table_name,pojo)
pojo = re.sub('CLASS_NAME',class_name,pojo)

new_file = open('pojo.java','w')
new_file.write(pojo)

#TODO: Generate getters and setters with this regex: (?>private\s+)(\w+)\s+(\w+;)



