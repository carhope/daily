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

dataf = pd.read_excel("sample_data.xlsx")
print("Head")
print(dataf.head())

print("\nTail")
print(dataf.tail())

print("\ndescribe")
print(dataf.describe())

print("\ninfor")
print(dataf.info)