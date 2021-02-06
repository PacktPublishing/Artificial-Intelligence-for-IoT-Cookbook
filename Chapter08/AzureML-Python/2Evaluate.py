import os
from azureml.core.authentication import ServicePrincipalAuthentication
from azureml.core import Workspace
import AML 
aml = AML.AML()
ws = aml.ws



   

print("Found workspace {} at location {}".format(ws.name, ws.location))


from azureml.core import Experiment
experiment = Experiment(workspace=ws, name="diabetes-experiment")


minimum_rmse_runid = None
minimum_rmse = None

for run in experiment.get_runs():
    run_metrics = run.get_metrics()
    run_details = run.get_details()
    # each logged metric becomes a key in this returned dict
    run_rmse = run_metrics["rmse"]
    run_id = run_details["runId"]

    if minimum_rmse is None:
        minimum_rmse = run_rmse
        minimum_rmse_runid = run_id
    else:
        if run_rmse < minimum_rmse:
            minimum_rmse = run_rmse
            minimum_rmse_runid = run_id

print("Best run_id: " + minimum_rmse_runid)
print("Best run_id rmse: " + str(minimum_rmse))

from azureml.core import Run
best_run = Run(experiment=experiment, run_id=minimum_rmse_runid)
print(best_run.get_file_names())


best_run.download_file(name="model_alpha_0.1.pkl")

model = best_run.register_model(model_name='diabetes',
                           model_path='model_alpha_0.1.pkl')
print(model.name, model.id, model.version, sep='\t')