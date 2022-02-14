# 조겁
# 1. 1번 집 색 != 2번 집 색
# 2. N번 집 색 != N-1번 집 색
# 3. i번 집 색 != i-1번 집 색 != i+1번 집 색
# 모든 집을 칠하는 비용의 최솟값

N=int(input()) # 집의 수
dp=[list(map(int, input().split())) for _ in range(N)] # 누접 최솟값이 담김, 빨초파의 비용

for i in range(1,N):
    dp[i][0]= dp[i][0] + min(dp[i - 1][1], dp[i - 1][2]) # 집i를 빨간색으로 칠하는 경우 집i-1을 초록색으로 칠하는 경우와 파란색으로 칠하는 경우 중 최솟값 선택
    dp[i][1]= dp[i][1] + min(dp[i - 1][0], dp[i - 1][2]) # 집i를 초록색으로 칠하는 경우 ...
    dp[i][2]= dp[i][2] + min(dp[i - 1][0], dp[i - 1][1]) # 집i를 파란색으로 칠하는 경우 ...

print(min(dp[N - 1]))