## About the connector
Cloudflare helps to automatically scan the entire public internet,  including DDoS protection, web application firewall, bot management, encryption, DNS security, access control, and rate limiting, to safeguard websites and online applications from various cyber threats.
<p>This document provides information about the Cloudflare Connector, which facilitates automated interactions, with a Cloudflare server using FortiSOAR&trade; playbooks. Add the Cloudflare Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Cloudflare.</p>

### Version information

Connector Version: 1.1.0


Authored By: spryIQ.co

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-cloudflare`

## Prerequisites to configuring the connector
- You must have the URL of Cloudflare server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Cloudflare server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Cloudflare</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Specify the URL of the cloudflare WAF server to connect and perform automated operations.<br>
<tr><td>Account ID<br></td><td>Specify the Account ID to access the endpoint to which you will connect and perform the automated operations.<br>
<tr><td>Zone ID<br></td><td>Specify the Zone ID to access the endpoint to which you will connect and perform the automated operations.<br>
<tr><td>API Key<br></td><td>Specify the Global API Key to access the endpoint to which you will connect and perform the automated operations.<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Create Firewall Rule<br></td><td>Allows users to add or create a new firewall rule in a firewall configuration<br></td><td>create_firewall_rule <br/>Investigation<br></td></tr>
<tr><td>Update Firewall Rule<br></td><td>Allows users to modify or edit an existing firewall rule within the firewall configuration<br></td><td>update_firewall_rule <br/>Investigation<br></td></tr>
<tr><td>List Firewall Rules<br></td><td>Get a list of firewall rules that are currently configured for your Cloudflare account or for a specific domain or zone within your account<br></td><td>list_firewall_rules <br/>Investigation<br></td></tr>
<tr><td>Delete Firewall Rule<br></td><td>Remove or delete an existing firewall rule from the firewall configuration<br></td><td>delete_firewall_rule <br/>Investigation<br></td></tr>
<tr><td>Create Filter<br></td><td>Allows users to add a new filter to their WAF configuration<br></td><td>create_filter <br/>Investigation<br></td></tr>
<tr><td>List Filters<br></td><td>Retrieve a list of filters configured within the Cloudflare Web Application Firewall (WAF) settings<br></td><td>list_filters <br/>Investigation<br></td></tr>
<tr><td>Update Filter<br></td><td>Modify and update the configuration settings of existing filters within their WAF configuration<br></td><td>update_filter <br/>Investigation<br></td></tr>
<tr><td>Delete Filter<br></td><td>Allows users to remove a specific filter from their WAF configuration.<br></td><td>delete_filter <br/>Investigation<br></td></tr>
<tr><td>List Zones<br></td><td>Retrieves a list of all zones associated with the user's Cloudflare account<br></td><td>list_zones <br/>Investigation<br></td></tr>
<tr><td>Get IP Lists<br></td><td>Allows users to retrieve information about IP lists configured within their Cloudflare account<br></td><td>get_ip_lists <br/>Investigation<br></td></tr>
<tr><td>Create IP List<br></td><td>Create a new IP list with a specified name and associated IP addresses.<br></td><td>create_ip_list <br/>Investigation<br></td></tr>
<tr><td>Delete IP List<br></td><td>Remove an existing IP list from their Cloudflare account<br></td><td>delete_ip_list <br/>Investigation<br></td></tr>
<tr><td>Create IP Items List<br></td><td>Add or append new items, such as IP addresses, to a specific list<br></td><td>create_ip_items_list <br/>Investigation<br></td></tr>
<tr><td>Get IP List Items<br></td><td>Retrieves the list of IP addresses items from a specific list<br></td><td>get_ip_list_item <br/>Investigation<br></td></tr>
<tr><td>Update IP List Items<br></td><td>Removes all existing items from the list and adds the provided items to the list.<br></td><td>update_ip_list_item <br/>Investigation<br></td></tr>
<tr><td>Delete IP List Items<br></td><td>Allows users to remove specific items, such as IP addresses, from an IP list<br></td><td>delete_ip_list_item <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Create Firewall Rule
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Description<br></td><td>Specify a description or name for the new firewall rule being created<br>
</td></tr><tr><td>Action<br></td><td>Specify the action or behavior to be taken when the rule's conditions are met<br>
</td></tr><tr><td>Products<br></td><td>Select one or more products or services to which the firewall rule applies<br>
</td></tr><tr><td>Paused<br></td><td>Specify whether the newly created firewall rule should be initially paused or inactive<br>
</td></tr><tr><td>Priority<br></td><td>Specify the precedence or order of the newly created firewall rule relative to other rules<br>
</td></tr><tr><td>Reference Tag<br></td><td>Specify an association of a reference or identifier with the newly created firewall rule<br>
</td></tr><tr><td>Filter ID<br></td><td>Specify the identifier of an existing filter to be associated with the newly created firewall rule. Required if filter_expression is unspecified.<br>
</td></tr><tr><td>Filter Expression<br></td><td>Specify the identifier of an existing filter to be associated with the newly created firewall rule. Required if filter_expression is unspecified. more info: https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/'<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "errors": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "action": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "paused": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "priority": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "products": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ref": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "filter": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "expression": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "paused": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "ref": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "success": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result_info": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "per_page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "total_count": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Update Firewall Rule
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Rule ID<br></td><td>Specify the unique identifier of the firewall rule that needs to be updated.<br>
</td></tr><tr><td>Description<br></td><td>Specify the description or name of the existing firewall rule to modify or update<br>
</td></tr><tr><td>Action<br></td><td>Specify the action or behavior to be taken when the updated rule's conditions are met<br>
</td></tr><tr><td>Products<br></td><td>Select one or more products or services to which the updated firewall rule applies<br>
</td></tr><tr><td>Paused<br></td><td>To update a firewall rule, it can be set to either active or inactive. To choose this option, the firewall rule must be paused or inactive<br>
</td></tr><tr><td>Priority<br></td><td>Specify the precedence or order of the firewall rules to be updated<br>
</td></tr><tr><td>Reference Tag<br></td><td>Specify a reference or identifier for the firewall rule to be updated<br>
</td></tr><tr><td>Filter ID<br></td><td>Specifies the identifier of an existing filter to be associated with the updated firewall rule. Can not update or delete rule filter, only add a new filter<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "errors": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "action": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "paused": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "priority": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "products": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ref": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "filter": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "expression": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "paused": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "ref": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "success": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result_info": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "per_page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "total_count": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: List Firewall Rules
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Action<br></td><td>Specifies the action or operation to be performed when retrieving firewall rules. Must be an exact match<br>
</td></tr><tr><td>Description<br></td><td>Specify this parameter allows you to filter firewall rules based on their description or name<br>
</td></tr><tr><td>Rule ID<br></td><td>Specify the unique identifier of the firewall rule<br>
</td></tr><tr><td>Paused<br></td><td>Specify this parameter value true, indicates that the firewall rule is currently paused<br>
</td></tr><tr><td>Page Number<br></td><td>Specify the page number of paginated results<br>
</td></tr><tr><td>Record Per Page<br></td><td>Specify this parameter to indicate the number of firewall rules per page<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "errors": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "action": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "paused": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "priority": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "products": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ref": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "filter": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "expression": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "paused": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "ref": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "success": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result_info": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "per_page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "total_count": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Delete Firewall Rule
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Rule ID<br></td><td>Specify the unique identifier of the firewall rule to delete<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "errors": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "action": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "paused": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "priority": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "products": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ref": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "filter": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "expression": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "paused": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "ref": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "success": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result_info": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "per_page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "total_count": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Create Filter
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Zone ID<br></td><td>Specifies the unique identifier of the Cloudflare zone where the filter will be applied<br>
</td></tr><tr><td>Description<br></td><td>Allows users to provide a description or additional information about the newly created filter<br>
</td></tr><tr><td>Expression<br></td><td>Specify this parameter allows users to define the filtering criteria or rules for the newly created filter<br>
</td></tr><tr><td>Reference ID<br></td><td>Specifying this parameter allows users to associate a reference or identifier with the newly created filter<br>
</td></tr><tr><td>Paused<br></td><td>Specifying this parameter allows users to specify whether the newly created filter should be initially paused or active<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "errors": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "expression": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "paused": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ref": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "success": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result_info": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "per_page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "total_count": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: List Filters
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Filter ID<br></td><td>Specify the identifier of a specific filter for retrieval.<br>
</td></tr><tr><td>Description<br></td><td>Allows users to filter the list of filters based on their descriptions<br>
</td></tr><tr><td>Expression<br></td><td>Specify a search expression or pattern to filter the list of filters returned by the Cloudflare WAF<br>
</td></tr><tr><td>Reference ID<br></td><td>Specifying this parameter allows users to filter the list of filters based on their reference or identifier.<br>
</td></tr><tr><td>Page Number<br></td><td>Specify the page number of paginated results<br>
</td></tr><tr><td>Per Page<br></td><td>Specify this parameter to indicate the number of filters per page<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "errors": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "expression": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "paused": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ref": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "success": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result_info": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "per_page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "total_count": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Update Filter
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Filter ID<br></td><td>Specifies the unique identifier of the filter that the user intends to update<br>
</td></tr><tr><td>Zone ID<br></td><td>Specifies this parameter facilitates the modification of the Cloudflare zone to which a specific filter is associated<br>
</td></tr><tr><td>Description<br></td><td>Specifying this parameter allows users to update the description or additional information associated with a specific filter<br>
</td></tr><tr><td>Expression<br></td><td>Specifying this parameter allows users to modify the filtering criteria or rules associated with a specific filter<br>
</td></tr><tr><td>Reference ID<br></td><td>Specifying this parameter allows users to modify or update the reference or identifier associated with a specific filter<br>
</td></tr><tr><td>Paused<br></td><td>Provides users with the ability to control the activation status of a specific filter<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "errors": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "expression": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "paused": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ref": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "success": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result_info": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "per_page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "total_count": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Delete Filter
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Filter ID<br></td><td>Specifies the unique identifier of the filter that users want to remove from their WAF configuration<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "errors": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "expression": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "paused": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ref": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "success": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result_info": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "per_page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "total_count": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: List Zones
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Match<br></td><td>Specifies this parameter is used to filter the list of zones based on specific criteria<br>
</td></tr><tr><td>Name<br></td><td>Specifying this parameter allows users to filter the list of zones based on the zone name<br>
</td></tr><tr><td>Account Name<br></td><td>Specifying this parameter allows users to filter the list of zones based on the name of the Cloudflare account associated with each zone<br>
</td></tr><tr><td>Order<br></td><td>Specifying this parameter allows users to specify the order in which the list of zones should be sorted in the response. Possible values :
name
status
account.id
account.name<br>
</td></tr><tr><td>Status<br></td><td>Specifying this parameter allows users to filter the list of zones based on their current operational status<br>
</td></tr><tr><td>Direction<br></td><td>Specifying this parameter allows users to specify the sorting direction of the list of zones based on certain criteria<br>
</td></tr><tr><td>Page Number<br></td><td>Specify the page number of paginated results<br>
</td></tr><tr><td>Per Page<br></td><td>Specify this parameter to indicate the number of zones per page<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "errors": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "success": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result_info": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "per_page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "total_count": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "account": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "name": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "activated_on": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "created_on": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "development_mode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "meta": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "cdn_only": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "custom_certificate_quota": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "dns_only": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "foundation_dns": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "page_rule_quota": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "phishing_detected": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "step": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "modified_on": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "original_dnshost": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "original_name_servers": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "original_registrar": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "owner": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "type": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "vanity_name_servers": []
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ]
</code><code><br>}</code>

### operation: Get IP Lists
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Page Number<br></td><td>Specify the page number of paginated results<br>
</td></tr><tr><td>Per Page<br></td><td>Specify this parameter to indicate the number of IP list items per page<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "errors": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "created_on": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "kind": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "modified_on": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "num_items": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "num_referencing_filters": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "success": true
</code><code><br>}</code>

### operation: Create IP List
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Name<br></td><td>Specifies the name of the new IP list to be created<br>
</td></tr><tr><td>Description<br></td><td>Specify this parameter to allows users to provide additional information or details about the new IP list being created<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "errors": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "0": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "created_on": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "kind": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "modified_on": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "num_items": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "num_referencing_filters": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "success": ""
</code><code><br>}</code>

### operation: Delete IP List
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>List ID<br></td><td>Specifies the ID of the list that you want to delete<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "errors": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "0": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "id": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "success": ""
</code><code><br>}</code>

### operation: Create IP Items List
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>List ID<br></td><td>Specifies the ID of the list from which you want to add or append as new items to the list.<br>
</td></tr><tr><td>IP Address<br></td><td>Specifies a CSV list of IP addresses that you want to add or append as new items to the list.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "errors": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "0": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "operation_id": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "success": ""
</code><code><br>}</code>

### operation: Get IP List Items
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>List ID<br></td><td>Specifies the ID of the list from which you want to retrieve the list of IP addresses.<br>
</td></tr><tr><td>Page Number<br></td><td>Specify the page number of paginated results<br>
</td></tr><tr><td>Record Per Page<br></td><td>Specify this parameter to indicate the number of IP list item per page<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "errors": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "comment": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "created_on": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ip": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "modified_on": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "success": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result_info": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "cursors": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "after": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "before": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Update IP List Items
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>List ID<br></td><td>Specifies the ID of the list from which you want to update the list of IP addresses.<br>
</td></tr><tr><td>IP Address<br></td><td>Specifies a CSV list of IP addresses that you want to update within the item list<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "errors": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "0": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "operation_id": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "success": ""
</code><code><br>}</code>

### operation: Delete IP List Items
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>List ID<br></td><td>Specifies the ID of the list from which you want to delete the IP list<br>
</td></tr><tr><td>Item ID<br></td><td>Specifies a CSV list of items ID that you want to delete from the list.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "errors": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "messages": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "0": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "operation_id": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "success": ""
</code><code><br>}</code>
## Included playbooks
The `Sample - cloudflare - 1.1.0` playbook collection comes bundled with the Cloudflare connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Cloudflare connector.

- Create Firewall Rule
- Update Firewall Rule
- List Firewall Rules
- Delete Firewall Rule
- Create Filter
- List Filters
- Update Filter
- Delete Filter
- List Zones
- Get IP Lists
- Create IP List
- Delete IP List
- Create IP Items List
- Get IP List Items
- Update IP List Items
- Delete IP List Items

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
