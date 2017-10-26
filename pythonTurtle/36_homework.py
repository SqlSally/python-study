#0. 按照以下提示尝试定义一个person类并生成类实例对象

#属性：姓名（默认姓名为『小甲鱼』）
#方法：打印姓名
#提示： 方法中属性的引用形式虚假上self 例如：self.name

class person:
    name = "xiaojiayu"

    def PrintName(self):
        print(self.name)


#按照以下提示尝试定义一个矩形类并生成类实例对象

#属性：长和宽
#方法：设置长和宽--》setRect(self), 获得长和宽--》getRect(self）,或的面积-->getArea(self)
#提示:方法中对属性的引用形式需要加上 self，如self.width

class rec:
    length = 5
    width = 4

    def setRect(self):
        print("请输入矩形的长和宽：")
        self.length = float(input("长："))
        self.width = float(input("宽："))

    def getRect(self):
        print("这个矩形的长是{0},宽是：{1}" .format(self.length, self.width))

    def getArea(self):
        print("面积是：",end="")
        return self.length * self.width

a = rec()
print(a.setRect())
print(a.getRect())
print(a.getArea())

