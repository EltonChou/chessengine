from .lookup_tables import mask_position


class Board:
    """
    A class representing a bitboard representation of the chess board
    """

    def __init__(self, side: str):
        self.white_pawns = 65280  # 1111111100000000 in binary (A2 to H2)
        self.white_rooks = 129  # 10000001 in binary (A1 and H1)
        self.white_knights = 66  # 01000010 in binary (B1 and G1)
        self.white_bishops = 36  # 00100100 in binary (C1 and F1)
        self.white_queen = 16  # 00010000 in binary (D1)
        self.white_king = 8  # 00001000 in binary (E1)
        # TODO - Fill in these positions
        self.black_pawns = 0  # (A7 to H7)
        self.black_rooks = 0  # (A8 and H8)
        self.black_knights = 0  # (B8 and G8)
        self.black_bishops = 0  # (C8 and F8)
        self.black_queen = 0  # (D8)
        self.black_king = 0  # (E8)

        self.all_white = (
            self.white_pawns
            | self.white_rooks
            | self.white_knights
            | self.white_bishops
            | self.white_queen
            | self.white_king
        )

        self.all_black = (
            self.black_pawns
            | self.black_rooks
            | self.black_knights
            | self.black_bishops
            | self.black_queen
            | self.black_king
        )

        self.all_pieces = self.all_black | self.all_white
        self.side = side.lower().strip()
        
        # A dictionary matching a side and piece to its corresponding bit board.
        # Useful when we want to iterate through all of the bitboards of the board.
        self.boards_table = {
            ('white', 'king'): self.white_king,
            ('white', 'queen'): self.white_queen,
            ('white', 'rook'): self.white_rooks,
            ('white', 'bishop'): self.white_bishops,
            ('white', 'knight'): self.white_knights,
            ('white', 'pawns'): self.white_pawns,
            ('black', 'king'): self.black_king,
            ('black', 'queen'): self.black_queen,
            ('black', 'rook'): self.black_rooks,
            ('black', 'bishop'): self.black_bishops,
            ('black', 'knight'): self.black_knights,
            ('black', 'pawns'): self.black_pawns,
        }

    def get_piece_bitboard(self, side: str, piece: str):
        """
        Returns the bitboard of the passed side for the passed pieces.
        Calling with side="black" and piece="king" will return the black_king bitboard
        """
        piece = piece.lower().strip()
        if piece not in {
            "king",
            "queen",
            "bishop",
            "knight",
            "rook",
            "pawn",
        }:
            raise ValueError(
                f"get_piece_bitboard got unknown piece.\nExpected one of {{'king', 'queen', 'bishop', 'knight', "
                f"'rook', 'pawn'}}, got {piece} instead."
            )
        if side not in {"black", "white"}:
            raise ValueError(
                f"get_piece_bitboard got unknown piece.\nExpected one of {{'white', 'black'}}, "
                f"got {side} instead."
            )
        attrname = side + '_' + piece
        if piece not in {"king", "queen"}:
            attrname += 's'
        return getattr(self, attrname)
    
    def get_self_piece_bitboard(self, piece: str):
        """
        Returns the attribute corresponding to the passed piece, considering the board's
        own side. i.e. - If the board is white, calling with piece = 'king' will return
        white king, etc.
        piece can be one of - "king", "queen", "bishop", "knight", "rook", "pawn"
        """
        return self.get_piece_bitboard(side=self.side, piece=piece)
    
    def identify_piece_at(self, position: str):
        mask = mask_position[position]
        for side, piece in self.boards_table:
            board = self.boards_table[(side, piece)]
            if board & mask > 0:
                return side, piece, board
        return None     # explicit > implicit

    def move(self, start: int, to: int, piece_bitboard=None):
        """
        
        """
