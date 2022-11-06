class Solution(object):
    def canVisitAllRooms(self, rooms):
        visit = [False for _ in range(len(rooms))]

        visit = self.visit_and_loot(rooms, visit, 0)

        for each in visit:
            if not each:
                return False

        return True

    def visit_and_loot(self, rooms, visit, room_num):
        if not visit[room_num]:
            visit[room_num] = True

            for i in range(len(rooms[room_num])):
                visit = self.visit_and_loot(rooms, visit, rooms[room_num][i])

        return visit

solution = Solution()
print(solution.canVisitAllRooms(rooms = [[1],[2],[3],[]]))
print(solution.canVisitAllRooms(rooms = [[1,3],[3,0,1],[2],[0]]))
