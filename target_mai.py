import numpy as np
import matplotlib.pyplot as plt

# 用于计算maimai推分的程序

# DX评分系数
RULE = {
    (100.5, 101) : 22.4, 
    (100, 100.5): 21.6,
    (99.5, 100) : 21.1,
    (99, 99.5) :20.8,
    (98, 99) : 20.3,
    (97, 98) : 20.0
    # (0,97.0) : 0, 因为不考虑97，S以下评分
}

# 正向计算dx评分
def forward_calculate(chart_level, score):
    # dx_score = chart_level * score * RULE_coef
    if score >= 100.5:
        score = 100.5 # 鸟加以外部分不予计算
    for rg, coef in RULE.items():
        if score >= rg[0]:
            return chart_level*score*coef/100

# 计算给定谱面定数，dx评分和成绩的分布
def generate_distribution(chart_level):
    # Generate scores from 97 to 100.5 with small intervals
    scores = np.linspace(97, 100.5, num=1000)
    outputs = []
    
    # Calculate outputs using the forward_calculate function
    for score in scores:
        outputs.append(forward_calculate(chart_level, score))
    
    # Plot outputs with respect to scores
    plt.figure(figsize=(10, 6))
    plt.plot(scores, outputs, label="Distribution")
    plt.xlabel("Scores")
    plt.ylabel("Outputs")
    plt.title("Distribution of Outputs vs Scores")
    plt.legend()
    plt.grid(True)
    plt.show()

# 反向计算各难度，各评级下的max/min
def backward_calculation_range(chart_level):
    ret = {}
    for rg, coef in RULE.items():
        ret[rg] = (chart_level*rg[0]*coef/100,chart_level*rg[1]*coef/100)
    ret[(100.5,101)] = chart_level*100.5*22.4/100
    return ret

# 较难计算，因为不连续...
# 计算给定铺面定数，达到指定dx rating的最低评分acc
def backward_calculation(chart_level, target_score):
    scores = np.linspace(97, 100.5, num=1000)
    outputs = []
    
    # Calculate outputs using the forward_calculate function
    for score in scores:
        outputs.append(forward_calculate(chart_level, score))
    for i, dx in enumerate(outputs):
        if target_score <= dx:
            return scores[i], '验证:', forward_calculate(chart_level,scores[i])

print(forward_calculate(14.9,100.5678))

# 对lv14的简单曲目计算：
# generate_distribution(14)

print(backward_calculation_range(14))

print(backward_calculation(14,300))