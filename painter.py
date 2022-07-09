from numpy import integer
import board as brd

class painter:
    
    def paint(paintable_board:brd.board_map, x_ccordinate:int, y_coordinate:int, point_style:str):
        paintable_board.map[y_coordinate][x_ccordinate] = point_style
