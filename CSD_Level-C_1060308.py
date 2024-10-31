# 【試題編號】11900-1060308
# 【題目】分數加、減、乘、除運算
# 【説明】下表列出分數的四則運算法則。
#     運算        範例        公式
#     加法      b/a + y/x  (bx+ay)/ax
#     減法      b/a - y/x  (bx-ay)/ax
#     乘法      b/a * y/x    by/ax
#     除法      b/a / y/x    bx/ay
# 請依題意及以下的功能動作要求，設計一程式以求出每一組分數之間的運算結果。
from tkinter import *
from tkinter.ttk import *

def showWindow(datas):
    root = Tk()
    root.title('求出分數的加、減、乘、除運算')
    root.geometry('480x380')

    labelframe = LabelFrame(root, text='應檢人資料')

    lab1 = Label(labelframe, text='姓名', width=8, anchor=E)
    lab1.grid(row=0, column=0, padx=5, pady=5, sticky=W)
    ent1 = Entry(labelframe, width=12)
    ent1.grid(row=0, column=1, padx=5, pady=5, sticky=W)
    ent1.insert('0', '陳自強')
    lab2 = Label(labelframe, text='術科測試編號', width=18, anchor=E)
    lab2.grid(row=0, column=2, padx=5, pady=5, sticky=W)
    ent2 = Entry(labelframe, width=12)
    ent2.grid(row=0, column=3, padx=5, pady=5, sticky=W)
    ent2.insert('0', '106010203')
    lab3 = Label(labelframe, text='座號', width=8, anchor=E)
    lab3.grid(row=1, column=0, padx=5, pady=5, sticky=W)
    ent3 = Entry(labelframe, width=12)
    ent3.grid(row=1, column=1, padx=5, pady=5, sticky=W)
    ent3.insert('0', '01')
    lab4 = Label(labelframe, text='考  試  日   期', width=18, anchor=E)
    lab4.grid(row=1, column=2, padx=5, pady=5, sticky=W)
    ent4 = Entry(labelframe, width=12)
    ent4.grid(row=1, column=3, padx=5, pady=5, sticky=W)
    ent4.insert('0', '2017/01/26')

    labelframe.pack(fill=X, padx=10, pady=10)

    # 建立Treeview
    tree = Treeview(root, columns=('VALUE1', 'OP', 'VALUE2', 'ANSWER'))
    # 建立欄標題
    tree.heading('#0')
    tree.heading('#1', text='VALUE1')
    tree.heading('#2', text='OP')
    tree.heading('#3', text='VALUE2')
    tree.heading('#4', text='ANSWER')
    # 格式化欄位
    tree.column('#0', width=20, anchor=CENTER)
    tree.column('#1', width=110, anchor=CENTER)
    tree.column('#2', width=110, anchor=CENTER)
    tree.column('#3', width=110, anchor=CENTER)
    tree.column('#4', width=110, anchor=CENTER)

    tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

    # 建立內容
    for data in datas:
        tree.insert('', index=END, values=data)

    root.mainloop()

def loadfile(fn):
    datas = []
    with open(fn) as file_Obj:
        for line in file_Obj:
            datas.append(line.rstrip().split(','))
    return datas

def results(datas):
    newdatas = []
    for data in datas:
        b, a, op, y, x = data
        newdata = [b+'/'+a, op, y+'/'+x]
        b = int(b)
        a = int(a)
        y = int(y)
        x = int(x)
        ansTop = 0
        ansDown = 0
        if op == '+':
            ansTop = b * x + a * y
            ansDown = a * x
        elif op == '-':
            ansTop = b * x - a * y
            ansDown = a * x
        elif op == '*':
            ansTop = b * y
            ansDown = a * x
        elif op == '/':
            ansTop = b * x
            ansDown = a * y
        gcd = 1
        for i in range(2, ansTop+1):
            if ansTop % i == 0 and ansDown % i == 0:
                gcd = i
        ansTop /= gcd
        ansDown /= gcd
        ans = str(int(ansTop)) + '/' + str(int(ansDown))
        if ansDown == 1: ans = str(int(ansTop))
        if ansTop ==0: ans = '0'
        newdata.append(ans)
        newdatas.append(newdata)
    return newdatas

if __name__ == '__main__':
    fn = 'D:\\test\\1060308.SM'
    datas = loadfile(fn)
    datas = results(datas)
    showWindow(datas)


