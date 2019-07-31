#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import status
from .main import CustomResponse, SuccessResponse, ErrorResponse, ResultResponse


success = CustomResponse().response(SuccessResponse('Successfully Completed', status.HTTP_200_OK))
error = CustomResponse().response(ErrorResponse('Operation Faild', status.HTTP_400_BAD_REQUEST))
result = CustomResponse().response(ResultResponse({}, status.HTTP_200_OK))
