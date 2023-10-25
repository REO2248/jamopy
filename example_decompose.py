from jamo import 자모분리
while True:
    입력됨 = input('입력: ')
    분리됨 = 자모분리(입력됨)
    print(분리됨)
    for 글자 in 분리됨:
        if 글자.조선글자인가:
            print(글자.자음,글자.모음,글자.받침)
        else:
            print(글자)
    print()