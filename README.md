# SharePointEmbeddedManage

it's a simple management of SharePoint Embedded in order to easy manage the container and files in SPE

## How to use

1. Clone the repository
2. Install the requirements
   ```
   pip install -r requirements.txt
   ```
3. Change the variable under the `config.py` file with your SharePoint credentials
   ```
   ContainerTypeId = '<CONTAINER TYPE ID>';
   self._containerId = '<DEFAULT CONTAINER ID>'
   ```
4. Change the constant under the `getAuthorization.py` file file with your credentials

   ```
   TENANT_ID = '<TENANT ID>'
   CLIENT_ID = '<CLIENT ID'
   CLIENT_SECRET = '<CLIENT SECRET>'
   ```

5. Run the `main.py` file
