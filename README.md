## End to End Ml Project For AWS by Github

#### Create venv
```
conda create -p venv python==3.8 -y  
```

#### to activate Venv
```
conda activate venv/
```

#### install requirements
```
pip install -r requirements.txt
```

### create setup.py file to create packages 

````
from setuptools import find_packages,setup
````

### -e . 
use to initiate packages in setup.py


### Git pointing

create repository and follow steps

### To install kernel
````
pip install ipykernel
````

## For Deployment

1. Create folder name ".ebextenstions" in route directory 
2. create file under it name - 'python.config'
    ````
    option_settings:
    'aws:elasticbeanstalk:container:python'
    WSGIPATH: application:application
    ````
3. change name from app.py to application.py
4. Select beanstalk and create application #AWS Beanstalk
5. select codepipeline

AWS url - http://diamondprediction-env.eba-d2bssjkh.ap-south-1.elasticbeanstalk.com/predict