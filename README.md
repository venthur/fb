Dear reviewer,

There is a `Board` class that encapsulates the state of the board and provides
methods to colorize the board and counting the connected-to-origin, along with
some methods used internally to do the colorizing.

The board knows nothing about the number of available colors, that is up to the
overlaying game to decide.

I've started a game method that takes a board and a list of available colors and
starts to play the game according to your greedy algorithm. Unfortunately there
is still a bug in the coloring algorithm that causes an ininite loop. I've
recreated the steps and wrote a unit-test for that reproduces the bug
(`test_regresssion_infinite_loop`) but was unable to find and fix the bug due to
lack of time.

The other unittests test all the aspects of the board, at least one test is
missing: only the length of `get_neighbours` return value is tested, but not the
actual neighbours. This is also due to lack of time.

The code runs on Python 2.7 and has no requirements. To run the unittests just
run `nosetests` on the root directory.
