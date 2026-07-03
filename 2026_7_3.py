import platform
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 운영체제에 맞는 한글 폰트 경로 설정
if platform.system() == "Darwin":
    font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
else:
    font_path = font_manager.findfont(font_manager.FontProperties(family=["Malgun Gothic", "NanumGothic", "AppleGothic"]))

# 폰트 등록 및 matplotlib 기본 폰트로 적용
font_name = font_manager.FontProperties(fname=font_path).get_name()
font_manager.fontManager.addfont(font_path)
rc("font", family=font_name)
plt.rcParams["axes.unicode_minus"] = False

# 그래프 객체 생성
G = nx.Graph()

# 장소 노드 추가
G.add_nodes_from([
    "집",
    "학교",
    "도서관",
    "카페",
    "편의점",
    "공원",
    "마트"
])

# (출발지, 도착지, 이동 비용) 형태의 간선 데이터
edges = [
    ("집","학교",4),
    ("집","도서관",2),
    ("학교","도서관",1),
    ("학교","카페",5),
    ("도서관","카페",8),
    ("도서관","편의점",10),
    ("카페","마트",2),
    ("카페","편의점",6),
    ("마트","공원",8),
    ("편의점","공원",2)
]

# 가중치가 있는 간선을 그래프에 추가
for u,v,w in edges:
    G.add_edge(u,v,weight=w)

# spring layout 알고리즘으로 노드 위치 계산 (seed 고정으로 재현성 보장)
pos = nx.spring_layout(G, seed=42)

# 그래프 시각화 (노드, 레이블 포함)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    node_color="skyblue",
    font_family=font_name
)

# 간선 위에 가중치(이동 비용) 레이블 표시
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

# 그래프 출력
plt.show()
