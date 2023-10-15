import os
import json
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

#Set environment variables for Azure managed identity
os.environ["AZURE_TENANT_ID"] = "provide the tenant id" 
os.environ["AZURE_CLIENT_ID"] = "provide the client id" 
os.environ["AZURE_CLIENT_SECRET"] = "provide the client secret" 

#Provide the details
subscription_id = 'provide subscription id'
resource_group = 'provide resource group info'
vm_name = 'test-vm'

#Set up Azure credentials
credential = DefaultAzureCredential()

#Create Compute Management Client
compute_client = ComputeManagementClient(credential, subscription_id)

#Fetch VM instance
vm_instance = compute_client.virtual_machines.get(resource_group, vm_name)

#Access metadata
metadata = vm_instance.instance_view.statuses[0].metadata

#convert metadat to JSON
metadata_json = json.dumps(metadata, indent=2)

print(metadata_json)

#Find a particular key info from the metadata file
with open(metadata_json, 'r') as json_file:
    json_data = json.load(metadata_json)
    par_data_key = 'resourceId'

    if par_data_key in json_data:
        value = json_data[par_data_key]
        print(f"The value of desired key is {value}")
    else:
        print(f"{par_data_key} is not available")