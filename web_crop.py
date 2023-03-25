import cv2
import numpy as np
import streamlit as st
import keyboard
from tesserocr import PyTessBaseAPI, RIL, get_languages, PSM , iterate_level , OEM
from PIL import Image

global frame

cap = cv2.VideoCapture(2)
frame = np.zeros((1280, 720, 3), dtype=np.uint8)
st.title('Webcam Crop')

x, y, w, h = 100, 100, 450, 250

w = st.slider('Width', 0, 640, 450)
h = st.slider('Height', 0, 480, 250)




stframe = st.empty()
stop = False
st.write('Press q to crop')

while stop == False:
    ret, frame = cap.read()
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
    stframe.image(frame, channels='BGR')
    if keyboard.is_pressed('q'):
        stop = True
        break
cap.release()
cv2.destroyAllWindows()


crop = frame[y:y+h, x:x+w]
reset = st.button('Reset')
while reset == True:
    x, y, w, h = 100, 100, 450, 250
    reset = False
    break

stframe.image(crop, channels='BGR')
option = st.selectbox(
    'Select Pre-Processing',
    ('Original Image','Binary', 'Dilation', 'Erosion', 'Opening', 'Closing'))

if option == 'Original Image':
    #original_img()
    st.write("default")
elif option == 'Binary':
    #binary_img()
    st.write("Binary")
elif option == 'Dilation':
    #dilation_img()
    st.write("Dilation")
elif option == 'Erosion':
    #erosion_img()
    st.write("Erosion")
elif option == 'Opening':
    #opening_img()
    st.write("Opening")
elif option == 'Closing':
    #closing_img()
    st.write("Closing")


image = Image.fromarray(crop)

#,oem=OEM.LSTM_ONLY, psm=PSM.SPARSE_TEXT_OSD

with PyTessBaseAPI(path='C:/Users/User/anaconda3/share/tessdata_best-main',lang="tha+eng") as api:
    api.SetImage(image)
    text = api.GetUTF8Text()
    conf = api.MeanTextConf()
    st.write("Confidence: {}".format(conf))
    # st.write("Text: {}".format(text))




name_array = text.split()
st.write(name_array)

# for i in range(len(name_array)):
#     if name_array[i] == 'Sender' or name_array[i] == 'sender:' or name_array[i] == 'sender' or name_array[i] == 'Sender:':
#         name1 = name_array[i+1]
#         address1 = name_array[i+2]
#         break
#     if name_array[i] == 'Receiver':
#         name2 = name_array[i+1]
#         address2 = name_array[i+2]
#         break
#     else:
#         name1 = 'Not Found'
#         address1 = 'Not Found'
#         name2 = 'Not Found'
#         address2 = 'Not Found'

# st.write('Name: ', name1)
# st.write('Address: ', address1)
# st.write('Name2: ', name2)
# st.write('Address2: ', address2)












    

















    



        










    


   

















    




    
    
   
    
    





