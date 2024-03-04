someCondition = lambda a : a>3
otherCondition = lambda a : a<3
i = 0
while i < 7:
    try:
        if someCondition(i):
            i = 6
        elif otherCondition(i):
            continue
        print(f'i = {i}')
    finally:
        i += 1
