

class Item:
    def __init__(self, w=0, p=0):
        self.weight = w
        self.price = p

if __name__ == "__main__":
    items = [
        Item(300, 400),
        Item(500, 250),
        Item(200, 980),
        Item(600, 340),
        Item(900, 670),
        Item(1360, 780),
        Item(800, 570),
        Item(250, 800)
    ]
    print(items[3].weight)

