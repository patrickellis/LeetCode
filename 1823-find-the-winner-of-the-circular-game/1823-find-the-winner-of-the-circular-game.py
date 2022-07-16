class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = set()
        for i in range(n):
            players.add(i+1)
        player = 0
        count = k
        while len(players) > 1:            
            player += 1
            if player != n:
                player = player % n
            if count == 1:
                if player in players:
                    players.remove(player)
                    count = k                    
                continue
            if player in players:
                count-=1
        
        return players.pop()