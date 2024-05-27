import json

## 讀取JSON檔
with open('test.json', 'r') as f:
    ## 將內容裝進text
    text = f.read()

print("JSON Format: ", text)
print("Type: ", type(text))
print("From JSON String Transform To Python Dict")
print("Python Dict: ", json.loads(text))
print("Type: ", type(json.loads(text)))

