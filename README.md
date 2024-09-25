These commands are a Dockerfile for building a Docker image using Python 3.10 and setting it up so the application can run (it's probably Django, since it has a manage.py runserver command). Each command works as follows:


<img width="189" alt="ภาพถ่ายหน้าจอ 2567-09-25 เวลา 07 40 06" src="https://github.com/user-attachments/assets/7a8462cc-b44d-4bc3-8388-1caf7f054fd2">


Use Python version 3.10 as the base for building Docker images for use in containers. This is a starter that says it will use Python 3.10 from Docker Hub as the base.


<img width="238" alt="ภาพถ่ายหน้าจอ 2567-09-25 เวลา 07 46 24" src="https://github.com/user-attachments/assets/5aa9b073-7941-4f59-bfd5-ddddfe1fbc4a">


Set the environment variable PYTHONUNBUFFERED=1 to have Python display the text immediately, without waiting for the data to be full.


<img width="322" alt="ภาพถ่ายหน้าจอ 2567-09-25 เวลา 07 53 03" src="https://github.com/user-attachments/assets/73dd93fe-646d-426d-8aee-f83ab5305fd0">


Set the working folder in the container to `/code`. All commands from now on will be executed in this folder (just like changing folders on your computer).

<img width="310" alt="ภาพถ่ายหน้าจอ 2567-09-25 เวลา 07 56 43" src="https://github.com/user-attachments/assets/6a221acc-b04c-4d8a-9089-79012b549b9b">

Copy the `requirements.txt` file from your machine to the container in the `/code` folder. This file tells you what add-ons or packages the application needs to install.
