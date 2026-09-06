
# notion-python

This [SDK](https://github.com/sdk-fabric/notion-python) is managed by the [SDK Fabric](https://sdk-fabric.org/) project, a global infrastructure to
automatically generate SDKs for every API.

You can find more information about this SDK at [TypeHub](https://typehub.cloud/):
https://app.typehub.cloud/d/sdkfabric/notion

## Usage

```python
from sdk.client import Client

client = Client.build("[access_token]")

# Returns a paginated list of Users for the workspace.
response = client.user().get_all("notion_version", "start_cursor", 1)

# Retrieves a User using the ID specified.
response = client.user().get("notion_version", "user_id")

# Retrieves a database object — information that describes the structure and columns of a database — for a provided database ID.
response = client.database().get("notion_version", "database_id")

# Retrieves a Page object using the ID specified.
response = client.page().get("page_id")

# Creates a new page that is a child of an existing page or database.
response = client.page().create(Page())
```
