#老師帶你投資飆股，保證獲利，快加LINE群組
def judge(message):
    

    red_flags=[]
    KEYWORDS = {
        "fake_investment": ["投資", "保證獲利", "穩賺", "飆股", "老師", "帶單", "加LINE", "群組", "高報酬"],
        "fake_shopping":   ["解除分期", "重複扣款", "ATM", "客服", "訂單錯誤", "退款"],
        "fake_buyer":      ["賣貨便", "金流服務", "簽署協議", "認證", "無法下單"],
        "fake_police":     ["偵查不公開", "帳戶被凍結", "監管帳戶", "地檢署", "涉嫌洗錢", "警察"],
        "fake_romance":    ["寶貝", "海關", "包裹", "保證金", "急需"],
        "phishing":        ["點擊連結", "帳號異常", "立即驗證", "驗證碼", "http", "停用"],
        "prize":           ["中獎", "領獎", "手續費", "恭喜"],
    }
    best_type=None
    best_score=0

    for i,j in KEYWORDS.items():
        score=0
        for k in j:
            if k in message:
                red_flags.append(k)
                score+=1
        if(best_score<score):
            best_score=score
            best_type=i
    if len(red_flags)>=3:
        risk="high"
    elif len(red_flags)>=1:
        risk="medium"
    else: risk="low"



    return {"risk":risk,"scam_type":best_type, "red_flags": red_flags}
x = input('')
print(judge(x))