import unittest
from TkinterDrawer import *
from MyParser import *
from MySourceReader import *
from TurtlePrompt import *
from GraphicsDrawer import *


class TestStringMethods(unittest.TestCase):

    def test_readerExists(self):
        reader = MySourceReader(MyParser(TurtleDrawer()))
        assert reader is not None

    def test_parserExists(self):
        reader = MySourceReader(MyParser(TurtleDrawer()))
        assert reader.parser is not None

    def test_turtleDrawerExists(self):
        reader = MySourceReader(MyParser(TurtleDrawer()))
        assert reader.parser.drawer is not None

    def test_tkinterDrawerExists(self):
        reader = MySourceReader(MyParser(TkinterDrawer()))
        assert reader.parser.drawer is not None

    def test_turtlePromptExists(self):
        reader = TurtlePrompt()
        assert reader is not None

    def test_graphicsDrawerExists(self):
        reader = MySourceReader(MyParser(GraphicsDrawer()))
        assert reader.parser.drawer is not None

    def test_graphicsDrawer_graphicsPropertyExists(self):
        reader = MySourceReader(MyParser(GraphicsDrawer()))
        assert reader.parser.drawer.graphics is not None

    def test_graphicsDrawer_xPropertyExists(self):
        reader = MySourceReader(MyParser(GraphicsDrawer()))
        assert reader.parser.drawer.x is not None

    def test_graphicsDrawer_yPropertyExists(self):
        reader = MySourceReader(MyParser(GraphicsDrawer()))
        assert reader.parser.drawer.y is not None

    def test_graphicsDrawer_penDownPropertyExists(self):
        reader = MySourceReader(MyParser(GraphicsDrawer()))
        assert reader.parser.drawer.penDown is not None

    def test_graphicsDrawer_colorPropertyExists(self):
        reader = MySourceReader(MyParser(GraphicsDrawer()))
        assert reader.parser.drawer.color is not None

    def test_graphicsDrawer_myDestPropertyExists(self):
        reader = MySourceReader(MyParser(GraphicsDrawer()))
        assert reader.parser.drawer.myDest is not None

    def test_graphicsDrawer_penlistPropertyExists(self):
        reader = MySourceReader(MyParser(GraphicsDrawer()))
        assert reader.parser.drawer.penlist is not None

    def test_graphicsDrawer_checkPropertyExists(self):
        reader = MySourceReader(MyParser(GraphicsDrawer()))
        assert reader.parser.drawer.check is not None

    def test_tkinterDrawer_topPropertyExists(self):
        reader = MySourceReader(MyParser(TkinterDrawer()))
        assert reader.parser.drawer.top is not None

    def test_tkinterDrawer_myCanvasPropertyExists(self):
        reader = MySourceReader(MyParser(TkinterDrawer()))
        assert reader.parser.drawer.myCanvas is not None

    def test_tkinterDrawer_colorPropertyExists(self):
        reader = MySourceReader(MyParser(TkinterDrawer()))
        assert reader.parser.drawer.color is not None

    def test_tkinterDrawer_penDownPropertyExists(self):
        reader = MySourceReader(MyParser(TkinterDrawer()))
        assert reader.parser.drawer.penDown is not None

    def test_tkinterDrawer_xPropertyExists(self):
        reader = MySourceReader(MyParser(TkinterDrawer()))
        assert reader.parser.drawer.x is not None

    def test_tkinterDrawer_yPropertyExists(self):
        reader = MySourceReader(MyParser(TkinterDrawer()))
        assert reader.parser.drawer.y is not None

    def test_tkinterDrawer_myDestPropertyExists(self):
        reader = MySourceReader(MyParser(TkinterDrawer()))
        assert reader.parser.drawer.myDest is not None

    def test_tkinterDrawer_penlistPropertyExists(self):
        reader = MySourceReader(MyParser(TkinterDrawer()))
        assert reader.parser.drawer.penlist is not None

    def test_tkinterDrawer_checkPropertyExists(self):
        reader = MySourceReader(MyParser(TkinterDrawer()))
        assert reader.parser.drawer.check is not None

    def test_turtleDrawer_penlistPropertyExists(self):
        reader = MySourceReader(MyParser(TurtleDrawer()))
        assert reader.parser.drawer.penlist is not None

    def test_turtleDrawer_turtlePropertyExists(self):
        reader = MySourceReader(MyParser(TurtleDrawer()))
        assert reader.parser.drawer.turtle is not None

    def test_turtleDrawer_checkPropertyExists(self):
        reader = MySourceReader(MyParser(TurtleDrawer()))
        assert reader.parser.drawer.check is not None

    def test_turtlePrompt_aliasPropertyExists(self):
        reader = TurtlePrompt()
        assert reader.alias is not None

    def test_graphicsDrawer_canSelectPens(self):
        reader = MySourceReader(MyParser(GraphicsDrawer()))
        reader.parser.drawer.select_pen(1)
        self.assertEqual(reader.parser.drawer.color, "white")

    def test_tkinterDrawer_canSelectPens(self):
        reader = MySourceReader(MyParser(TkinterDrawer()))
        reader.parser.drawer.select_pen(1)
        self.assertEqual(reader.parser.drawer.color, "white")

    def test_turtleDrawer_canSelectPens(self):
        reader = MySourceReader(MyParser(TurtleDrawer()))
        reader.parser.drawer.select_pen(1)
        self.assertEqual(reader.parser.drawer.turtle.pencolor(), "white")

    def test_graphicsDrawer_penIsDown(self):
        reader = MySourceReader(MyParser(GraphicsDrawer()))
        reader.parser.drawer.pen_down()
        self.assertTrue(reader.parser.drawer.penDown)

    def test_graphicsDrawer_penIsUp(self):
        reader = MySourceReader(MyParser(GraphicsDrawer()))
        reader.parser.drawer.pen_up()
        self.assertFalse(reader.parser.drawer.penDown)

    def test_tkinterDrawer_penIsDown(self):
        reader = MySourceReader(MyParser(TkinterDrawer()))
        reader.parser.drawer.pen_down()
        self.assertTrue(reader.parser.drawer.penDown)

    def test_tkinterDrawer_penIsUp(self):
        reader = MySourceReader(MyParser(TkinterDrawer()))
        reader.parser.drawer.pen_up()
        self.assertFalse(reader.parser.drawer.penDown)

    def test_turtleDrawer_penIsDown(self):
        reader = MySourceReader(MyParser(TurtleDrawer()))
        reader.parser.drawer.pen_down()
        self.assertTrue(reader.parser.drawer.turtle.isdown())

    def test_turtleDrawer_penIsUp(self):
        reader = MySourceReader(MyParser(TurtleDrawer()))
        reader.parser.drawer.pen_up()
        self.assertFalse(reader.parser.drawer.turtle.isdown())

    def test_graphicsDrawer_goAlong(self):
        reader = MySourceReader(MyParser(GraphicsDrawer()))
        reader.parser.drawer.go_along(300)
        self.assertEqual(reader.parser.drawer.x, 300)

    def test_graphicsDrawer_goDown(self):
        reader = MySourceReader(MyParser(GraphicsDrawer()))
        reader.parser.drawer.go_down(300)
        self.assertEqual(reader.parser.drawer.y, 300)

    def test_tkinterDrawer_goAlong(self):
        reader = MySourceReader(MyParser(TkinterDrawer()))
        reader.parser.drawer.go_along(300)
        self.assertEqual(reader.parser.drawer.x, 300)

    def test_tkinterDrawer_goDown(self):
        reader = MySourceReader(MyParser(TkinterDrawer()))
        reader.parser.drawer.go_down(300)
        self.assertEqual(reader.parser.drawer.y, 300)

    def test_turtleDrawer_goAlong(self):
        reader = MySourceReader(MyParser(TurtleDrawer()))
        reader.parser.drawer.go_along(300)
        self.assertEqual(reader.parser.drawer.turtle.xcor(), 300)

    def test_turtleDrawer_goDown(self):
        reader = MySourceReader(MyParser(TurtleDrawer()))
        reader.parser.drawer.go_down(300)
        self.assertEqual(reader.parser.drawer.turtle.ycor(), 300)

if __name__ == '__main__':
    unittest.main()
