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
` <br />
  <br />
    <img src="3_separate_objects_img/3_recort_obj/3_colocar_retangulo_nos_obj_contorn.png" style="width: 45%; margin-right: 5%;" alt="3_colocar_retangulo_nos_obj_contorn">
    <img src="3_separate_objects_img/3_recort_obj/4_recortou_os_objteos_eaddpasta.png" style="width: 45%;" alt="4_recortou_os_objteos_eaddpasta">
</div>
---

<h4 align="center">4_Deteccao_obj_Haarcascade 🚀</h4>

<div align="center">
    <img src="4_Deteccao_obj_Haarcascade/4_img_Haarcascade/3 - detecta_face_front.png" style="width: 45%; margin-right: 5%;" alt="3 - detecta_face_front">
     <img src="4_Deteccao_obj_Haarcascade/4_img_Haarcascade/4 - detecta_eyes.png" style="width: 45%; margin-right: 5%;" alt="3 - detecta_face_front">
` <br />
  <br />
    <img src="4_Deteccao_obj_Haarcascade/4_img_HaarCascade_treinam_cap_img/1_capturar_fotos.png" style="width: 45%; margin-right: 5%;" alt="1_capturar_fotos">
    <img src="4_Deteccao_obj_Haarcascade/4_img_HaarCascade_treinam_cap_img/3_cascade.xml_ reconhec_obj.png" style="width: 45%;" alt="3_cascade.xml_ reconhec_obj">
</div>
---

<h4 align="center">5_Parking_Vacancies_Accountant 🚀</h4>

<div align="center">
    <img src="5_Parking_Vacancies_Accountant/01_img_JobCounter/01_mark_vacancies.png" style="width: 45%; margin-right: 5%;" alt="01_mark_vacancies">
     <img src="5_Parking_Vacancies_Accountant/01_img_JobCounter/04_video_checking_vacant_coordinates.png" style="width: 45%; margin-right: 5%;" alt="04_video_checking_vacant_coordinates">
` <br />
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

- <br />

<h4 align="center"> 2. Morphological Operations </h4>
<br />

- dilate: Expands white areas, useful for highlighting objects.
- erode: Reduces noise by shrinking white areas.
- MORPH_OPEN: Erosion followed by dilation, removing small noise.
- GaussianBlur: Applies a filter to smooth the image.
- MORPH_CLOSE: Dilation followed by erosion, filling in gaps.

---

### 🚀 Features

 - Register goal: Allows the user to enter a new goal.
 - List goals: Displays all registered goals and allows you to select which ones have been completed.
 - Completed goals: Displays only the goals that have been marked as completed.
 - Open goals: Lists the goals that have not yet been completed.
 - Delete goals: Allows you to delete goals selected by the user.
 - Save data: All goals are saved in a JSON file (goals.json).

---


### 📦 Pre-requisites

 - Node.js: Make sure you have Node.js installed on your machine.
 - NPM packages: The project uses the @inquirer/prompts and fs libraries for prompts and file manipulation.

---


### 📦 Project structure

 - Application's #Back-end with Node.js, you will learn to explore technologies such as Fastify, Zod, Docker Compose, Drizzle ORM and create the database schema and seed, as well as create some of the project's features: goals, pending goals and complete goals.<br>
 - The #Front-end of the project. Let's start by building the interfaces, creating various components, and then using tools such as Vite, Biome and TailwindCSS! <br>
 - Application with #API using React Query and form with React Hook Form 

---

# 🎨 Layout
You can view the project layout via the link below:
- [Layout Web](https://www.figma.com/design/OB4CuFIpikW8L0eUUGyMeJ/NLW-Pocket-JS-%E2%80%A2-in.orbit-(Community)?node-id=82-2&node-type=canvas&t=ZvhfxeRBENvJSQqV-0) (Remember that you need to have a Figma account🥰).

### 🔗 Useful links
- **Project Repository:** [https://github.com/ludiemert/Nlw_Pocket_Node_React.git](https://github.com/ludiemert/Nlw_Pocket_Node_React.git)
#### ✒️ Authors
- **Rocketseat**

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
## 🎁 Acknowledgements and dedications

* Thank you #Rocketseat team

