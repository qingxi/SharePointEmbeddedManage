
import json
import requests
from fileManagement import FileManagement
from getAuthorization import getAuthorizationHeader

class ContainerManagement:
    def __init__(self):
        self.specAuthorizationHeader = getAuthorizationHeader()
        self.fileManagement = FileManagement();

    def listContainers(self, ContainerTypeId):
        containerIds = [] # Make sure to set this to your actual container type ID
        url = f"https://graph.microsoft.com/beta/storage/fileStorage/containers?$filter=containerTypeId eq {ContainerTypeId}"
        resp = requests.get(url, headers=self.specAuthorizationHeader)
        if resp.status_code == 200:
            containers = resp.json()
            print(f"\033[92mTotal {len(containers['value'])} containers found.\033[0m")
            print(f"\033[92m{'-'*102}\033[0m")
            # Adjust the column widths as needed
            header_format = "\033[92m|\033[0m{:<8}\033[92m|\033[0m{:<40}\033[92m|\033[0m{:<50}\033[92m|\033[0m"
            row_format = "\033[92m|\033[0m{:<8}\033[92m|\033[0m{:<40}\033[92m|\033[0m{:<50}\033[92m|\033[0m"
            print(header_format.format("Index", "Container name", "Folder name"))
            print(f"\033[92m{'-'*102}\033[0m")
            for index, container in enumerate(containers['value']):
                containerIds.append({container['id']: container['displayName']})
                folders = self.fileManagement.fetchFolders(container['id'])
                # Ensure folders are joined by a semicolon and a space for better readability
                folders_str = '; '.join(folders)
                print(row_format.format(index, container['displayName'], folders_str))
                print(f"\033[92m{'-'*102}\033[0m")
        else:
            print(f"\033[91m{resp.content}\033[0m")
            raise Exception("Failed to fetch containers")
        return containerIds
    
    def getDriveInfo(self, containerId):
        url = f"https://graph.microsoft.com/beta/drives/{containerId}"
        resp = requests.get(url, headers=self.specAuthorizationHeader)
        if(resp.status_code == 200):
            driveInfo = resp.json()
            quota = json.dumps(driveInfo['quota'], indent=4)
            print(f"\033[92mContainer Id: {driveInfo['id']}\n quota: {quota}\033[0m")
        else:
            print(f"\033[91m{resp.content}\033[0m")  
            raise Exception("Failed to fetch drive info")