# coding: utf-8

"""
    API v1.0.1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse200MessagesReceived(object):
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
    swagger_types = {"since_timestamp": "str", "count": "int"}

    attribute_map = {"since_timestamp": "since_timestamp", "count": "count"}

    def __init__(self, since_timestamp=None, count=None):  # noqa: E501
        """InlineResponse200MessagesReceived - a model defined in Swagger"""  # noqa: E501

        self._since_timestamp = None
        self._count = None
        self.discriminator = None

        if since_timestamp is not None:
            self.since_timestamp = since_timestamp
        if count is not None:
            self.count = count

    @property
    def since_timestamp(self):
        """Gets the since_timestamp of this InlineResponse200MessagesReceived.  # noqa: E501


        :return: The since_timestamp of this InlineResponse200MessagesReceived.  # noqa: E501
        :rtype: str
        """
        return self._since_timestamp

    @since_timestamp.setter
    def since_timestamp(self, since_timestamp):
        """Sets the since_timestamp of this InlineResponse200MessagesReceived.


        :param since_timestamp: The since_timestamp of this InlineResponse200MessagesReceived.  # noqa: E501
        :type: str
        """

        self._since_timestamp = since_timestamp

    @property
    def count(self):
        """Gets the count of this InlineResponse200MessagesReceived.  # noqa: E501


        :return: The count of this InlineResponse200MessagesReceived.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this InlineResponse200MessagesReceived.


        :param count: The count of this InlineResponse200MessagesReceived.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if not isinstance(other, InlineResponse200MessagesReceived):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
