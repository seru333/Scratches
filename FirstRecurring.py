def next_recur(ar1: list):
    store = {}
    print(ar1)
    answer = []
    for i in ar1:
        if i in store:
            store[i] += 1
            if i not in answer:
                answer.append(i)
        else:
            store[i] = 1
        print(store)
    print(answer)
    return answer



if __name__ == '__main__':
    assert next_recur(['A', 'B', 'C', 'B', 'A']) == ['B', 'A']
    assert next_recur(['Z','E','F','Z','H',2,'Z',1,2,'H']) == ['Z',2,'H']
