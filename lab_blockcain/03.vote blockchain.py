chain = []

#딕션너리 안에 딕션너리 가능
block1 = {
    'type': 'open',
    #데이터의 투표정보
    'data': {
        'id': '투표 ID',
        'question': '투표 질문',
        #여러 선택지: 리스트
        'options': ['투표 항목1', '투표 항목2', '투표 항목3']
    }
}

chain.append(block1)

block2 = {
    'type': 'vote',
    'data': {
        'id': '투표 ID',
        'vote': '투표 항목1'
    }
}

chain.append(block2)
print(chain)