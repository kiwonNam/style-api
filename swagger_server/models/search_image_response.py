# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.image import Image  # noqa: F401,E501
from swagger_server import util


class SearchImageResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, message: str=None, data: List[Image]=None):  # noqa: E501
        """SearchImageResponse - a model defined in Swagger

        :param message: The message of this SearchImageResponse.  # noqa: E501
        :type message: str
        :param data: The data of this SearchImageResponse.  # noqa: E501
        :type data: List[Image]
        """
        self.swagger_types = {
            'message': str,
            'data': List[Image]
        }

        self.attribute_map = {
            'message': 'message',
            'data': 'data'
        }

        self._message = message
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'SearchImageResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SearchImageResponse of this SearchImageResponse.  # noqa: E501
        :rtype: SearchImageResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self) -> str:
        """Gets the message of this SearchImageResponse.


        :return: The message of this SearchImageResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this SearchImageResponse.


        :param message: The message of this SearchImageResponse.
        :type message: str
        """

        self._message = message

    @property
    def data(self) -> List[Image]:
        """Gets the data of this SearchImageResponse.


        :return: The data of this SearchImageResponse.
        :rtype: List[Image]
        """
        return self._data

    @data.setter
    def data(self, data: List[Image]):
        """Sets the data of this SearchImageResponse.


        :param data: The data of this SearchImageResponse.
        :type data: List[Image]
        """

        self._data = data
