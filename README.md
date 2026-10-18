
# notion-python

This [SDK](https://github.com/sdk-fabric/notion-python) is managed by the [SDK Fabric](https://sdk-fabric.org/) project, a global infrastructure to
automatically generate SDKs for every API.

You can find more information about this SDK at [TypeHub](https://typehub.cloud/):
https://app.typehub.cloud/d/sdkfabric/notion

## Usage

```python
from sdk.client import Client

client = Client.build("[access_token]")

# Creates and appends new children blocks to the parent block or page specified.
response = client.block().appendChildren("notion-version", "block_id", Append_Block_Children_Request())

# Moves a block (including a page) to the trash.
response = client.block().delete("notion-version", "block_id")

# Retrieves a Block object using the ID specified.
response = client.block().get("notion-version", "block_id")

# Returns a paginated array of child block objects contained in the block (or page) using the ID specified.
response = client.block().getChildren("notion-version", "block_id", 1, "start_cursor")

# Updates the content of a block based on its type, or moves it to/from the trash.
response = client.block().update("notion-version", "block_id", Update_Block_Request())

# Creates an additional data source in an existing database.
response = client.data_source().create("notion-version", Create_Data_Source_Request())

# Retrieves a data source object, including its property schema.
response = client.data_source().get("notion-version", "data_source_id")

# Creates a database and its initial data source as a child of a page or the workspace.
response = client.database().create("notion-version", Create_Database_Request())

# Retrieves a database object, a container for one or more data sources, for a provided database ID.
response = client.database().get("notion-version", "database_id")

# Updates the attributes (title, description, icon, cover, parent, inline, trash and lock status) of a database.
response = client.database().update("notion-version", "database_id", Update_Database_Request())

# Creates a new page as a child of an existing page or data source.
response = client.page().create("notion-version", "filter_properties", Create_Page_Request())

# Retrieves a Page object using the ID specified.
response = client.page().get("notion-version", "filter_properties", "page_id")

# Retrieves the content of a page rendered as enhanced markdown.
response = client.page().getMarkdown("notion-version", True, "page_id")

# Retrieves a page property item.
response = client.page().getProperty("notion-version", "page_id", 1, "property_id", "start_cursor")

# Moves an existing page to a new parent page or data source.
response = client.page().move("notion-version", "page_id", Move_Page_Request())

# Updates page properties, icon, cover, lock state or trash status (in_trash).
response = client.page().update("notion-version", "filter_properties", "page_id", Update_Page_Request())

# Updates or replaces content in a page using enhanced markdown.
response = client.page().updateMarkdown("notion-version", "page_id", Update_Page_Markdown_Request())

# Retrieves a User using the ID specified.
response = client.user().get("notion-version", "user_id")

# Returns a paginated list of Users for the workspace.
response = client.user().getAll("notion-version", 1, "start_cursor")

# Retrieves the bot User associated with the API token provided in the authorization header.
response = client.user().getMe("notion-version")
```
