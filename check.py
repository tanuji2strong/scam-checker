from dotenv import load_dotenv
import aisuite as ai
import json
#老師帶你投資飆股，保證獲利，快加LINE群組
load_dotenv()   
client = ai.Client()
KEYWORDS = {
        "fake_investment": ["投資", "保證獲利", "穩賺", "飆股", "老師", "帶單", "加LINE", "群組", "高報酬"],
        "fake_shopping":   ["解除分期", "重複扣款", "ATM", "客服", "訂單錯誤", "退款"],
        "fake_buyer":      ["賣貨便", "金流服務", "簽署協議", "認證", "無法下單"],
        "fake_police":     ["偵查不公開", "帳戶被凍結", "監管帳戶", "地檢署", "涉嫌洗錢", "警察"],
        "fake_romance":    ["寶貝", "海關", "包裹", "保證金", "急需"],
        "phishing":        ["點擊連結", "帳號異常", "立即驗證", "驗證碼", "http", "停用"],
        "prize":           ["中獎", "領獎", "手續費", "恭喜"],
}
TESTS = [
    "老師帶你投資飆股，保證獲利，快加LINE群組",
    "您的訂單重複扣款，請至ATM操作解除分期，有問題請洽客服",
    "恭喜中獎！請點擊連結領獎",
    "這裡是地檢署，你涉嫌洗錢，帳戶被凍結，偵查不公開不能告訴家人",
    "寶貝我在海關被扣了包裹，急需保證金",
    "你的帳號異常，請立即驗證",
    "明天一起吃午餐嗎？",
    "我爸最近在研究投資ETF",
    "恭喜！您的帳號異常，請洽客服",
]
SYSTEM_PROMPT = """You check Chinese text messages for scams, based on common scam types in Taiwan.

Reply with one JSON object only. No explanation, no markdown, no code fences.
The JSON must have exactly these 3 keys:
- "risk": one of "low", "medium", "high"
- "scam_type": one of "fake_investment", "fake_shopping", "fake_buyer", "fake_police", "fake_romance", "phishing", "prize", "none"
- "red_flags": a list of short phrases copied exactly from the message, character for character. Do not rewrite or translate them.

Scam types:
- fake_investment: stock tips, "teachers", guaranteed profit, investment groups or apps
- fake_shopping: fake shop or customer service, order or payment errors, ATM steps, canceling installments
- fake_buyer: a "buyer" on a selling platform who sends a link to verify or sign a payment service
- fake_police: someone claiming to be police, prosecutors, or a government office; frozen accounts, money laundering, secrecy
- fake_romance: an online partner who needs money for customs, packages, or emergencies
- phishing: account or login warnings that ask you to click, log in, or verify
- prize: you won something and must click, pay a fee, or give data to claim it

Risk levels:
- high: asks for money, personal data, a click, or moving to another app, usually with pressure or urgency
- medium: some suspicious signs, but no clear request yet
- low: a normal message

Mentioning a topic like investing, shopping, or police is not a red flag by itself. Judge what the message asks the reader to do.
If the message is normal, reply with risk "low", scam_type "none", and red_flags [].

Example 1
Message: 你好，我是你賣場的買家，我這邊無法下單，客服說你要點擊以下連結完成簽署金流服務：http://bit.ly/xxxx
Reply: {"risk": "high", "scam_type": "fake_buyer", "red_flags": ["無法下單", "點擊以下連結", "簽署金流服務"]}

Example 2
Message: 下週的報告我放在雲端了，你有空看一下
Reply: {"risk": "low", "scam_type": "none", "red_flags": []}
"""

def judge_keywords(message):

    red_flags=[]
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

def judge_llm(message):
    response = client.chat.completions.create(
    model="groq:qwen/qwen3.8-27b",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT}  ,  
        {"role": "user", "content": message },
        
    ],
    )
    return json.loads(response.choices[0].message.content)


#x = input('')
#print(judge_keywords(x))
#print(judge_llm(x))
result = judge_llm(TESTS[0])
print(type(result))
print(result["risk"])