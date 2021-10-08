from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import pytesseract 
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
root = Tk()
root.title('TechVidvan Text from image project') 
newline= Label(root)
uploaded_img=Label(root)
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
def extract(path):
    Actual_image = cv2.imread(path)
    Sample_img = cv2.resize(Actual_image,(400,350))
    Image_ht,Image_wd,Image_thickness = Sample_img.shape
    Sample_img = cv2.cvtColor(Sample_img,cv2.COLOR_BGR2RGB)
    texts = pytesseract.image_to_data(Sample_img) 
    mytext=""
    prevy=0
    for cnt,text in enumerate(texts.splitlines()):
        if cnt==0:
            continue
        text = text.split()
        if len(text)==12:
            x,y,w,h = int(text[6]),int(text[7]),int(text[8]),int(text[9])
            if(len(mytext)==0):
                prey=y
            if(prevy-y>=10 or y-prevy>=10):
                print(mytext)
                Label(root,text=mytext,font=('Times',15,'bold')).pack()
                mytext=""
            mytext = mytext + text[11]+" "
            prevy=y
    Label(root,text=mytext,font=('Times',15,'bold')).pack()
def show_extract_button(path):
    extractBtn= Button(root,text="Extract text",command=lambda: extract(path),bg="#2f2f77",fg="gray",pady=15,padx=15,font=('Times',15,'bold'))
    extractBtn.pack()
def upload():
    try:
        path=filedialog.askopenfilename()
        image=Image.open(path)
        img=ImageTk.PhotoImage(image)
        uploaded_img.configure(image=img)
        uploaded_img.image=img
        show_extract_button(path)
    except:
        pass  
uploadbtn = Button(root,text="Upload an image",command=upload,bg="#2f2f77",fg="gray",height=2,width=20,font=('Times',15,'bold')).pack()
newline.configure(text='\n')
newline.pack()
uploaded_img.pack()
root.mainloop()
