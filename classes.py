class Kerdesek:
    def __init__(self, list):
        data = list.split(";")
        self.question = data[0]
        self.answer1 = data[1]
        self.answer2 = data[2]
        self.answer3 = data[3]
        self.point1 = int(data[4])
        self.point2 = int(data[5])
        self.point3 = int(data[6])



