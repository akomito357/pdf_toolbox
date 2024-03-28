# last update: 240329

'''
參考資料
1. https://steam.oxxostudio.tw/category/python/example/pdfplumber.html
2. https://github.com/hbh112233abc/pdfplumber/blob/stable/README-CN.md
3. https://pypdf2.readthedocs.io/en/latest/index.html
4. https://medium.com/seaniap/python-%E4%BD%BF%E7%94%A8%E6%AA%94%E6%A1%88%E7%B3%BB%E7%B5%B1-eaecbe7001dd
5. https://steam.oxxostudio.tw/category/python/example/image-conversion.html
6. https://stackoverflow.com/questions/62805973/how-do-i-extract-all-of-the-text-from-a-pdf-using-indexing
7. https://steam.oxxostudio.tw/category/python/tkinter/button.html
8. https://steam.oxxostudio.tw/category/python/tkinter/labelframe.html
'''

import os
import pdfplumber
import tkinter as tk
from PyPDF2 import PdfWriter
from PIL import Image

def get_file(filExt):
    msg = 'loading……'
    label_msg.config(text=msg) 
    fileList = []
    for f in os.listdir(os.curdir):
        if f.lower().endswith(filExt):
            fileList.append(f)
    return fileList

def get_text(get_text_list):
    if get_text_list != []:
        for file in get_text_list:
            txt_name = file[:-3] + 'txt'
            f = open(txt_name, 'w+', encoding='utf-8')
            with pdfplumber.open(file) as pdf:
                for pdf_page in pdf.pages:
                    single_page_text = pdf_page.extract_text()
                    f.write(single_page_text)
                f.close()
        get_text_msg = get_text_list, '皆已轉為txt檔。'
    elif get_text_list == []:
        get_text_msg = '資料夾中沒有pdf檔，請在該資料夾裡放入欲轉成文字的的pdf檔。'
    label_msg.config(text=get_text_msg) 

def merge_pdf(merge_list):
    if merge_list != []:
        merger = PdfWriter()
        for pdf in merge_list:
            merger.append(pdf)   
        merger.write("merged_pdf.pdf")
        merge_msg = merge_list, '已經合併為一個pdf檔。'
        merger.close()
    elif merge_list == []:
        merge_msg = '資料夾中沒有pdf檔，請在該資料夾裡放入欲合併的pdf檔。'
    label_msg.config(text=merge_msg) 

def convert(convert_list):
    if convert_list != []:
        for pic in convert_list:
            im = Image.open(pic)
            im.save(pic[:-3]+'pdf')
        convert_msg = convert_list, 'have been converted to pdf.'    
    elif convert_list == []:
        convert_msg = '資料夾中沒有jpg、jpeg或png檔，請在該資料夾裡放入欲轉為pdf的圖片。'
    label_msg.config(text=convert_msg) 

## windows setting
root = tk.Tk()
root.title('pdf_editor')
root_width = 600
root_height = 450
root.geometry(f'{root_width}x{root_height}')
root.resizable(False, False)

# labelframe for descrip
descrip_frame = tk.LabelFrame(root, text = '說明')
descrip_frame.pack(fill='x', padx=20, pady=10, ipady=5)
descrip_text000 = tk.Label(descrip_frame, justify='left', wraplength=550, text='此程式會針對「editPDF」資料夾中的檔案進行處理。以下進行說明：\n')
descrip_title01 = tk.Label(descrip_frame, font=('微軟正黑體', 9, 'bold'),  text='1. 獲取pdf文字', anchor='e')
descrip_text101 = tk.Label(descrip_frame, justify='left', wraplength=550, text='''此功能將「editPDF」資料夾中的pdf檔文字提取出來，另存為txt檔，檔名同原pdf檔名。不支援表格。
一次處理太多檔案可能會造成程式卡頓。\n''')
descrip_title02 = tk.Label(descrip_frame, font=('微軟正黑體', 9, 'bold'), text='2. 將圖檔轉為pdf', anchor='e')
descrip_text201 = tk.Label(descrip_frame, justify='left', wraplength=550, text='''此功能將「editPDF」資料夾中的圖片檔轉換為pdf檔，
支援格式包括：jpg、jpeg、png。轉為pdf的檔案會以原圖檔名輸出。\n''')
descrip_title03 = tk.Label(descrip_frame, font=('微軟正黑體', 9, 'bold'), text='3. 合併pdf', anchor='e')
descrip_text301 = tk.Label(descrip_frame, justify='left', wraplength=550, text='''此功能將「editPDF」資料夾中的pdf檔進行合併。
合併完成的pdf檔名為「merged_pdf.pdf」，若資料夾內已有同名檔案，該檔案會加入合併後被覆蓋。
頁面排序按照檔名順序，因此建議可在進行合併前先更改檔名（如：pdf01、pdf02、pdf03……）。
亦可先按順序更改好圖片檔名，將圖片轉為pdf後再直接按鍵合併。''')

descrip_text000.pack(anchor='w')
descrip_title01.pack(anchor='w')
descrip_text101.pack(anchor='w')
descrip_title02.pack(anchor='w')
descrip_text201.pack(anchor='w')
descrip_title03.pack(anchor='w')
descrip_text301.pack(anchor='w')

# labelframe for system message
system_msg_frame = tk.LabelFrame(root, text = '訊息')
system_msg_frame.pack(fill='x', padx=20, pady=10, ipady=5)

label_msg = tk.Label(system_msg_frame, wraplength=500)
label_msg.pack()
label_msg.config(text='歡迎使用本程式') 

# bottoms
bottom_frame = tk.Frame(root)
bottom_frame.pack(padx=20, pady=5)

btn_get_text = tk.Button(bottom_frame, text='【獲取pdf文字】', command=lambda: get_text(get_file('pdf')))
btn_get_text.grid(column=0, row=0, padx=20, pady=10)

btn_convert = tk.Button(bottom_frame, text='【將圖檔轉為pdf】', command=lambda: convert(get_file('jpg' or 'jpeg' or 'png')))
btn_convert.grid(column=2, row=0, padx=20, pady=10)

btn_merge = tk.Button(bottom_frame, text='【合併pdf】', command=lambda: merge_pdf(get_file('pdf')))
btn_merge.grid(column=4, row=0, padx=20, pady=10)


def main():
    os.chdir('editPDF') # change path to specify folder
    root.mainloop()

if __name__ == '__main__':
    main()