class paper:
    '''
    Paper with complete map

    Parameters:
    meta: (object) map meta data
    '''

    def __init__(self, metadata):
        from random import randint
        self.meta = meta(metadata=metadata)
        self.map = []
        self.status = 1

        for i1 in range(self.meta.height):
            self.map.append([])
            for i2 in range(self.meta.width):
                self.map[i1].append(plot())

        self.starting_area = []

        for empty_plot in self.meta.empty_plots:
            for position in self.meta.start_zone:
                selected_plot = [empty_plot[0] + position[0], empty_plot[1] + position[1]]
                if(not selected_plot in self.starting_area):
                    self.map[selected_plot[0]][selected_plot[1]].open = True
                    self.starting_area.append(selected_plot)

        i = 0

        while(i < self.meta.mine_count):
            x = randint(0, self.meta.height -1)
            y = randint(0, self.meta.width -1)

            if(self.__emptyPlot__(x, y) == False):
                continue

            selected_plot = self.map[x][y]

            if(selected_plot.mine == False):
                selected_plot.mine = True

                self.__mineCounter__(x, y)

                i += 1

        self.updateOpenPlots()

    def __mineCounter__(self, x, y):
        effect_zone = self.meta.effect_zone

        for position in effect_zone:
            selected_plot_y = y + position[1]
            selected_plot_x = x + position[0]

            if(self.__insideBorders__(selected_plot_x, selected_plot_y)):
                selected_plot = self.map[selected_plot_x][selected_plot_y]

                if(selected_plot.strength == None):
                    selected_plot.strength = 0

                selected_plot.strength = selected_plot.strength + 1

    def __emptyPlot__(self, x, y):
        if([x, y] in self.starting_area):
            return False
        return True

    def __insideBorders__(self, x, y):
        return (
                y > -1 and
                y < self.meta.width and
                x > -1 and
                x < self.meta.height
            )

    def updateOpenPlots(self):
        for row in self.map:
            for selected_plot in row:
                selected_x = self.map.index(row)
                selected_y = row.index(selected_plot)

                if(self.map[selected_x][selected_y].open):
                    self.openPlot(selected_x, selected_y)

    def openPlot(self, x, y):
        selected_plot = self.map[x][y]
        selected_plot.open = True

        if(selected_plot.mine == True):
            self.status = 0

        if(selected_plot.strength == 0 or selected_plot.strength == None):
            for position in self.meta.effect_zone:
                if(
                    self.__insideBorders__(x + position[0], y + position[1]) and
                    self.map[x + position[0]][y + position[1]].open == False
                ):
                    self.openPlot(x + position[0], y + position[1])

        for position in self.meta.effect_zone:
            if(self.__insideBorders__(x + position[0], y + position[1])):
                effect_plot = self.map[x + position[0]][y + position[1]]

                if((effect_plot.strength == None or effect_plot.strength == 0) and effect_plot.open == False):
                    self.openPlot(x + position[0], y + position[1])


class meta:
    '''
    Map metadata

    Parameters
    '''
    def __init__(self, metadata):
        self.width = metadata['width']
        self.height = metadata['height']
        self.effect_zone = metadata['effect_zone']
        self.mine_count = metadata['mine_count']
        self.empty_plots = metadata['empty_plots']
        self.start_zone = metadata['start_zone']


class plot:
    '''
    Plot of an row of the paper
    '''

    def __init__(self, color = "fff", mine = False, strength = None):
        self.color = color
        self.mine = mine
        self.strength = strength
        self.open = False