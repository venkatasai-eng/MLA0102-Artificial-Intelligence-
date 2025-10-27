import math

def evaluate(board):
    return board.count('A') - board.count('B')

def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0:
        return evaluate(board)
    if maximizing:
        max_eval = -math.inf
        for _ in range(2):
            eval = minimax(board, depth-1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for _ in range(2):
            eval = minimax(board, depth-1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

board = ['A','B','A','B','A','B','A','B']
print("Best Move Value:", minimax(board, 3, -math.inf, math.inf, True))