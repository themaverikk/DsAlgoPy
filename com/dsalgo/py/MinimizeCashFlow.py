class Person:

    def __init__(self, num, balance):
        self.num = num
        self.balance = balance


def minimize_cash_flow(cash_flow):
    inbound = []
    outbound = []

    for i in range(len(cash_flow)):

        curr_friend_cash_flow = 0

        for j in range(len(cash_flow[i])):
            curr_friend_cash_flow += cash_flow[j][i]
            curr_friend_cash_flow -= cash_flow[i][j]

        if curr_friend_cash_flow > 0:
            inbound.append(Person(i, curr_friend_cash_flow))
        elif curr_friend_cash_flow < 0:
            outbound.append(Person(i, -curr_friend_cash_flow))

    inbound.sort(key=lambda p: p.balance)
    outbound.sort(key=lambda p: p.balance)

    i = 0
    j = 0
    while i < len(inbound):
        transferred_amt = min(inbound[i].balance, outbound[j].balance)
        print("Person {} gives {} Rupees to Person {}".format(j, transferred_amt, i))
        inbound[i].balance -= transferred_amt
        outbound[j].balance -= transferred_amt

        if inbound[i].balance == 0:
            i += 1

        if outbound[j].balance == 0:
            j += 1


graph = [[0, 25, 2000],
         [0, 0, 5000],
         [0, 0, 0]]

minimize_cash_flow(graph)
