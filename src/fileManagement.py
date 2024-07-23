from os import path
import requests
import json
from datetime import datetime
from config import Config
from getAuthorization import getAuthorizationHeader


class FileManagement:
    def __init__(self,containerId:str=None):
        self.containerId = containerId
        self.speAuthorizationHeader = getAuthorizationHeader()

    def fetchFolders(self, containerId: str):
        getFoldersUrl=f"https://graph.microsoft.com/v1.0/drives/{containerId}/items?$expand=listitem($expand=fields)&$filter=listItem/contentType/name eq 'Folder'";
        response = requests.get(getFoldersUrl, headers=self.speAuthorizationHeader);
        if(response.status_code == 200):
            yield 'root' # Root folder (Default)
            for item in response.json()['value']:
                yield item['name']
        else:
            yield response.content;
    
    def fetchItems(self):
        getItemsUrl=f"https://graph.microsoft.com/v1.0/drives/{self.containerId}/items?$expand=listitem($expand=fields)&$filter=listItem/contentType/name eq 'Document'";

        response = requests.get(getItemsUrl, headers=self.speAuthorizationHeader);
        if(response.status_code == 200):
            formatted_now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            fileName=f'driveitems-{formatted_now}.json'
            itemPath =path.join("items",fileName)
            items= response.json();
            with open(itemPath, 'w') as outfile:
                json.dump(items, outfile,indent=4)
            print(f"\033[92mTotal {len(items['value'])} Items fetched successfully and saved to {path.abspath(itemPath)}\033[0m")
            return items
        else:
            print(response.content);
            throw("Failed to fetch items");

    def deleteItems(self):
        data = self.fetchItems();
        if(data is None):
            throw("Failed to fetch items")

        existFiles = [];
        for item in data['value']:
            deleteUrl = f"https://graph.microsoft.com/v1.0/drives/{self.containerId}/items/{item['id']}"
            print(deleteUrl)
            resp = requests.delete(deleteUrl, headers=self.speAuthorizationHeader)
            if(resp.status_code == 204):
                print(f"Deleted {item['id']} {item['name']}")
            else:
                print(resp.content);
                throw("Failed to delete file")
                existFiles.append(item['id'])

        if existFiles:
            print(f"Failed to delete files: {existFiles}")
        else: 
            print("All files deleted successfully")
    
    def permanentDeleteItems(self):
        data = self.fetchItems();

        if(data is None):
            throw("Failed to fetch items")
            
        existFiles = [];

        for item in data['value']:
            deleteUrl = f"https://graph.microsoft.com/v1.0/drives/{self.containerId}/items/{item['id']}/permanentDelete"
            print(deleteUrl)
            resp = requests.post(deleteUrl, headers=self.speAuthorizationHeader)
            if(resp.status_code == 204):
                print(f"\033[92mDeleted {item['id']} {item['name']}\033[0m")
            else:
                print(f"\033[91m{resp.content}\033[0m")  # Reset to default color at the end
                throw("Failed to delete file");
                existFiles.append(item['id'])

        if existFiles:
            print(f"\033[91mFailed to delete files: {existFiles}\033[0m")
        else:
            print("All files deleted successfully")