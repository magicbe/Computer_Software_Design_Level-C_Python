# 【試題編號】11900-1060306
# 【題目】身分證號碼檢查
from tkinter import *
from tkinter.ttk import *

def showWindow(datas):
    # 通用格式為4欄位
    root = Tk()
    root.title('身分證號碼檢查')
    root.geometry('480x380')

    labelframe = LabelFrame(root, text='應檢人資料')

    lab1 = Label(labelframe, text='姓名', width=8, anchor=E)
    lab1.grid(row=0, column=0, padx=5, pady=10, sticky=W)
    ent1 = Entry(labelframe, width=12)
    ent1.grid(row=0, column=1, padx=5, pady=10, sticky=W)
    ent1.insert(0, '陳自強')
    lab2 = Label(labelframe, text='術科測試編號', width=18, anchor=E)
    lab2.grid(row=0, column=2, padx=5, pady=10, sticky=W)
    ent2 = Entry(labelframe, width=12)
    ent2.grid(row=0, column=3, padx=5, pady=10, sticky=W)
    ent2.insert(0, '106010203')
    lab3 = Label(labelframe, text='座號', width=8, anchor=E)
    lab3.grid(row=1, column=0, padx=5, pady=10, sticky=W)
    ent3 = Entry(labelframe, width=12,)
    ent3.grid(row=1, column=1, padx=5, pady=10, sticky=W)
    ent3.insert(0, '01')
    lab4 = Label(labelframe, text='考   試   日   期', width=18, anchor=E)
    lab4.grid(row=1, column=2, padx=5, pady=10, sticky=W)
    ent4 = Entry(labelframe, width=12)
    ent4.grid(row=1, column=3, padx=5, pady=10, sticky=W)
    ent4.insert(0, '2017/01/26')

    labelframe.pack(fill=X, padx=10, pady=10)

    # 建立Treeview
    tree = Treeview(root, columns=(('ID_NO', 'NAME', 'SEX', 'ERROR')))
    # 建立欄標題
    tree.heading('#0')
    tree.heading('#1', text='ID_NO', anchor=W)
    tree.heading('#2', text='NAME', anchor=W)
    tree.heading('#3', text='SEX', anchor=W)
    tree.heading('#4', text='ERROR', anchor=W)
    # 格式化欄位
    tree.column('#0', width=30)
    tree.column('#1', width=120)
    tree.column('#2', width=120)
    tree.column('#3', width=50)
    tree.column('#4', width=200)
    # 建立內容
    for data in datas:
        tree.insert('', index=END, values=data)

    tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

    root.mainloop()

def loadFile(fn):
    datas = []
    with open(fn) as file_Obj:
        for line in file_Obj:
            datas.append(line.rstrip().split(','))
    return datas

def checkID(datas):
    # 按身分證號碼由小到大排序
    datas.sort()
    tmp_datas = []
    # 身分證號碼檢查
    for ID, name, sex in datas:
        error = ''
        # 格式檢查
        if (not str.istitle(ID)) or (not str.isdigit(ID[1:])):
            error = 'FORMAT ERROR'
        # 性別判定檢查
        elif not ((ID[1] == '1' and sex == 'M') or (ID[1] == '2' and sex == 'F')):
            error = 'SEX CODE ERROR'
        else:
            # 身分證檢核碼計算
            A2O = 'ABCDEFGHJKLMNPQRSTUVXYWZIO'
            L1 = A2O.find(ID[0]) + 10
            X1 = L1 // 10
            X2 = L1 % 10
            Y = X1 + 9 * X2 + int(ID[9])
            for i in range(1, 9):
                Y += (9 - i) * int(ID[i])
            if not (Y % 10 == 0):
                error = 'CHECK SUM ERROR'

        tmp_datas.append((ID, name, sex, error))

    return tmp_datas

if __name__ == '__main__':
    fn = 'D:\\test\\1060306.SM'
    datas = loadFile(fn)
    datas = checkID(datas)
    showWindow(datas)

