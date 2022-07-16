class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = set()
        for i in range(n):
            players.add(i+1)
        #print(list(dict.fromkeys(players)))
        player = 0
        count = k
        while len(players) > 1:            
            player += 1
            if player != n:
                player = player % n
            if count == 1:
                if player in players:
                    print("removing player: {}".format(player))
                    players.remove(player)
                    count = k                    
                continue
            if player in players:
                print("here")
                count-=1
        
        return players.pop()