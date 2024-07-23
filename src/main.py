from config import Config, ContainerTypeId
from fileManagement import FileManagement
from containerManagement import ContainerManagement

# Fetch all containers
containerMgt = ContainerManagement()
allContainers = containerMgt.listContainers(ContainerTypeId=ContainerTypeId)

def selectContainer(containerIds):
    while True:
        try:
            selection = input("Enter the index of the container you want to select: [e to exit] ")
            if selection == "e":
                return None
            selection = int(selection)
            if 0 <= selection < len(containerIds):
                selectedContainer = list(containerIds[selection].items())[0]
                print(f"\033[94mSelected Container ID: {selectedContainer[0]}, Name: {selectedContainer[1]}\033[0m")
                return selectedContainer
            else:
                print("Invalid index, please try again.")
        except ValueError:
            print("Please enter a valid integer.")

# Manually select a container
selectedContainer = selectContainer(allContainers)

config = Config()
if(selectedContainer):
    config.setContainerId(selectedContainer[0])
    print(f"\033[92mSelected Container ID: {config.getContainerId()}\033[0m")
    fileManagement = FileManagement(config.getContainerId())
    print(f"\033[92m{'-'*102}\033[0m")
    print(f"1\tFetching items...\n2\tDeleting items...\n3\tPermanent deleting items...\n4\tFetching container quota...")
    print(f"\033[92m{'-'*102}\033[0m\n")
    while True:
        try:
            selection = input("Enter the operations you want to select[e to exit]: ")
            if selection == "e":
                break;
            selection = int(selection)
            if selection == 1:
                print("Fetching items...")
                fileManagement.fetchItems()
                break
            elif selection == 2:
                print("Deleting items...")
                fileManagement.deleteItems()
                break
            elif selection == 3:
                print("Permanent deleting items...")
                fileManagement.permanentDeleteItems()
                break
            elif selection == 4:
                print("Fetching container quota...")
                containerMgt.getDriveInfo(config.getContainerId())
                break
            else:
                print("Invalid index, please try again.")
        except ValueError:
            print("Please enter a valid integer.")
     
        