class Node:
    def __init__(self):
        self.chils = dict()
        self.word = None

    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.chils:
                curr.chils[c] = Node()
            curr = curr.chils[c]
        curr.word = word


class Solution:
    steps = ((-1, 0), (0, 1), (1, 0), (0, -1))

    def _dfs(self, i, j, N, M, board, visited, node, answer):
        if node.word:
            answer.add(node.word)

        if not 0 <= i < N or not 0 <= j < M or visited[i][j]:
            return

        visited[i][j] = True

        if board[i][j] in node.chils:
            for di, dj in Solution.steps:
                ni, nj = i + di, j + dj
                self._dfs(ni, nj, N, M, board, visited, node.chils[board[i][j]], answer)

        visited[i][j] = False

    def findWords(self, board, words):
        if not board or not words:
            return list()

        trie = Node()
        for word in words:
            trie.insert(word)

        N, M = len(board), len(board[0])
        visited = [[False] * M for _ in range(N)]
        result = set()
        for i in range(N):
            for j in range(M):
                self._dfs(i, j, N, M, board, visited, trie, result)
        return list(result)


if __name__ == "__main__":
    board = [
      ['o', 'a', 'a', 'n'],
      ['e', 't', 'a', 'e'],
      ['i', 'h', 'k', 'r'],
      ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]

    print(Solution().findWords(board, words))