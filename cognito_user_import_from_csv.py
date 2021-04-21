import boto3
import json
#import requests
#import csv
import subprocess
import os
import time

############################  README  ######################################################################################
######### we need to make sure of following things:                           ##############################################
######### 1. User_Pool_ID                                                     ##############################################
######### 2. IAM_ROLE_ARN ( iam role for cognito to send logs to cloudwatch ) ##############################################
######### 3. CSV file with correct headers(coulmns)                           ##############################################
######### 4. You can give any Name for Import_Job_Name                        ##############################################
######### 5. Python Version: python3                                          ##############################################
######### 6. We need to wait for importJob to get finished.                   ##############################################
#########    So,set sleep time based on how long it might take                ##############################################
#########    to import the users in CSV.                                      ##############################################
######### 7. New imported Users and their Sub ID is stored in                 ##############################################
#########    file NewImportedUsers.json                                       ##############################################
############################################################################################################################

Import_Job_Name = "MyImportJobnotworking"
User_Pool_ID = "eu-central-1_0000AAjurf"
IAM_ROLE_ARN = "arn:aws:iam::00000000000:role/service-role/Cognito-UserImport-Role"
filelocation = "/import-cognito-users.csv"

client = boto3.client('cognito-idp')

##### create User Import Job and get presigned URL and JObID #####
def createImportJob():
    response = client.create_user_import_job(
        JobName=Import_Job_Name,
        UserPoolId=User_Pool_ID,
        CloudWatchLogsRoleArn=IAM_ROLE_ARN
    )
    return response

##### list User import JOb #####
def ListImportJob():
    response = client.list_user_import_jobs(
    UserPoolId=User_Pool_ID,
    MaxResults=1,
    #PaginationToken='string'
    )
    return response

##### Upload CSV file to import Job URL using PUT request method #####
def uploadCSV():
    y = subprocess.call('curl -v -T "%s" -H "x-amz-server-side-encryption:aws:kms" "%s"'% (filelocation, PreSignedUrl),shell=True)
    return y

##### Start the import user job #####
def startImport():
    response = client.start_user_import_job(
    UserPoolId=User_Pool_ID,
    JobId=JobID
    )
    return response

##### list all available users in cognito #####
def listUsers():
    response = client.list_users(
    UserPoolId=User_Pool_ID,
    AttributesToGet=[
        'email',
        'sub'
    ],
    #Limit=123,
    #Filter='string'
    )
    return response

##### extract user's email and sub ID from cognito users list #####
def getUserDetails(UserfileName):
    users = listUsers()
    emails=[]
    useremail = None
    usersub = None
    for user in users["Users"]:
        #print(user["Username"])
        for attribute in user["Attributes"]:
            if attribute["Name"] == "sub":
                usersub=attribute["Value"]        
            if attribute["Name"] == "email":
                useremail=attribute["Value"]

                emails.append({useremail : usersub})
    # print(json.dumps(emails, indent=4))
    with open(UserfileName, 'w', encoding='utf-8') as f:
        f.write(json.dumps(emails, indent=4))
        f.close

def ImportedUsersDetails():
    getUserDetails("UsersAfterImport.json")   #get all users(now contains imported users too) in cognito and write to file UsersBeforImport.json
    subprocess.call('grep -vxFf UsersBeforeImport.json UsersAfterImport.json > NewImportedUsers.json',shell=True)  #compare files and take unique fields only  

def checkImportStatus():
    y=ListImportJob()
    for x in y['UserImportJobs']:
        if x['Status'] == 'Pending' or x['Status'] == 'InProgress':
            time.sleep(10)
            checkImportStatus()
        if x['Status'] == 'Failed' or x['Status'] == 'Succeeded':
            ImportedUsersDetails()
            print("Import Suceed")     

getUserDetails("UsersBeforeImport.json")  #get all existing users in cognito and write to file UsersBeforImport.json

call = createImportJob()
PreSignedUrl = call['UserImportJob']['PreSignedUrl'] #extract presignedUrl form dictionary return value
JobID = call['UserImportJob']['JobId']               ##extract JobID form dictionary return value

# print("Presigned URL: ", PreSignedUrl, "\n")
# print("Job ID:  ", JobID)


uploadCSV()
startImport()

#print(json.dumps(ListImportJob(), indent=4, sort_keys=True, default=str))
#time.sleep(5)  # sleep is required to wait till the import job finishes. Otherwise we will miss to write some imported users to file.


checkImportStatus()
