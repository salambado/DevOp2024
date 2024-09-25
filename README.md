These commands are a Dockerfile for building a Docker image using Python 3.10 and setting it up so the application can run (it's probably Django, since it has a manage.py runserver command). Each command works as follows:


<img width="189" alt="ภาพถ่ายหน้าจอ 2567-09-25 เวลา 07 40 06" src="https://github.com/user-attachments/assets/7a8462cc-b44d-4bc3-8388-1caf7f054fd2">


Use Python version 3.10 as the base for building Docker images for use in containers. This is a starter that says it will use Python 3.10 from Docker Hub as the base.


<img width="238" alt="ภาพถ่ายหน้าจอ 2567-09-25 เวลา 07 46 24" src="https://github.com/user-attachments/assets/5aa9b073-7941-4f59-bfd5-ddddfe1fbc4a">


Set the environment variable PYTHONUNBUFFERED=1 to have Python display the text immediately, without waiting for the data to be full.


<img width="322" alt="ภาพถ่ายหน้าจอ 2567-09-25 เวลา 07 53 03" src="https://github.com/user-attachments/assets/73dd93fe-646d-426d-8aee-f83ab5305fd0">


Set the working folder in the container to `/code`. All commands from now on will be executed in this folder (just like changing folders on your computer).

<img width="310" alt="ภาพถ่ายหน้าจอ 2567-09-25 เวลา 07 56 43" src="https://github.com/user-attachments/assets/6a221acc-b04c-4d8a-9089-79012b549b9b">

Copy the `requirements.txt` file from your machine to the container in the `/code` folder. This file tells you what add-ons or packages the application needs to install.

<img width="370" alt="ภาพถ่ายหน้าจอ 2567-09-25 เวลา 07 57 23" src="https://github.com/user-attachments/assets/b15eb8bf-fc43-4bcb-a1e8-e188901adde0">

Install all the dependencies specified in the requirements.txt file using the pip command. This is the step to prepare the environment required for the app.

<img width="229" alt="ภาพถ่ายหน้าจอ 2567-09-25 เวลา 08 02 46" src="https://github.com/user-attachments/assets/3ab9b1bf-1aed-44a8-8c66-a785047d599c">

Copy all files from your local machine to the /code directory in the container, including all the application code.

<img width="245" alt="ภาพถ่ายหน้าจอ 2567-09-25 เวลา 08 05 28" src="https://github.com/user-attachments/assets/5f78b92d-1a8a-43cc-bdec-6663a9e2bbd4">

Open port 8000 in the container, which is the port on which the application (e.g. Django) will run. This specifies that the container can accept connections over this port.

<img width="435" alt="ภาพถ่ายหน้าจอ 2567-09-25 เวลา 08 05 41" src="https://github.com/user-attachments/assets/0835665e-82cc-4ad4-be8a-006f2d3bea33">

Specify the command to run when the container starts, in this case python manage.py runserver , which is Django's command to run the web server.




Docker Image.


<img width="262" alt="ภาพถ่ายหน้าจอ 2567-09-25 เวลา 08 17 13" src="https://github.com/user-attachments/assets/00a678a2-69e8-45db-abf2-3708ac7ac704">

1.docker compose up: This command is used to start the services defined in the docker-compose.yml file.

2.--build: This option is used to force Docker to rebuild a new Docker image for each service before starting the container, whether the image already exists or not.

In total, this command will:

-Read the docker-compose.yml file.

-Create a new image (if any changes) and run the specified container.
