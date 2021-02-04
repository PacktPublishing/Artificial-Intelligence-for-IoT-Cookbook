import os
from azureml.core.authentication import ServicePrincipalAuthentication
from azureml.core import Workspace

from configparser import SafeConfigParser


class AML:
  def __init__(self):

    parser = SafeConfigParser()
    parser.read('config.ini')

    svc_pr = ServicePrincipalAuthentication(
    tenant_id=parser.get('SP', 'tenantid'),
    service_principal_id=parser.get('SP','service_principal_id'),
    service_principal_password=parser.get('SP', 'password'))


    ws = Workspace(
    subscription_id=parser.get('AML', 'subscription_id'),
    resource_group=parser.get('AML', 'resource_group'),
    workspace_name=parser.get('AML', 'workspace_name'),
    auth=svc_pr
    )
    self.ws = ws

