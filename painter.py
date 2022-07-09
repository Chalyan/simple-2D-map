from numpy import integer
import board as brd

class painter:
    
    def paint(paintable_board:brd.board_map, x_ccordinate:int, y_coordinate:int, point_style):
        paintable_board.map[x_ccordinate][y_coordinate] = point_style
