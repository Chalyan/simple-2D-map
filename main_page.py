import board as brd
import painter as pnt

current_board = brd.board_map(20,8)
x_ccordinate = int(input("Enter x coordinate: "))
y_ccordinate = int(input("Enter y coordinate: "))
pnt.painter.paint(current_board, x_ccordinate, y_ccordinate, "X")
current_board.show_map("file.txt")
