import os
import fitz
from utils import ocr
import cv2

# specify the folder path containing PDF files
folder_path = "./allPDF"

# create a result folder to store the PDF folders
result_folder = "result"
os.makedirs(result_folder, exist_ok=True)

# iterate over each PDF file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        # get the full path of the PDF file
        pdf_path = os.path.join(folder_path, filename)

        # get the name of the PDF file without the extension
        pdf_name = os.path.splitext(filename)[0]

        # create a folder with the PDF name within the result folder
        pdf_folder_path = os.path.join(result_folder, pdf_name)
        os.makedirs(pdf_folder_path, exist_ok=True)

        filename = pdf_folder_path + '\\' + pdf_name + '.txt'

        # open the PDF file
        pdf_file = fitz.open(pdf_path)

        # iterate over each page in the PDF
        for page_index in range(len(pdf_file)):
            # get the page
            page = pdf_file[page_index]

            # convert the page to a pixmap
            pix = page.get_pixmap()

            # save the pixmap as an image
            image_name = f"{page_index + 1}.png"
            image_path = os.path.join(pdf_folder_path, image_name)
            pix.save(image_path, "PNG")
            print(f"Image saved to {image_path}")


            text = ''
            try:
                # do ocr
                text = ocr.read(image_path)
                print("text- ", text)
                # create the file and write the contents to it
                with open(filename, 'a') as f:
                    f.write(text)
                print()
            except:
                pass

        # close the PDF file
        pdf_file.close()
