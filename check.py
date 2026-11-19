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
    for i,j in KEYWORDS.items():
        for k in j:
            if k in message:
                red_flags.append(k)
    return red_flags
x = input('')
print(judge(x))