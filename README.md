# SDCC_project_22-23
Final project for the course Distributed Systems &amp; Cloud Computing

☁️CLOUDY DAYS☁️

How to run our system?

- git clone https://github.com/AnastasiaBrinati/SDCC_project_22-23.git

and then executing the ansible-playbook

- ansible-playbook deployment-playbook.yml

Add an inventory if you like it, however for the purpose of this project we limited ourselves at executing only in localhost.

Disclaimer: we didn't care for security aspects, most passwords and passwkeys are hardcoded and visible.

### note to self: The playbook is still not working, problems with chmod ###

Per il deployment 'manuale' è sufficiente una macchina con minikube e fare il clone della repo

-spostarsi nella sottocartella /k8s
-kubectl apply -f .
-attendere/controllare che i pods siano tutti running
-kubctl get pods
-minikube tunnel
