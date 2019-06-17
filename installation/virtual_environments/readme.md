# Virtual Envronment 
- What is virtual Environment? 

# Python 3+ 
- package name venv

# Best practices 
- Usually all virtual environments should be under single folder(pydev or vdev) under home folder
- each version of python should be seperate namig, i put as py36, py27, py37 etc

# Windows
- Install 
      
      pip install venv
      
- configure , create a folder in a suitable directory and run 

      python -m venv your_path
 Example : I am creating in my home root under folder py37dev
 
      python -m venv %systemdrive%%homepath%\py37dev
      
      


# Redhat 

venv comes default python3 installations. 

# Ubuntu/debian  

sudo apt-get install python3-venv

# Settings 

      mkdir ~/pydev
      cd ~/pydev
      python3 -m venv py36-venv
      source py36-venv/bin/activate

Adding in your bash script : 

      scl enable rh-python36 bash
      cd ~/pydev
      source py36-env/bin/activate

Deactivation : (only active when you are inside venv)
      
      deactivate

Delete existing envirnment : 

      venv --clear
