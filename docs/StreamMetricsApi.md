# pipeline_publisher_python.StreamMetricsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stream_metrics_get**](StreamMetricsApi.md#stream_metrics_get) | **GET** /stream_metrics | Fetches metrics about the stream


# **stream_metrics_get**
> InlineResponse200 stream_metrics_get(count_since_timestamp=count_since_timestamp)

Fetches metrics about the stream

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
api_instance = pipeline_publisher_python.StreamMetricsApi(pipeline_publisher_python.ApiClient(configuration))
count_since_timestamp = 'count_since_timestamp_example' # str | ISO 8601 compliant timestamp to perform message count calculations from. Example: 2018-04-12T23:54:57.595Z (optional)

try:
    # Fetches metrics about the stream
    api_response = api_instance.stream_metrics_get(count_since_timestamp=count_since_timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamMetricsApi->stream_metrics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count_since_timestamp** | **str**| ISO 8601 compliant timestamp to perform message count calculations from. Example: 2018-04-12T23:54:57.595Z | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

