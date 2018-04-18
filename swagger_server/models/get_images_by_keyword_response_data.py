# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.simple_image import SimpleImage  # noqa: F401,E501
from swagger_server import util


class GetImagesByKeywordResponseData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, total_count: str=None, images: List[SimpleImage]=None):  # noqa: E501
        """GetImagesByKeywordResponseData - a model defined in Swagger

        :param total_count: The total_count of this GetImagesByKeywordResponseData.  # noqa: E501
        :type total_count: str
        :param images: The images of this GetImagesByKeywordResponseData.  # noqa: E501
        :type images: List[SimpleImage]
        """
        self.swagger_types = {
            'total_count': str,
            'images': List[SimpleImage]
        }

        self.attribute_map = {
            'total_count': 'total_count',
            'images': 'images'
        }

        self._total_count = total_count
        self._images = images

    @classmethod
    def from_dict(cls, dikt) -> 'GetImagesByKeywordResponseData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetImagesByKeywordResponse_data of this GetImagesByKeywordResponseData.  # noqa: E501
        :rtype: GetImagesByKeywordResponseData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def total_count(self) -> str:
        """Gets the total_count of this GetImagesByKeywordResponseData.


        :return: The total_count of this GetImagesByKeywordResponseData.
        :rtype: str
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count: str):
        """Sets the total_count of this GetImagesByKeywordResponseData.


        :param total_count: The total_count of this GetImagesByKeywordResponseData.
        :type total_count: str
        """

        self._total_count = total_count

    @property
    def images(self) -> List[SimpleImage]:
        """Gets the images of this GetImagesByKeywordResponseData.


        :return: The images of this GetImagesByKeywordResponseData.
        :rtype: List[SimpleImage]
        """
        return self._images

    @images.setter
    def images(self, images: List[SimpleImage]):
        """Sets the images of this GetImagesByKeywordResponseData.


        :param images: The images of this GetImagesByKeywordResponseData.
        :type images: List[SimpleImage]
        """

        self._images = images
