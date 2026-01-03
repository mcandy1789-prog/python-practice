scores = {
    "Alice": 80,
    "Bob": 65,
    "Charlie": 90
}

# 平均点を計算
# 80点以上の人を表示
def judge(score):
    if score >= 80:
        return "Pass"
    else:
        return "Fail"

print(judge(85))
print(judge(60))
