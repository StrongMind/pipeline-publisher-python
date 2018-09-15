# coding: utf-8

"""
    API v1.0.2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from pipeline_publisher_python.models.inline_response_200_messages_received import (
    InlineResponse200MessagesReceived
)  # noqa: F401,E501


class InlineResponse200(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {"messages_received": "InlineResponse200MessagesReceived"}

    attribute_map = {"messages_received": "messages_received"}

    def __init__(self, messages_received=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501

        self._messages_received = None
        self.discriminator = None

        if messages_received is not None:
            self.messages_received = messages_received

    @property
    def messages_received(self):
        """Gets the messages_received of this InlineResponse200.  # noqa: E501


        :return: The messages_received of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200MessagesReceived
        """
        return self._messages_received

    @messages_received.setter
    def messages_received(self, messages_received):
        """Sets the messages_received of this InlineResponse200.


        :param messages_received: The messages_received of this InlineResponse200.  # noqa: E501
        :type: InlineResponse200MessagesReceived
        """

        self._messages_received = messages_received

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
