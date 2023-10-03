import torch

A = torch.Tensor([3])
B = torch.Tensor([7])
C = torch.Tensor([2])
D = torch.Tensor([5])
E = torch.Tensor([10])

# TODO : torch 함수를 이용해서 (3 + 7) * 2 - 5 / 10 를 계산해보세요!
# 정답 19.5가 나와야 합니다!'
A = torch.mul(A,C)
A = torch.div(A,E)
B = torch.mul(B,C)
B = torch.sub(B,D)
B = torch.div(B,E)

output = torch.add(A, B) # 1줄에 torch 함수 하나씩만 사용하세요!
print(output)

# 아래 코드는 수정하실 필요가 없습니다!
if output == 19.5:
    print("🎉🎉🎉 성공!!! 🎉🎉🎉")
else:
    print("🐙 다시 도전해봐요!")