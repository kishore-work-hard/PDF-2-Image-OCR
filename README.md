# PDF-2-Image-OCR
this project is supposed to convert multiple or n number of pdf into images and does OCR and stores it within a text file.

In the folder "allPDF" keep all input PDF files. as many as needed. 

then in the req.txt file make sure to install all library 

then, numpy will cause some issues..so make the below changes then only ocr will work

go to -

venv\lib\site-packages\paddleocr\ppocr\postprocess\db_postprocess.py

replace -

xmin = np.clip(np.floor(box[:, 0].min()).astype(np.int), 0, w - 1) 

xmax = np.clip(np.ceil(box[:, 0].max()).astype(np.int), 0, w - 1) 

ymin = np.clip(np.floor(box[:, 1].min()).astype(np.int), 0, h - 1) 

ymax = np.clip(np.ceil(box[:, 1].max()).astype(np.int), 0, h - 1) 

with -

xmin = np.clip(np.floor(box[:, 0].min()).astype(int), 0, w - 1)

xmax = np.clip(np.ceil(box[:, 0].max()).astype(int), 0, w - 1)

ymin = np.clip(np.floor(box[:, 1].min()).astype(int), 0, h - 1)

ymax = np.clip(np.ceil(box[:, 1].max()).astype(int), 0, h - 1)
        
        
