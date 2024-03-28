# PDF編輯器
# 合併、分割、擷取內容、轉檔(jpg or png to pdf)
# 用檔名/資料夾區分要做什麼?
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
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image

os.chdir('editPDF') # change path to specify folder
system_msg = ''

def get_file(filExt):
    fileList = []
    for f in os.listdir(os.curdir):
        if f.lower().endswith(filExt):
            fileList.append(f)
    return fileList

def get_text(get_text_list): # with pdfplumber
    for file in get_text_list:
        txt_name = file[:-3] + 'txt'
        f = open(txt_name, 'w+', encoding='utf-8')
        with pdfplumber.open(file) as pdf:
            for pdf_page in pdf.pages:
                single_page_text = pdf_page.extract_text()
                f.write(single_page_text)
            f.close()

def merge_pdf(merge_list):
    if merge_list != []:
        merger = PdfWriter()
        for pdf in merge_list:
            merger.append(pdf)   
        merger.write("merged_pdf.pdf")
        print(merge_list, 'have been merged into one pdf file.')
        merger.close()
    elif merge_list == []:
        print('merge_PDF資料夾中沒有pdf檔，請在該資料夾裡放入欲合併的pdf檔。') # 萬一資料夾裡沒有pdf/不是pdf的檔案要予以排除

# 轉個檔
def convert(convert_list):
    if convert_list != []:
        for pic in convert_list:
            im = Image.open(pic)
            im.save(pic[:-3]+'pdf')
        print(convert_list, 'have been converted to pdf.')      
    elif convert_list == []:
        print('pic_to_PDF資料夾中沒有jpg或png檔，請在該資料夾裡放入欲轉為pdf的圖片。')


root = tk.Tk()
root.title('pdf_editor')
root.resizable(False, False)
# root.geometry('500x500')

# labelframe descrip
descrip_frame = tk.LabelFrame(root, text = '說明')
descrip_frame.pack(padx=20, pady=10, ipady=5)
descrip_text000 = tk.Label(descrip_frame, justify='left', text='此程式會針對「editPDF」資料夾中的檔案進行處理。以下進行說明：\n')
descrip_title01 = tk.Label(descrip_frame, font=('Arial', 9, 'bold'),  text='1. 獲取pdf文字', anchor='e')
descrip_text101 = tk.Label(descrip_frame, justify='left', text='此功能將「editPDF」資料夾中的pdf檔文字提取出來，另存為txt檔，檔名同原pdf檔名。\n一次處理太多檔案可能會造成程式卡頓。\n')
descrip_title02 = tk.Label(descrip_frame, font=('Arial', 9, 'bold'), text='2. 將圖檔轉為pdf', anchor='e')
descrip_text201 = tk.Label(descrip_frame, justify='left', text='此功能將「editPDF」資料夾中的圖片檔轉換為pdf檔，支援格式包括：jpg、jpeg、png。\n轉為pdf的檔案會以原圖檔名輸出。\n')
descrip_title03 = tk.Label(descrip_frame, font=('Arial', 9, 'bold'), text='3. 合併pdf', anchor='e')
descrip_text301 = tk.Label(descrip_frame, justify='left', text='此功能將「editPDF」資料夾中的pdf檔進行合併。\n合併完成的pdf檔名為「」，頁面排序按照檔名順序，\n因此建議可在進行合併前預先更改檔名（如：pdf01、pdf02、pdf03……）。')

descrip_text000.pack(anchor='w')
descrip_title01.pack(anchor='w')
descrip_text101.pack(anchor='w')
descrip_title02.pack(anchor='w')
descrip_text201.pack(anchor='w')
descrip_title03.pack(anchor='w')
descrip_text301.pack(anchor='w')

# labelframe 系統文字
system_msg_frame = tk.LabelFrame(root, text = '訊息')

bottom_frame = tk.Frame(root)
bottom_frame.pack(padx=20)

# get_text_botton
btn_get_text = tk.Button(bottom_frame, text='獲取pdf文字！', command=lambda: get_text(get_file('pdf')))
btn_get_text.grid(column=0, row=0, padx=20, pady=10)

# convert_botton
btn_convert = tk.Button(bottom_frame, text='將圖檔轉為pdf！', command=lambda: convert(get_file('jpg' or 'jpeg' or 'png')))
btn_convert.grid(column=2, row=0, padx=20, pady=10)

# merge_botton
btn_merge = tk.Button(bottom_frame, text='合併pdf！', command=lambda: merge_pdf(get_file('pdf')))
btn_merge.grid(column=4, row=0, padx=20, pady=10)



def main():
    file_names = get_file('get_PDF_text', 'pdf')
    get_text(file_names)

root.mainloop()