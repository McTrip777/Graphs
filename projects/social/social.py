import random

class Queue:
    def __init__(self):
        self.queue = []

# ---------------------------------------------------------------------------

    def enqueue(self, value):   
        self.queue.append(value)

# ---------------------------------------------------------------------------

    def dequeue(self):
        if (self.size()) > 0:
            return self.queue.pop(0)
        else:
            return None

# ---------------------------------------------------------------------------

    def size(self):
        return len(self.queue)

# ==========================================================================

class User:
    def __init__(self, name):
        self.name = name

# ==========================================================================

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

# ---------------------------------------------------------------------------

    def addFriendship(self, userID, friendID):
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

# ---------------------------------------------------------------------------

    def addUser(self, name):
        self.lastID += 1
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

# ---------------------------------------------------------------------------

    def populateGraph(self, numUsers, avgFriendships):
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        for i in range(0, numUsers):
            self.addUser(f"User {i}")
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID +1, self.lastID +1):
                possibleFriendships.append((userID, friendID))
        random.shuffle(possibleFriendships)
        for i in range(0, (numUsers * avgFriendships // 2)):
            friendship = possibleFriendships[i]
            self.addFriendship(friendship[0], friendship[1])

# ---------------------------------------------------------------------------

    def getAllSocialPaths(self, userID):
        visited = {}
        q = Queue()
        q.enqueue([userID])
        while q.size() > 0:
            path = q.dequeue()
            newUserID = path[-1]
            if newUserID not in visited:
                visited[newUserID] = path
                for friendID in self.friendships[newUserID]:
                    if friendID not in visited:
                        new_path = list(path)
                        new_path.append(friendID)
                        q.enqueue(new_path)
        return visited

# ---------------------------------------------------------------------------

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)




'''
                 1
               /  \
             10    2
            / \   / \
           9   7 3   6
                      \
                       8
'''