import base64

my_id = 'admin'
my_pw = 'nimda'

my_id = my_id.encode('UTF-8')
my_pw = my_pw.encode('UTF-8')

for i in range(20):
    my_id = base64.b64encode(my_id)
    my_pw = base64.b64encode(my_pw)

my_id = str(my_id)
my_pw = str(my_pw)

my_id.replace('1', '!')
my_id.replace('2', '@')
my_id.replace('3', '$')
my_id.replace('4', '^')
my_id.replace('5', '&')
my_id.replace('6', '*')
my_id.replace('7', '(')
my_id.replace('8', ')')

my_pw.replace('1', '!')
my_pw.replace('2', '@')
my_pw.replace('3', '$')
my_pw.replace('4', '^')
my_pw.replace('5', '&')
my_pw.replace('6', '*')
my_pw.replace('7', '(')
my_pw.replace('8', ')')

print('id:',my_id)
print('pw:',my_pw)
