# Autogenerated. Do not modify.
#
# Profile: 21.60
from typing import List as list
from typing import Optional

from fit_tool.base_type import BaseType
from fit_tool.data_message import DataMessage
from fit_tool.definition_message import DefinitionMessage
from fit_tool.developer_field import DeveloperField
from fit_tool.endian import Endian
from fit_tool.field import Field


class SdmProfileMessage(DataMessage):
    ID = 5
    NAME = 'sdm_profile'

    @staticmethod
    def __get_field_size(definition_message: DefinitionMessage, field_id: int) -> int:
        size = 0
        if definition_message:
            field_definition = definition_message.get_field_definition(field_id)
            if field_definition:
                size = field_definition.size

        return size

    def __init__(self, definition_message=None, developer_fields=None, local_id: int = 0,
                 endian: Endian = Endian.LITTLE):
        super().__init__(name=SdmProfileMessage.NAME,
                         global_id=SdmProfileMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
                             MessageIndexField(
                                 size=self.__get_field_size(definition_message, MessageIndexField.ID),
                                 growable=definition_message is None),
                             SdmProfileEnabledField(
                                 size=self.__get_field_size(definition_message, SdmProfileEnabledField.ID),
                                 growable=definition_message is None),
                             SdmProfileSdmAntIdField(
                                 size=self.__get_field_size(definition_message, SdmProfileSdmAntIdField.ID),
                                 growable=definition_message is None),
                             SdmProfileSdmCalFactorField(
                                 size=self.__get_field_size(definition_message, SdmProfileSdmCalFactorField.ID),
                                 growable=definition_message is None),
                             SdmProfileOdometerField(
                                 size=self.__get_field_size(definition_message, SdmProfileOdometerField.ID),
                                 growable=definition_message is None),
                             SdmProfileSpeedSourceField(
                                 size=self.__get_field_size(definition_message, SdmProfileSpeedSourceField.ID),
                                 growable=definition_message is None),
                             SdmProfileSdmAntIdTransTypeField(
                                 size=self.__get_field_size(definition_message, SdmProfileSdmAntIdTransTypeField.ID),
                                 growable=definition_message is None),
                             SdmProfileOdometerRolloverField(
                                 size=self.__get_field_size(definition_message, SdmProfileOdometerRolloverField.ID),
                                 growable=definition_message is None)
                         ])

        self.growable = self.definition_message is None

    @classmethod
    def from_bytes(cls, definition_message: DefinitionMessage, developer_fields: list[DeveloperField],
                   bytes_buffer: bytes, offset: int = 0):
        message = cls(definition_message=definition_message, developer_fields=developer_fields)
        message.read_from_bytes(bytes_buffer, offset)
        return message

    @property
    def message_index(self) -> Optional[int]:
        field = self.get_field(MessageIndexField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @message_index.setter
    def message_index(self, value: int):
        field = self.get_field(MessageIndexField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def enabled(self) -> Optional[bool]:
        field = self.get_field(SdmProfileEnabledField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @enabled.setter
    def enabled(self, value: bool):
        field = self.get_field(SdmProfileEnabledField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def sdm_ant_id(self) -> Optional[int]:
        field = self.get_field(SdmProfileSdmAntIdField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @sdm_ant_id.setter
    def sdm_ant_id(self, value: int):
        field = self.get_field(SdmProfileSdmAntIdField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def sdm_cal_factor(self) -> Optional[float]:
        field = self.get_field(SdmProfileSdmCalFactorField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @sdm_cal_factor.setter
    def sdm_cal_factor(self, value: float):
        field = self.get_field(SdmProfileSdmCalFactorField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def odometer(self) -> Optional[float]:
        field = self.get_field(SdmProfileOdometerField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @odometer.setter
    def odometer(self, value: float):
        field = self.get_field(SdmProfileOdometerField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def speed_source(self) -> Optional[bool]:
        field = self.get_field(SdmProfileSpeedSourceField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @speed_source.setter
    def speed_source(self, value: bool):
        field = self.get_field(SdmProfileSpeedSourceField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def sdm_ant_id_trans_type(self) -> Optional[int]:
        field = self.get_field(SdmProfileSdmAntIdTransTypeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @sdm_ant_id_trans_type.setter
    def sdm_ant_id_trans_type(self, value: int):
        field = self.get_field(SdmProfileSdmAntIdTransTypeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def odometer_rollover(self) -> Optional[int]:
        field = self.get_field(SdmProfileOdometerRolloverField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @odometer_rollover.setter
    def odometer_rollover(self, value: int):
        field = self.get_field(SdmProfileOdometerRolloverField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)


class MessageIndexField(Field):
    ID = 254

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='message_index',
            field_id=self.ID,
            base_type=BaseType.UINT16,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class SdmProfileEnabledField(Field):
    ID = 0

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='enabled',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class SdmProfileSdmAntIdField(Field):
    ID = 1

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='sdm_ant_id',
            field_id=self.ID,
            base_type=BaseType.UINT16Z,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class SdmProfileSdmCalFactorField(Field):
    ID = 2

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='sdm_cal_factor',
            field_id=self.ID,
            base_type=BaseType.UINT16,
            offset=0,
            scale=10,
            size=size,
            units='%',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class SdmProfileOdometerField(Field):
    ID = 3

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='odometer',
            field_id=self.ID,
            base_type=BaseType.UINT32,
            offset=0,
            scale=100,
            size=size,
            units='m',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class SdmProfileSpeedSourceField(Field):
    ID = 4

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='speed_source',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class SdmProfileSdmAntIdTransTypeField(Field):
    ID = 5

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='sdm_ant_id_trans_type',
            field_id=self.ID,
            base_type=BaseType.UINT8Z,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class SdmProfileOdometerRolloverField(Field):
    ID = 7

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='odometer_rollover',
            field_id=self.ID,
            base_type=BaseType.UINT8,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )