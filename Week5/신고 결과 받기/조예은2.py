class User:
    def __init__(self, id) -> None:
        self.id = id  # 유저 아이디
        self.reported = list()  # 자신을 신고한 유저 아이디
        self.ban = False
        self.emailed = 0


class System:
    def __init__(self, id_list, ban_thres) -> None:
        self.users = {id: User(id) for id in id_list}
        self.ban_thres = ban_thres
        # self.ban_users = set()

    def reports(self, id1, id2):
        user2 = self.users[id2]
        if (not user2.ban):
            user2.reported.append(id1)
            
            if (len(user2.reported) == self.ban_thres):
                user2.ban = True
                # self.ban_users.add(id2)
                for id in user2.reported:
                    self.email(id)
        else:
            self.email(id1)
    
    def email(self, id):
        self.users[id].emailed += 1


def solution(id_list, report, k):
    system = System(id_list, k)
    
    for r in set(report):
        id1, id2 = r.split()
        system.reports(id1, id2)

    answer = [system.users[i].emailed for i in id_list]
    return answer