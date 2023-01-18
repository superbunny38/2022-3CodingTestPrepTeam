class User:
    def __init__(self, id) -> None:
        self.id = id  # 유저 아이디
        self.reported = list()  # 자신을 신고한 유저 아이디
        self.ban = False  # 밴 당했는지 여부
        self.emailed = 0  # 이메일 받은 횟수


class System:
    def __init__(self, id_list, ban_thres) -> None:
        self.users = {id: User(id) for id in id_list}  # 이 시스템을 이용하는 유저들
        self.ban_thres = ban_thres  # k와 같다. ban threshold 이상 신고 받았을 시 밴
        # self.ban_users = set()

    def reports(self, id1, id2):  # 신고 기능
        user2 = self.users[id2]
        if (not user2.ban):  # 밴 당하지 않았으면
            user2.reported.append(id1)  # 신고 한 유저 아이디 추가
            
            if (len(user2.reported) == self.ban_thres):  # threshold에 도달했을 시
                user2.ban = True  # 밴
                # self.ban_users.add(id2)
                for id in user2.reported:  # 지금까지 신고한 유저 모두에게
                    self.email(id)  # 이메일

        else:  # 이미 밴 당했으면
            self.email(id1)  # 바로 신고한 사람에게 이메일
    
    def email(self, id):  # 이메일 기능
        self.users[id].emailed += 1


def solution(id_list, report, k):
    system = System(id_list, k)  # 게시판 시스템 초기화
    
    for r in set(report):  # 신고
        id1, id2 = r.split()
        system.reports(id1, id2)

    answer = [system.users[i].emailed for i in id_list]  # 각 유저의 이메일 받은 개수
    return answer


'''
핵심 아이디어 1
이미 밴 당한 유저를 신고한 경우 이것 저것 하지 말고 바로 이메일을 보낸다.
'''