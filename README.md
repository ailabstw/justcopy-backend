# 記者快抄

## Install & Setup

若在Ubuntu環境下，可直接執行以下指令：

```
sudo bash install.sh
```

若在其他環境下，請參照`install.sh`與`requirements.txt`來安裝相關python3套件

若相關套件已安裝成功，請更改`setup.sh`並source它。

- `JIEBA_DATA`: jieba 資料中 extra_dict 的路徑，用於斷詞。
- `DATA`: 你想把爬下來的 PTT 資料放哪，舉例來說從八卦版爬下來的資料會放在 `$DATA/raw/Gossiping/`
- `POSTS`: 你想把產生的新聞放在哪裡。
- `TEMPLATE`: 你把新聞的 template 放在哪裡。
- `DOC`: 搜尋圖片時用到的DB位置 (目前未直接公開，歡迎來信聯絡)
- `TFIDF_DATA`: DB的tf-idf資訊 (目前未直接公開，歡迎來信聯絡)
- `PYTHONPATH`: 這個 repository 的路徑
- `DBDATA`: 建立DB所用的PTT資料，產生新聞時不會用到

## To Run

`python3 journalist.py`

## About Image Searching DataBase

因為一些隱私權問題，我們並沒有直接公開資料庫。

目前使用 ["Reading Wikipedia to Answer Open-Domain Questions", ACL 2017](https://github.com/facebookresearch/DrQA) 提供的 search engine 演算法來找適合的圖片。

您可直接省略需要用到此DB的程式碼、跳過自動搜尋合適圖片的步驟，或來信與我們聯絡取得`DOC`與`TFIDF_DATA`。

## About Auto Generated Articles

目前使用 TextRank 抓出內文重點與重要回文後，將其填進我們撰寫的簡單模板(template)來產生新聞。

其他嘗試中的方法：

- [“Abstractive Sentence Summarization with Attentive Recurrent Neural Networks”, NAACL 2016](https://github.com/facebookarchive/NAMAS): 容易 overfitting 且無法處理中文因斷詞所以 vocabulary size 太大的問題
- ["Get To The Point: Summarization with Pointer-Generator Networks", ACL 2017](https://github.com/exe1023/pointer-generator): 現在正在嘗試的 model，處理 OOV 的能力很不錯，但是產生出來的摘要在文法上略嫌不通順，可能是 training data 的問題。

Training data 為從蘋果, 自由時報等新聞網站爬下來約 10 萬篇新聞。

同樣因為一些著作權問題不太方便公開 training data。如果你對自動產生文章有心得或是想要提供中文文章與摘要的 data，歡迎和我們聯絡。

Update: 現在我使用一份叫做 [CIRB010](kslab.km.nccu.edu.tw/xms/read_attach.php?id=150) 的 data，實際測試在 pointer-generator networks 上後結果還算能接受，但是文法不通順的問題仍待解決。

## Issues

- Code需要進一步整理來減少不必要的運算
- Pre-processing與summarize改良
- <strike>DataBase 與搜尋圖片演算法的改良</strike>
- 自動產生內文而不依賴 template

## Related projects

- [PTT-Chat-Generator](https://github.com/zake7749/PTT-Chat-Generator): `util/ptt_filter.py` 的原型
- [ptt-web-crawler](https://github.com/jwlin/ptt-web-crawler): `util/crawler` 的原型
- [TextRank4ZH](https://github.com/letiantian/TextRank4ZH): 中文 TextRank 的實作
- [DrQA](https://github.com/facebookresearch/DrQA): 用於搜索相關文章與圖片
- [jieba](https://github.com/fxsjy/jieba): 中文斷詞
