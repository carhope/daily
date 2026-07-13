"""
학생 스마트폰 이동중 사용 습관과 아차사고 경험 예측 모델
- 익명 자기보고 설문 데이터(가상) 기반
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score, cross_val_predict
from sklearn.metrics import classification_report

_font_path = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
fm.fontManager.addfont(_font_path)
plt.rcParams["font.family"] = fm.FontProperties(fname=_font_path).get_name()
plt.rcParams["axes.unicode_minus"] = False

np.random.seed(42)
n = 90  # 설문 방식이라 관찰보다 표본 확보가 유리

주_사용_앱_유형 = np.random.choice(
    ["SNS_숏폼", "메신저", "동영상", "게임", "기타"], size=n, p=[0.35, 0.30, 0.20, 0.10, 0.05]
)
알림_즉시확인 = np.random.choice([0, 1], size=n, p=[0.55, 0.45])
주_이용_이동수단 = np.random.choice(["보행", "자전거", "전동킥보드"], size=n, p=[0.65, 0.22, 0.13])
이어폰_습관 = np.random.choice([0, 1, 2], size=n, p=[0.35, 0.35, 0.30])  # 0=안함,1=가끔,2=항상
사용빈도_체감 = np.random.choice([0, 1, 2], size=n, p=[0.30, 0.45, 0.25])  # 0=거의없음,1=가끔,2=자주
학년 = np.random.choice([1, 2, 3], size=n)

숏폼_여부 = (주_사용_앱_유형 == "SNS_숏폼").astype(int)
이동장치_여부 = (주_이용_이동수단 != "보행").astype(int)

# 가설 반영 확률식
prob = (
    0.25 * 숏폼_여부
    + 0.15 * 알림_즉시확인
    + 0.15 * 이동장치_여부
    + 0.12 * (이어폰_습관 / 2)
    + 0.20 * (사용빈도_체감 / 2)
)
prob = np.clip(prob, 0.03, 0.95)
아차사고_경험_여부 = np.random.binomial(1, prob)

df = pd.DataFrame({
    "주_사용_앱_유형": 주_사용_앱_유형,
    "알림_즉시확인": 알림_즉시확인,
    "주_이용_이동수단": 주_이용_이동수단,
    "이어폰_습관": 이어폰_습관,
    "사용빈도_체감": 사용빈도_체감,
    "학년": 학년,
    "아차사고_경험_여부": 아차사고_경험_여부
})

print("=== 데이터셋 상위 5행 ===")
print(df.head())
print(f"\n총 샘플 수: {len(df)}개 | 아차사고 경험률: {df['아차사고_경험_여부'].mean()*100:.1f}%")

df_encoded = pd.get_dummies(df, columns=["주_사용_앱_유형", "주_이용_이동수단"])
X = df_encoded.drop(columns=["아차사고_경험_여부"])
y = df_encoded["아차사고_경험_여부"]

model = DecisionTreeClassifier(max_depth=3, random_state=42)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(model, X, y, cv=skf)
y_pred = cross_val_predict(model, X, y, cv=skf)

print(f"\n=== 5-Fold 교차검증 ===")
print(f"평균 정확도: {cv_scores.mean()*100:.1f}% (표준편차: {cv_scores.std()*100:.1f}%p)")
print(f"\n{classification_report(y, y_pred, target_names=['경험없음(0)','경험있음(1)'], zero_division=0)}")

importances = []
for train_idx, _ in skf.split(X, y):
    m = DecisionTreeClassifier(max_depth=3, random_state=42)
    m.fit(X.iloc[train_idx], y.iloc[train_idx])
    importances.append(m.feature_importances_)

importance_df = pd.DataFrame({
    "변수": X.columns, "평균_중요도": np.mean(importances, axis=0)
}).sort_values("평균_중요도", ascending=False)
print("\n=== 변수 중요도 ===")
print(importance_df.to_string(index=False))

print("\n=== 앱 유형별 아차사고 경험률 ===")
print((df.groupby("주_사용_앱_유형")["아차사고_경험_여부"].mean() * 100).round(1))

plot_df = importance_df.sort_values("평균_중요도", ascending=True)
plt.figure(figsize=(8, 5))
plt.barh(plot_df["변수"], plot_df["평균_중요도"], color="#4C72B0")
plt.xlabel("평균 Feature Importance (5-Fold)")
plt.title("아차사고 경험 예측 - 변수 중요도")
plt.tight_layout()
plt.savefig("/home/claude/survey_importance.png", dpi=150)
print("\n그래프 저장 완료")