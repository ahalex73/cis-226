Please fix the snowfall_threads.py file. You should NOT edit any other file. The problems are with the threading code, and not other logic.

# Requirements

* No code has been copied from elsewhere
    * (Do not copy the first result for Python Database in Google)


* Find and fix the following problems:
    		* `stop_event` is not created correctly
    		* `queue_left` should not raise an error if empty
    		* `queue_right` should not raise an error if full
    		* Fix how the threads are started
    		* Ensure the correct arguments are passed to `run_game`


* Here is how the final program should work once you've fixed the above:
    * No errors are raised
    * Player can move left and right with `a` and `d` keys
    * Two piles of snow should slowly appear on the left side of the screen
    * A pile should slowly decrease if the player is near it
    * Pressing Ctrl+C should end the program without an error
    * Pressing Escape should end the program without an error (sometimes have to press multiple times)
    * See below for example output
* `snowfall_threads.py` has a header with your name, date, CRN, and class name
* Include total debugging time

## Example Output (bottom left of screen)

    |
    |                  ...|
    |         ===      0 /
    |         ===      /
    |         ===     / \
    +===================================
