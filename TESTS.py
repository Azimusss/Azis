class Block:
    def __init__(self, coords, width, height, color):
        self.x = coords[0]
        self.y = coords[1]
        self.width = width
        self.height = height
        self.color = color

    def get_area(self):
        """
        Метод возвращает площадь данного блока
        """
        return self.width*self.height

    def set_width(self, new_width):
        if type(new_width) is not int:    # Если тип не int
            print("Error: Попытка задать некорректный тип свойства width")
            return -1
        elif new_width < 0:
            print("Error: Попытка задать отритцательное зачение свойства widht")
        else:
            self.width = new_width


redSmallBlock = Block((20, 40), 20, 10, "red")
blueBigBlock = Block((60, 10), 120, 100, "blue")


print("Ширина красного блока = ", redSmallBlock.width)
print("Координата х синего блока = ", blueBigBlock.x)

redSmallBlock.width = 40
blueBigBlock.x = -20

print("Площадь красного блока = ",redSmallBlock.width*redSmallBlock.height)
print("Площадь синего блока = ",blueBigBlock.width*blueBigBlock.height)
print(redSmallBlock)