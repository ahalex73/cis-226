import shutil


SHOVEL = [
r'''

 0
 |\
/ \\-/
''',
r'''

 0
 |\==/
/ \
''',
r'''

 0 ==/
 |/``
/ \
''',
r'''
 ...|
 0 /
 |/
/ \
''',
]


def clear_terminal():
    """Clear all text on the terminal"""
    # From https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    print("\033c\033[3J\033[2J\033[0m\033[H", end='')


class CharacterBuffer:
    """Manage an array of text that can be printed to fill the terminal"""
    def __init__(self):
        self._buffer = []
        self.height = 0
        self.width = 0
        self.reset()

    def reset(self):
        """Clear the buffer, to all spaces"""
        size = shutil.get_terminal_size()
        self._buffer = []
        for _ in range(size.lines):
            row = [' '] * (size.columns - 1)
            self._buffer.append(row)
        self.height = len(self._buffer)
        self.width = len(self._buffer[0])
        return self._buffer

    def add_borders(self):
        """Add a border of + and = around the edge of the buffer"""
        self._buffer[0] = list('+' + ('=' * (len(self._buffer[0]) - 2)) + '+')
        for y in range(1, len(self._buffer) - 1):
            self._buffer[y][0] = '|'
            self._buffer[y][-1] = '|'
        self._buffer[-1] = self._buffer[0][:] # Copy top line

    def draw(self, text, x, y):
        """Insert given text into x and y offset in buffer"""
        for line in text.splitlines():
            new_x = x
            for char in line:
                self._buffer[y][new_x] = char
                new_x += 1
            y += 1

    def print(self):
        """Print the buffer to the screen"""
        length = len(self._buffer)
        text = ''
        for i, row in enumerate(self._buffer):
            end = ''
            if i < length - 1:
                end = '\n'
            text += ''.join(row) + end
        clear_terminal()
        print(text, end='', flush=True)
