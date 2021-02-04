from azureml.core.webservice import Webservice
from azureml.core.image import ContainerImage


import os
from azureml.core.authentication import ServicePrincipalAuthentication
from azureml.core import Workspace


import AML 
aml = AML.AML()
ws = aml.ws


from azureml.core.model import Model
from sklearn.externals import joblib
mods = Model.list(ws, name=None, tags=None, properties=None, run_id=None, latest=False)
print(mods)
model_path = Model.get_model_path('diabetes', _workspace=ws)
print(model_path)
model = joblib.load(model_path)


from azureml.core.webservice import AciWebservice

aciconfig = AciWebservice.deploy_configuration(cpu_cores=1,
                                                   memory_gb=1,
                                                   tags={"data": "diabetes",
                                                         "method": "sklearn"},
                                                   description='Predict diabetes with sklearn')


# configure the image
image_config = ContainerImage.image_configuration(execution_script="score.py", 
                                                  runtime="python", 
                                                  conda_file="myenv.yml")

service = Webservice.deploy_from_model(workspace=ws,
                                       name='diabetes-svc',
                                       deployment_config=aciconfig,
                                       models=[mods[0]],
                                       image_config=image_config)

service.wait_for_deployment(show_output=True)

print(service.scoring_uri)