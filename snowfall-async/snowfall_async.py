# Alexander Holmes
# 9/27/22
# CRN: 10235
# CIS 226: Advanced Python Programming
# Total time it took to debug --- 45 seconds ---

import asyncio
import random

from kbhit import KBHit
import snowfall

NUM_COROUTINES = 2 # more coroutines means more snow
MAX_QUEUE_SIZE = 10 # Higher number means higher snow piles

stop_event = asyncio.Event()


async def run_game(queue_left, queue_right):
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
        await asyncio.sleep(0.1) # Let other coroutines run

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
                    queue_left.get_nowait()
                except asyncio.QueueEmpty:
                    pass
            else:
                # Remove from the queue if we can
                try:
                    queue_right.get_nowait()
                except asyncio.QueueEmpty:
                    pass

        # Increment animation index, and wrap around to 0
        shovel_animation_index += 1
        shovel_animation_index %= len(snowfall.SHOVEL)

    # Done with loop so mark done
    stop_event.set()


async def make_snow(queue_left, queue_right):
    """Separate coroutine that randomly adds snow to the left and right queues"""

    # Keep running until stop_event is triggered
    while not stop_event.is_set():
        if random.random() > 0.75:
            # Put something in the queue if there's room
            try:
                queue_left.put_nowait(1)
            except asyncio.QueueFull:
                pass

        if random.random() > 0.75:
            # Put something in the queue if there's room
            try:
                queue_right.put_nowait(1)
            except asyncio.QueueFull:
                pass

        await asyncio.sleep(0.2) # Let other coroutines run


async def main():
    """Main Function"""
    queue_left = asyncio.Queue(MAX_QUEUE_SIZE)
    queue_right = asyncio.Queue(MAX_QUEUE_SIZE)

    # Create a list of coroutines that will be started later
    coroutines = []
    for x in range(NUM_COROUTINES):
        coroutines.append(make_snow(queue_left, queue_right))

    # Run and wait for make_snow coroutines and run_game coroutine together
    await asyncio.gather(
        *coroutines, # The asterisk tells Python to "unpack" the list
        run_game(queue_left, queue_right),
    )


if __name__ == '__main__':
    try:
        # Start our event loop
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Goodbye')
