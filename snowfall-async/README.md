Please fix the snowfall_async.py file. You should NOT edit any other file. The problems are with the async code, and not other logic.

# Requirements (all must be satisfied)

* No code has been copied from elsewhere
* Find and fix the following problems:
    * `queue_left` should not raise an error if full
    * `queue_right` should not raise an error if empty
* There are less problems to fix because the async version is so different from the others
* Here is how the final program should work once you've fixed the above:
    * No errors are raised
    * Player can move left and right with `a` and `d` keys
    * Two piles of snow should slowly appear on the left side of the screen
    * A pile should slowly decrease if the player is near it
    * Pressing Ctrl+C should end the program without an error
    * Pressing Escape should end the program without an error (sometimes have to press multiple times)
    * See below for example output
* `snowfall_async.py` has a header with your name, date, CRN, and class name
* Include total debugging time

## Example Output (bottom left of screen)

    |
    |                  ...|
    |         ===      0 /
    |         ===      /
    |         ===     / \
    +===================================
