# pdf_toolbox 
last updated at: 2024/04/20

## 說明
本程式會針對「editPDF」資料夾中的檔案進行處理。目前共有三種功能：

**1. 獲取pdf文字**

此功能將「editPDF」資料夾中的pdf檔文字提取出來，另存為txt檔，檔名同原pdf檔名。不支援表格。
一次處理太多檔案可能會造成程式卡頓。

**2. 將圖檔轉為pdf**

此功能將「editPDF」資料夾中的圖片檔轉換為pdf檔，支援格式包括：jpg、jpeg、png。
轉為pdf的檔案會以原圖檔名輸出。

**3. 合併pdf**

此功能將「editPDF」資料夾中的pdf檔進行合併。
合併完成的pdf檔名為「merged_pdf.pdf」，若資料夾內已有同名檔案，該檔案會加入合併後被覆蓋。
頁面排序按照檔名順序，因此建議可在進行合併前先更改檔名（如：pdf01、pdf02、pdf03……）。
亦可先按順序更改好圖片檔名，將圖片轉為pdf後再直接按鍵合併。


其餘功能待新增。