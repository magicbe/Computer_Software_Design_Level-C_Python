# 【試題編號】11900-1060307
# 【題目】撲克牌比大小
from tkinter import *
from tkinter.ttk import *

def showWindow(datas):
    # 通用格式為4欄位
    root = Tk()
    root.title('撲克牌比大小')
    root.geometry('480x380')

    labelframe = LabelFrame(root, text='應檢人資料')
    lab1 = Label(labelframe, text='姓名', width=8, anchor=E)
    lab1.grid(row=0, column=0, padx=5, pady=5, sticky=W)
    ent1 = Entry(labelframe, width=12)
    ent1.grid(row=0, column=1, padx=5, pady=5, sticky=W)
    ent1.insert(0, '陳自強')
    lab2 = Label(labelframe, text='術科測試編號', width=18, anchor=E)
    lab2.grid(row=0, column=2, padx=5, pady=5, sticky=W)
    ent2 = Entry(labelframe, width=12)
    ent2.grid(row=0, column=3, padx=5, pady=5, sticky=W)
    ent2.insert(0, '106010203')
    lab3 = Label(labelframe, text='座號', width=8, anchor=E)
    lab3.grid(row=1, column=0, padx=5, pady=5, sticky=W)
    ent3 = Entry(labelframe, width=12)
    ent3.grid(row=1, column=1, padx=5, pady=5, sticky=W)
    ent3.insert(0, '01')
    lab4 = Label(labelframe, text='考  試   日  期', width=18, anchor=E)
    lab4.grid(row=1, column=2, padx=5, pady=5, sticky=W)
    ent4 = Entry(labelframe, width=12)
    ent4.grid(row=1, column=3, padx=5, pady=5, sticky=W)
    ent4.insert(0, '2017/01/26')

    labelframe.pack(fill=X, padx=10, pady=10)

    # 建立Treeview
    tree = Treeview(root, columns=(('序號', '玩家', '莊家', '結果')))
    # 建立欄標題
    tree.heading('#0')
    tree.heading('#1', text='序號', anchor=W)
    tree.heading('#2', text='玩家', anchor=W)
    tree.heading('#3', text='莊家', anchor=W)
    tree.heading('#4', text='結果', anchor=W)
    # 格式化欄位
    tree.column('#0', width=20)
    tree.column('#1', width=80)
    tree.column('#2', width=120)
    tree.column('#3', width=120)
    tree.column('#4', width=120)

    tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

    # 建立內容
    for data in datas:
        tree.insert('', index=END, values=data)

    root.mainloop()


def loadFile(fn):
    global gno
    with open(fn) as file_Obj:
        datas = list(map(eval, file_Obj.read().split()))
    return datas

# 撲克牌比大小
def checkCard(datas):
    # 進行次數
    gno = datas[0]
    # 隨機數x52
    nums = [int(n * 52) for n in datas[1:]]
    cards = list(set(nums))
    cards.sort(key=nums.index)
    newdatas = []
    suit = [u'\u2660', u'\u2665', u'\u2666', u'\u2663']
    disp = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for i in range(gno):
        data = []
        data.append(i+1)
        msg = ''
        f1 = cards[i*2] // 13
        n1 = cards[i*2] % 13 + 1
        f2 = cards[i*2+1] // 13
        n2 = cards[i*2+1] % 13 + 1
        data = [i+1, suit[f1]+disp[n1], suit[f2]+disp[n2]]
        if n1 == 1: n1 += 13
        if n2 == 1: n2 += 13
        if n1 > n2: msg = '玩家贏'
        if n1 == n2: msg = '平手'
        if n1 < n2: msg = '莊家贏'
        data.append(msg)
        newdatas.append(data)
    return newdatas


if __name__ == '__main__':
    fn = 'D:\\test\\1060307.SM'
    datas = loadFile(fn)
    datas = checkCard(datas)
    showWindow(datas)

