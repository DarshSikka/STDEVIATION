class dog():
    def __init__(self, color, hairstyle, breed):
        self.color=color
        self.hairstyle=hairstyle
        self.breed=breed
    def showcolor(self):
        print(self.color)
bruno=dog("red", "curly", "lebra")
bruno.showcolor()