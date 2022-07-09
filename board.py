class board_map:
    
    def __init__(self, x:int, y:int):
        self.map = [['-' for x in range(x)] for y in range(y)]
        
    def show_map(self,file_name: str):
        file = open(file_name, "w")
        for row in range (len(self.map)):
            for column in range (len(self.map[row])):
                file.write(self.map[row][column])
            file.write('\n')
        file.close()
