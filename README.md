# DRF http response
A DRF http custom response

## Description
This a http response package for django rest framework custom response. This is only for any django projects which used drf for http response.

## Dependencies
Djago
DRF

## Uses
Install it by runing
- `pip install drf-http-response`

Import into your project
- `from drf_http_response import success, result, error`

Use it in your http response
- `return success.get_response(message='Successfully Completed', status=200)`

If you use any type of response without passing parameter into it. No problem it will always return a default message. For `result.get_response()` you can pass data or object as a message into it.
