# pipeline_publisher_python.MessagesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**messages_post**](MessagesApi.md#messages_post) | **POST** /messages | Creates a message on the pipeline


# **messages_post**
> messages_post(message)

Creates a message on the pipeline

### Example
```python
from __future__ import print_function
import time
import pipeline_publisher_python
from pipeline_publisher_python.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = pipeline_publisher_python.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pipeline_publisher_python.MessagesApi(pipeline_publisher_python.ApiClient(configuration))
message = pipeline_publisher_python.Message() # Message | Note: At least one key/value pair for identifiers field is required.

try:
    # Creates a message on the pipeline
    api_instance.messages_post(message)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | [**Message**](Message.md)| Note: At least one key/value pair for identifiers field is required. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

