import pandas as pd
import numpy as np
# 1. 고정된 시드로 랜덤 값 생성
np.random.seed(42)
#2. 샘플 데이터 구성
names = [f"힉생{i}" for i in range(1,101)]
ages = np.random.randint(18,30,size=100)
genders = np.random.choice(["남","여"],size=100)
socres = np.random.randint(50,101,size=100)
#3. 데이터 프레임 생성
dataf = pd.DataFrame({
    "이름" : names,
    "나이" : ages,
    "성별" : genders,
    "점수" : socres
})
#4. CSV로 저장
dataf.to_excel("sample_data.xlsx", index=False)
print("sample_excel 생성 완료")
# 1. 데이터 상위 5행보기 가장 위꺼(높은게 아니라)
dataf = pd.read_excel("sample_data.xlsx")
print("Head")
print(dataf.head())
#2. 데이터 하위 5행 (마지막 5명)
print("\nTail")
print(dataf.tail())
#3. 데이터 요약 통계
print("\ndescribe")
print(dataf.describe())
#4. 데이터 정보 요약
print("\ninfor")
print(dataf.info)
#5. 특정 열만 출력
print("\n점수 열만")
print(dataf["점수"])
#6. 성별별 평균 점수
print("\n 성별별 평균 점수")
#7. 조건 필터링 예시 : 점수 90점 이상
print("\n 90점이상 학생")
print(dataf["점수"] >=90)