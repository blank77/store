
# 说说你认为 Python3 和 Python2 之间的区别？（京东测试开发面试）
# Python2和Python3之间的区别有：1、输出print的不同；2、整数除法，返回值的不同；3、列表理解循环变量方面；4、Unicode字符串方面；5、错误处理方面；6、xrange方面不同等等

# 标识符	    是否合法	标识符	是否合法
# char	    合法	    Cy%ty	不合法
# Oax_li	合法	    $123	不合法
# fLul	    合法  	3_3 	不合法
# BYTE	    合法	    T_T 	合法

A=56
B=78
A=A+B
B=A-B
A=A-B

print(A,B)

a = 1
b = 2
c = 3
d = 4
e = 5
n = sum((a,b,c,d,e))
f = n/5
print(n,f)

num1 = 45
num2 = num1
print(num1,num2)