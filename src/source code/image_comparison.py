import cv2
import face_recognition

id1="Messi1.webp"
id2="Messi.webp"

img=cv2.imread(f"C:/Users/Usuario/Documents/UFG_Remoto/Projects/_ComputerVision/Software Domain/source code/{id1}")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

img2=cv2.imread(f"C:/Users/Usuario/Documents/UFG_Remoto/Projects/_ComputerVision/Software Domain/source code/images/{id2}")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

result= face_recognition.compare_faces([img_encoding], img_encoding2)

if result[0] == False:
    print("\n Different Faces \n")
else:
    print("\n Identical Faces \n")

# cv2.imshow("Img", img)
# cv2.imshow("Img 2", img2)
cv2.waitKey(0)