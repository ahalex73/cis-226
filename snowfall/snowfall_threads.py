# Alexander Holmes
# 11/29/22
# CRN: 10235
# CIS 226: Advanced Python Programming
# Total time it took to debug --- 45 minutes ---

import queue
import random
import threading
import time

from kbhit import KBHit
import snowfall

NUM_THREADS = 1 # more threads means more snow
MAX_QUEUE_SIZE = 15 # Higher number means higher snow piles

stop_event = threading.Event()                              # Bug fixed


def run_game(queue_left, queue_right):
    """Run the game loop"""
    kb = KBHit()
    buffer = snowfall.CharacterBuffer()
    shovel_animation_index = 0
    x = 2
    left_size = 0
    right_size = 0
    while True:
        animation = snowfall.SHOVEL[shovel_animation_index]
        buffer.reset()
        buffer.add_borders()
        buffer.draw(animation, x, buffer.height - 6)

        # Draw snow piles based on length in queues
        left_size = queue_left.qsize()
        right_size = queue_right.qsize()
        if left_size > 0:
            buffer.draw('===\n' * left_size, 10, buffer.height - left_size)
        if right_size > 0:
            buffer.draw('===\n' * right_size, 20, buffer.height - right_size)

        buffer.print()
        time.sleep(0.1)

        if kb.kbhit():
            c = kb.getch()
            if ord(c) == 27: # ESC
                break

            # WASD Controls
            if c == 'a':
                x -= 2
            elif c== 'd':
                x += 2

            # Swallow up remaining keypresses so there isn't a delay
            while kb.kbhit():
                kb.getch()

        # Keep animation in bounds
        if x < 1:
            x = 1
        elif x > buffer.width - 7:
            x = buffer.width - 7

        if random.random() > 0.5:
            if x < 15:
                # Remove from the queue if we can
                try:
                    queue_left.get(block=False)             # Bug Fixed
                except queue.Empty:
                    pass
            else:
                # Remove from the queue if we can
                try:
                    queue_right.get(block=False)
                except queue.Empty:
                    pass

        # Increment animation index, and wrap around to 0
        shovel_animation_index += 1
        shovel_animation_index %= len(snowfall.SHOVEL)


def make_snow(queue_left, queue_right):
    """Threaded process that randomly adds snow to the left and right queues"""

    # Keep running until stop_event is triggered
    while not stop_event.is_set():
        if random.random() > 0.75:
            # Put something in the queue if there's room
            try:
                queue_left.put(1, block=False)
            except queue.Full:                              # Bug Fixed
                pass

        if random.random() < 0.75:
            # Put something in the queue if there's room
            try:
                queue_right.put(1, block=False)
            except queue.Full:
                pass

        time.sleep(0.2)


def main():
    """Main Function"""
    queue_left = queue.Queue(MAX_QUEUE_SIZE)
    queue_right = queue.Queue(MAX_QUEUE_SIZE)

    # Create threads with the arguments queue_left and queue_right
    threads = [threading.Thread(target=make_snow, args=(queue_left, queue_right)) for x in range(NUM_THREADS)]
    # Start all the threads
    for thread in threads:
        thread.start()                                      # Bug fixed 

    try:
        run_game(queue_left, queue_right)
    except KeyboardInterrupt:
        print('Goodbye')

    # Game is done so tell threads to stop
    stop_event.set()
    # Wait until each thread stops
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
