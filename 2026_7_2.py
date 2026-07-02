import pandas as pd
import numpy as np
np.random.seed(42)
names = [f"학생{i}" for i in range(1,101)]
ages = np.random.randint(18,30,size=100)
genders = np.random.choice(["남","여"],size=100)
socres = np.random.randint(50,101,size=100)

dataf = pd.DataFrame({
    "이름" : names,
    "나이" : ages,
    "성별" : genders,
    "점수" : socres
})

dataf.to_excel("sample_data.xlsx", index=False)
print("sample_excel 생성 완료")