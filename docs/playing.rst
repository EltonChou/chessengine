.. _playing_a_game:

Playing A Game
==============

.. note::

    The current version of chessengine has not yet implemented all rules of
    chess. A few move-related bugs are also known and under development.

    * King moves -
        * Moves generated by other pieces are not checked to make sure they do not place the king in check
        * The king generates moves that move it into check
        * The king isn't required to move itself out of check
    * Pawn promotion -
        * Pawns are not promoted when they reach the last rank
    * Stalemate -
        * The engine still asks for a move if the user is stalemated
        * If the engine is stalemated, it crashes
    * SAN input by user is not verified for correctness -
        * SAN moves that are ambiguous are accepted as valid, and a piece is chosen by the engine
        * SAN moves that are invalid throw an error instead of giving the user a chance to enter the move again
    * Castling -
        * Castling is accepted after the rook has moved
        * Castling is accepted after the king has moved
    * En-passant moves -
        * The engine does not make en-passant moves
        * The engine does not allow the user to make en-passant moves

The recommended way to play a game on the console is by using the command -

.. code-block:: console

    $ chessengine play

You can also invoke chessengine from python by running -

.. code-block:: console

    $ python -m chessengine.play

Use the ``-p`` flag to play against another player instead of the computer -

.. code-block:: console

    $ chessengine play -p

If playing against the computer, chessengine will prompt you to pick the side you
want to play - black or white. Enter "w" for white and "b" for black. The computer
will parse PGN files included in the package to search for opening moves, and the
game will start.

.. _move_representation:

Making Moves On The Board
-------------------------

You can make moves by entering the Standard Algebraic Notation (SAN) of the move
as the input. SAN is the standard method of recording moves in chess games. Note
that the SAN you enter must be valid given the current state of the chessboard.

If you are not familiar with SAN, you can also make moves by describing the start
square and the end square for the move in the following format -

``"<start_square> to <end_square>"``

Where ``<start_square>`` and ``<end_square>`` are given as coordinates on the
chessboard. For example, ``b1 to c3``. This will move the piece on square ``b1``
to the square ``c3``.