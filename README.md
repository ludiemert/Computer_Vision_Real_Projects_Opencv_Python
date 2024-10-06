<h2 align="center"> 💻 Computer_Vision_Real_Projects_Opencv_Python </h2>
<br>
<h4 align="center">  - This repository explores Computer Vision in a practical way using OpenCV and Python. You will learn how to apply advanced image and video processing techniques to develop automated solutions, including object recognition, face detection, motion analysis, and more, integrating computer vision into real-world applications. </h4>
  
---


<h4 align="center">Projects: 🚀</h4>

---

<h4 align="center">1_opencvBasic 🚀</h4>

<div align="center">
    <img src="1_opencvBasic/1_img_open_cv/6 - Dilate - dilatar a imagem de contornos.png" style="width: 45%; margin-right: 5%;" alt="01 - img piramed">
    <img src="1_opencvBasic/1_img_open_cv/8 - process de closing and opening img.png" style="width: 45%;" alt="01 - img piramed">
</div>

---

<h4 align="center">2_binarizacao _threshold_adaptativo 🚀</h4>

<div align="center">
    <img src="2_binarizacao _threshold_adaptativo/2_img_binarizacao/1_img_binarizacao_c_sombra.png" style="width: 45%; margin-right: 5%;" alt="01 - img_binarizacao_c_sombra">
    <img src="2_binarizacao _threshold_adaptativo/2_img_binarizacao/3_img binarizada_th1_th2_th3.png" style="width: 45%;" alt="binarizada_th1_th2_th3">
</div>

---

<h4 align="center">3_separate_objects_img 🚀</h4>

<div align="center">
    <img src="3_separate_objects_img/3_recort_obj/1_contorno_de_cada_img_num.png" style="width: 45%; margin-right: 5%;" alt="1_contorno_de_cada_img_num">
    <img src="3_separate_objects_img/3_recort_obj/2_mapeamento_contorno_obj.png" style="width: 45%;" alt="2_mapeamento_contorno_obj">
 <br />
  <br />
    <img src="3_separate_objects_img/3_recort_obj/3_colocar_retangulo_nos_obj_contorn.png" style="width: 45%; margin-right: 5%;" alt="3_colocar_retangulo_nos_obj_contorn">
    <img src="3_separate_objects_img/3_recort_obj/4_recortou_os_objteos_eaddpasta.png" style="width: 45%;" alt="4_recortou_os_objteos_eaddpasta">
</div>

---

<h4 align="center">4_Deteccao_obj_Haarcascade 🚀</h4>

<div align="center">
    <img src="4_Deteccao_obj_Haarcascade/4_img_Haarcascade/3 - detecta_face_front.png" style="width: 45%; margin-right: 5%;" alt="3 - detecta_face_front">
     <img src="4_Deteccao_obj_Haarcascade/4_img_Haarcascade/4 - detecta_eyes.png" style="width: 45%; margin-right: 5%;" alt="3 - detecta_face_front">
 <br />
  <br />
    <img src="4_Deteccao_obj_Haarcascade/4_img_HaarCascade_treinam_cap_img/1_capturar_fotos.png" style="width: 45%; margin-right: 5%;" alt="1_capturar_fotos">
    <img src="4_Deteccao_obj_Haarcascade/4_img_HaarCascade_treinam_cap_img/3_cascade.xml_ reconhec_obj.png" style="width: 45%;" alt="3_cascade.xml_ reconhec_obj">
</div>

---

<h4 align="center">5_Parking_Vacancies_Accountant 🚀</h4>

<div align="center">
    <img src="5_Parking_Vacancies_Accountant/01_img_JobCounter/01_mark_vacancies.png" style="width: 45%; margin-right: 5%;" alt="01_mark_vacancies">
     <img src="5_Parking_Vacancies_Accountant/01_img_JobCounter/04_video_checking_vacant_coordinates.png" style="width: 45%; margin-right: 5%;" alt="04_video_checking_vacant_coordinates">
 <br />
  <br />
    <img src="5_Parking_Vacancies_Accountant/01_img_JobCounter/07_img_clear.png" style="width: 45%; margin-right: 5%;" alt="07_img_clear">
    <img src="5_Parking_Vacancies_Accountant/01_img_JobCounter/9_img_dilate.png" style="width: 45%;" alt="9_img_dilate">
   <br />
  <br />
    <img src="5_Parking_Vacancies_Accountant/01_img_JobCounter/13_green_rectangle when_vacancy_ free.png" style="width: 45%; margin-right: 5%;" alt="13_green_rectangle when_vacancy_ free">
    <img src="5_Parking_Vacancies_Accountant/01_img_JobCounter/14_vacancy_free_text.png" style="width: 45%;" alt="14_vacancy_free_text">
</div>

---


### 📋 Technologies Used

- OpenCV:** omputer Vision Library.
- Python:** Programming Language.
- PyCharm:** IDE for Python development.
- GitHub:** Version control and code collaboration.

---

### 🛠️ Key OpenCV Commands
<br />

<h4 align="center"> 1. Basic Image Manipulation </h4>
<br />

- imread: Loads an image.
- resize: Resizes the image.
- cvtColor: Converts between different color spaces (e.g., BGR to grayscale).
- GaussianBlur: Applies a filter to smooth the image.
- Canny: Detects edges.

---

<h4 align="center"> 2. Morphological Operations </h4>
<br />

- dilate: Expands white areas, useful for highlighting objects.
- erode: Reduces noise by shrinking white areas.
- MORPH_OPEN: Erosion followed by dilation, removing small noise.
- GaussianBlur: Applies a filter to smooth the image.
- MORPH_CLOSE: Dilation followed by erosion, filling in gaps.

---

<h4 align="center"> 3. Drawing Shapes and Adding Text </h4>
<br />

<h5 align="center"> This project allows you to draw geometric shapes and add text to images and videos. Sample code for shapes: </h5>
<br />

> Drawing Shapes and Adding Text - python
```bash
cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 5)  # Rectangle
cv2.circle(img, (center_x, center_y), radius, (0, 0, 255), 5)  # Circle
cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Line
cv2.putText(img, 'Text', (20, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)  # Text

```
---

<h4 align="center"> 4. Binarization and Thresholding </h4>
<br />

- cv2.THRESH_BINARY: Converts the image to black and white using a fixed threshold.
- cv2.ADAPTIVE_THRESH_GAUSSIAN_C: Adaptive thresholding that improves image quality.

---

<h4 align="center"> 5. Object Segmentation in Images </h4>
<br />

<h5 align="center"> Using contours to isolate objects and save them separately: </h5>
<br />

> Using contours to isolate objects and save them separately: - python
```bash
contours, hierarchy = cv2.findContours(imgClose, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

```
---

<h5 align="center"> 6. Object Detection with HaarCascade </h5>
<br />

> Detecting faces and objects using HaarCascade classifiers: - python
```bash
cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
objects = cascade.detectMultiScale(imgGray)
for (x, y, w, h) in objects:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


```
---

<h5 align="center"> 7. HaarCascade Training and Testing </h5>
<br />

> Training classifiers for object detection: - python
```bash
video = cv2.VideoCapture(0)
cv2.imwrite(f'fotos/p/im{sample}.jpg', imgR)  # Capture positive images for training
```

<br />

> Testing with the trained classifier: - python
```bash
classifier = cv2.CascadeClassifier('cascade.xml')
camera = cv2.VideoCapture(0)
objects = classifier.detectMultiScale(imgGray, scaleFactor=1.2)

```
---

### 📦 How to Run the Project

> Clone the project repository
```bash
git clone https://github.com/ludiemert/Computer_Vision_Real_Projects_Opencv_Python.git
```

> Go to the project folder and install the dependencies
```bash
python your_file.py
```

---

### 📦 License

 - This project is licensed under the MIT License

---

### 📦 Contribution

 - Feel free to contribute by submitting pull requests or reporting issues.

---

- #### My LinkedIn - [![Linkedin Badge](https://img.shields.io/badge/-LucianaDiemert-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/lucianadiemert/)](https://www.linkedin.com/in/lucianadiemert/)

#### Contact

<img align="left" src="https://www.github.com/ludiemert.png?size=150">

#### [**Luciana Diemert**](https://github.com/ludiemert)

🛠 Full-Stack Developer <br>
📍 São Jose dos Campos – SP - Brazil

<a href="https://www.linkedin.com/in/lucianadiemert" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn Badge" height="25"></a>&nbsp;
<a href="mailto:lucianadiemert@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white" alt="Gmail Badge" height="25"></a>&nbsp;
<a href="#"><img src="https://img.shields.io/badge/Discord-%237289DA.svg?logo=discord&logoColor=white" title="LuDiem#0654" alt="Discord Badge" height="25"></a>&nbsp;
<a href="https://www.github.com/ludiemert" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white" alt="GitHub Badge" height="25"></a>&nbsp;

<br clear="left"/>

------------------

