class Robot:
    def __init__(self, X, Y):
        self.X, self.Y = X, Y
        self.cordinates = [[self.X, self.Y]]
        self.start = [self.X, self.Y]

    def move(self, way):
        if way:
            for char in way:
                if char == 'N':
                    self.X += 1
                    self.cordinates.append([self.X, self.Y])
                elif char == 'S':
                    self.X -= 1
                    self.cordinates.append([self.X, self.Y])
                elif char == 'E':
                    self.Y += 1
                    self.cordinates.append([self.X, self.Y])
                elif char == 'W':
                    self.Y -= 1
                    self.cordinates.append([self.X, self.Y])
            return self.cordinates[-1]
        else:
            return False

    def path(self, way):
        if self.move(way):
            return self.cordinates
        else:
            return self.start
