#_author_='leafletxie'
#coding=utf-8

d={'adam':75,'tom':82,'jerry':99,'sarah':92}
print('成绩单：',d)
name=input('请输入您的姓名：')
d[name]=int(input('请输入您的成绩：'))
print('更新后的成绩单：',d)
name=input('请输入您要查询成绩的姓名：')
if name in d:
    print('%s的成绩是：%d'%(name,d[name]))
else:
    print('抱歉，未查询到相关成绩！')
    c=input("输入'Y'新建该生成绩，输入任意键忽略：")
    if c=='Y':
        d[name]=int(input('请输入该生成绩：'))
        print('录入成功，%s的成绩是：%d'%(name,d[name]))
    else:
        z=input("感谢再次使用本系统，如对成绩有疑问，请输入'X'修改，输入任意键退出")
        if z=='X':
            name=input('请输入要修改成绩的学生的姓名：')
            d[name]=int(input('请输入该生成绩：'))
            print('修改成功！%s的成绩是：%d'%(name,d[name]))
        else:
            exit()
