import os
import pew
import supervisor
import board
import displayio
import terminalio


def _wait_keys():
    try:
        while True:
            keys = pew.keys()
            if keys:
                break
        for i in range(5):
            if not pew.keys():
                break
            pew.tick(0.0625)
        else:
            keys = pew.keys()
    except pew.GameOver:
        keys = 0
    return keys


class Menu:
    def __init__(self):
        grid = board.DISPLAY.root_group[0]
        grid = displayio.TileGrid(grid.bitmap, pixel_shader=grid.pixel_shader,
            tile_width = grid.tile_width, tile_height=grid.tile_height,
            width = 12, height = 6)
        terminal_group = displayio.Group()
        terminal_group.scale = 2
        terminal_group.append(grid)
        self.screen = displayio.Group()
        self.screen.append(terminal_group)
        bitmap = displayio.Bitmap(16, 10, 2)
        i = 0
        for byte in b'7\xf8(\x84"D*x$P$\xf0+\x10!\xf0* 7\xc0':
            for bit in range(8):
                bitmap[i] = byte & 0x80 != 0
                byte <<= 1
                i += 1
        palette = displayio.Palette(2)
        palette[0] = 0x0000
        palette[1] = 0xffff
        self.cursor = displayio.TileGrid(bitmap, pixel_shader=palette, x=0)
        self.screen.append(self.cursor)
        self.terminal = terminalio.Terminal(grid, terminalio.FONT)

    def select(self, items):
        self.terminal.write("\x1b[2J")
        for item in items[:6]:
            self.terminal.write("  %s\r\n" % item[:10])
        selected = 0
        total = min(6, len(items)) - 1
        while True:
            self.cursor.y = selected * 12 + 3
            pew.tick(0.125)
            keys = _wait_keys()
            if keys & pew.K_UP and selected > 0:
                selected -= 1
            if keys & pew.K_DOWN and selected < total:
                selected += 1
            if keys & pew.K_O:
                return items[selected]

pew.init()
menu = Menu()
board.DISPLAY.show(menu.screen)
files = [name[:-3] for name in os.listdir()
         if name.endswith('.py') and name != 'main.py']
game = menu.select(files)
supervisor.set_next_code_file("%s.py" % game, reload_on_success=True)
supervisor.reload()
