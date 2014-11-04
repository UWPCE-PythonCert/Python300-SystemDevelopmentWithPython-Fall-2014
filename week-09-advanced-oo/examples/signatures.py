class Shape(object):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super(Shape, self).__init__(**kwds)

class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super(ColoredShape, self).__init__(**kwds)

cs = ColoredShape(color='red', shapename='circle')
