from PIL import Image, ImageDraw

#test commit from nout
class Drawer:
    def __init__(self, draw_map, cell_size):
        self.m = []
        for i in draw_map:
            for p in i:
                self.m += [p]
        self.mapd = draw_map[:][:]
        self.cell_size = cell_size

    def numbers(self):
        itog = sorted(list(set(self.m)))
        if isinstance(itog, tuple):
            return reversed(itog)
        return sorted(list(set(self.m)))

    def set_color(self, number, color):
        for i in range(len(self.mapd)):
            for p in range(len(self.mapd[i])):
                tek = i * len(self.mapd[i]) + p
                if tek == number - 1:
                    self.mapd[i][p] = color
                    return None

    def set_cell_size(self, cell_size):
        self.cell_size = cell_size

    def size(self):
        itog = self.cell_size * len(self.mapd), int(self.cell_size) * len(self.mapd[0])
        return itog

    def draw(self):
        im = Image.new("RGB", (self.cell_size * len(self.mapd), self.cell_size * len(self.mapd[0])))
        drawer = ImageDraw.Draw(im)
        for i in range(len(self.mapd)):
            for p in range(len(self.mapd[i])):
                if isinstance(self.mapd[i][p], int):
                    drawer.rectangle(((p * self.cell_size, i * self.cell_size),
                                      (self.cell_size + p * self.cell_size,
                                       self.cell_size * i + self.cell_size)), 'black')
                else:
                    drawer.rectangle(((p * self.cell_size, i * self.cell_size),
                                     (self.cell_size + p * self.cell_size,
                                     self.cell_size * i + self.cell_size)), self.mapd[i][p])

        return im

dr = Drawer([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 20)
dr.set_color(1, 'black')
dr.set_color(2, 'red')
dr.set_color(3, 'orange')
dr.set_color(4, 'yellow')
dr.set_color(5, 'green')
dr.set_color(6, 'lightblue')
dr.set_color(7, 'blue')
dr.set_color(8, 'violet')
dr.set_color(9, 'white')
print(dr.numbers())

dr.draw()