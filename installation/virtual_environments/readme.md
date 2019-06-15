# Virtual Envronment 
- What is virtual Environment? 

# Best practices 
- Usually all virtual environments should be under single folder(pydev or vdev) under home folder
- each version of python should be seperate namig, i put as py36, py27, py37 etc

# Redhat 

      mkdir ~/pydev
      cd ~/pydev
      python3 -m venv py36-venv
      source py36-venv/bin/activate

Adding in your bash script : 

      scl enable rh-python36 bash
      cd ~/pydev
      source py36-env/bin/activate

Deactivation : 
      
      deactivate
