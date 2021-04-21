"""
The handler function is the starting point of your code.
so, handler == fileName.functionName

Handler functions must always take two arguments, event and context
--------------------------------------------------------------------
# def lambda_handler(event, context):
#     ...
#     return some_value

* In this example, handler = 12_lambda.lambda_handler
-------------------------------------------------------------------

1. event:  data that's passed to the function upon execution. event can come from whatever triggers the lambda
if the lambda were triggered from an HTTP api call via API Gateway, then the event object would look something like this:

{
    "resource": "/",
    "path": "/",
    "httpMethod": "GET",
    "requestContext": {
        "resourcePath": "/",
        "httpMethod": "GET",
        "path": "/Prod/",
        ...
    },
    "headers": {
        "accept": "text/html",
        "accept-encoding": "gzip, deflate, br",
        "Host": "xxx.us-east-2.amazonaws.com",
        "User-Agent": "Mozilla/5.0",
        ...
    }
}

2. Context: It's main role is to provide information about the **current execution environment**. It is a Python objects that implements methods and has attributes.
Context methods:
get_remaining_time_in_millis – Returns the number of milliseconds left before the execution times out.

Context properties:
function_name – The name of the Lambda function.
function_version – The version of the function.
invoked_function_arn – The Amazon Resource Name (ARN) that's used to invoke the function. Indicates if the invoker specified a version number or alias.
memory_limit_in_mb – The amount of memory that's allocated for the function.
aws_request_id – The identifier of the invocation request.
log_group_name – The log group for the function.
log_stream_name – The log stream for the function instance.

"""