from tkinter import *
import pyscreenshot
from tkinter import colorchooser

class Paint:

    def __init__(self):

        self.window = Tk()
        self.window.title('PainTk')
        self.window.geometry('1260x600')
        #self.window.minsize(width=1260, height=400)
        self.window.resizable(0, 0)

        self.oval_brush = False
        self.line_brush = False
        self.eraser_brush = False

        self.img_line = PhotoImage(file='icons/line.png')#chamando img para a aplicação
        self.img_oval = PhotoImage(file='icons/oval.png')
        self.img_eraser = PhotoImage(file='icons/eraser.png')
        self.img_save = PhotoImage(file='icons/save.png')
        self.img_square = PhotoImage(file='icons/square.png')
        self.img_new = PhotoImage(file='icons/new.png')

        self.colors = ('black', 'gray', 'white', 'red', 'green', 'blue', 'purple', 'orange', 'VioletRed4', 'aquamarine')

        self.pick_colors = 'black'

        self.barra_menu = Frame(self.window, bg='#3b3b3b', height=50)
        self.barra_menu.pack(fill='x') #Fill serve para preencher toda a tela na horizontal

        self.cor_texto = Label(self.barra_menu, text='  Cor:  ', fg='white', bg='#3b3b3b')
        self.cor_texto.pack(side='left')# Posiciona a esquerda

        for i in self.colors:# Modo de fazer varios botoes de uma forma mais simples
            self.botao_cor = Button(self.barra_menu, bg=i, width=4, height=2,command= lambda col=i :self.selecao_cor(col)).pack(side='left')

        self.label_colors_choose = Label(self.barra_menu, text='  Color Choose:  ', fg='white', bg='#3b3b3b')
        self.label_colors_choose.pack(side='left')
        self.color_choose = Button(self.barra_menu, image=self.img_square, bd=0, command=self.selecionar_cor)
        self.color_choose.pack(side='left')

        self.text_pen_size = Label(self.barra_menu, text=' Size:  ', fg='white', bg='#3b3b3b').pack(side='left')

        self.pen_size = Spinbox(self.barra_menu, from_=1, to=50)
        self.pen_size.pack(side='left')

        #self.botao_cor = Button(self.barra_menu, bg='black', width=4, height=1,command=None).pack(side='left')
        #Outro metodo de usar o .pack

        self.text_brushs = Label(self.barra_menu, text='  Brushs:  ', fg='white', bg='#3b3b3b').pack(side='left')

        self.button_line =  Button(self.barra_menu, image=self.img_line, bd=0,command=self.brush_line).pack(side='left')
        self.button_oval = Button(self.barra_menu, image=self.img_oval, bd=0,command=self.brush_oval).pack(side='left')

        self.button_eraser = Button(self.barra_menu, image=self.img_eraser, bd=0, command=self.brush_eraser).pack(side='left')

        self.opcao_texto = Label(self.barra_menu,text='  Options:  ', fg='white', bg='#3b3b3b').pack(side='left')
        self.button_save = Button(self.barra_menu, image=self.img_save, bd=0, command=self.save).pack(side='left')
        self.button_new = Button(self.barra_menu, image=self.img_new, bd=0,command=self.clear).pack(side='left')

        self.area_desenho = Canvas(self.window, height=720,bg='white')
        self.area_desenho.pack(fill='both') #Fill com a config de both preenche toda a tela
        self.area_desenho.bind('<B1-Motion>', self.desenho)#Bind chama um evento especifico

        self.window.bind('<F1>', self.clear)
        self.window.bind('<F2>', self.save)

        self.window.mainloop()

    def desenho(self, event):

        x1, y1 = (event.x), (event.y)
        x2, y2 = (event.x), (event.y)


        if self.oval_brush:
            self.area_desenho.create_oval(x1, y1, x2, y2, fill=self.pick_colors,
                                          outline=self.pick_colors, width=self.pen_size.get())
        elif self.line_brush:
            self.area_desenho.create_line(x1-10, y1-10, x2, y2, fill=self.pick_colors, width=self.pen_size.get())
        else:
            self.area_desenho.create_oval(x1, y1, x2, y2, fill=self.pick_colors,
                                          outline='white', width=self.pen_size.get())

    def selecao_cor(self, col):
        self.pick_colors = col
    def brush_oval(self):
        self.oval_brush = True
        self.line_brush = False
        self.eraser_brush = False
    def brush_line(self):
        self.oval_brush = False
        self.line_brush = True
        self.eraser_brush = False
    def brush_eraser(self):
        self.oval_brush = False
        self.line_brush = False
        self.eraser_brush = True
    def clear(self, event):
        self.area_desenho.delete('all')
    def save(self, event):
        x = self.window.winfo_rootx() + self.area_desenho.winfo_x()
        y = self.window.winfo_rooty() + self.area_desenho.winfo_y()
        x1= self.window.winfo_rootx() + self.area_desenho.winfo_width()
        y1= self.window.winfo_rooty() + self.area_desenho.winfo_height()

        img = pyscreenshot.grab(bbox=(x,y,x1,y1))
        img.save('image.png', 'png')

    def selecionar_cor(self):
        colors = colorchooser.askcolor()
        self.pick_colors = colors[1]


Paint()
