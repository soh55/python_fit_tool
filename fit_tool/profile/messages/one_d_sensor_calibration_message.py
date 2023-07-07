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
from fit_tool.profile.profile_type import *
from fit_tool.sub_field import SubField


class OneDSensorCalibrationMessage(DataMessage):
    ID = 210
    NAME = 'one_d_sensor_calibration'

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
        super().__init__(name=OneDSensorCalibrationMessage.NAME,
                         global_id=OneDSensorCalibrationMessage.ID,
                         local_id=definition_message.local_id if definition_message else local_id,
                         endian=definition_message.endian if definition_message else endian,
                         definition_message=definition_message,
                         developer_fields=developer_fields,
                         fields=[
                             TimestampField(
                                 size=self.__get_field_size(definition_message, TimestampField.ID),
                                 growable=definition_message is None),
                             OneDSensorCalibrationSensorTypeField(
                                 size=self.__get_field_size(definition_message,
                                                            OneDSensorCalibrationSensorTypeField.ID),
                                 growable=definition_message is None),
                             OneDSensorCalibrationCalibrationFactorField(
                                 size=self.__get_field_size(definition_message,
                                                            OneDSensorCalibrationCalibrationFactorField.ID),
                                 growable=definition_message is None),
                             OneDSensorCalibrationCalibrationDivisorField(
                                 size=self.__get_field_size(definition_message,
                                                            OneDSensorCalibrationCalibrationDivisorField.ID),
                                 growable=definition_message is None),
                             OneDSensorCalibrationLevelShiftField(
                                 size=self.__get_field_size(definition_message,
                                                            OneDSensorCalibrationLevelShiftField.ID),
                                 growable=definition_message is None),
                             OneDSensorCalibrationOffsetCalField(
                                 size=self.__get_field_size(definition_message, OneDSensorCalibrationOffsetCalField.ID),
                                 growable=definition_message is None)
                         ])

        self.growable = self.definition_message is None

    @classmethod
    def from_bytes(cls, definition_message: DefinitionMessage, developer_fields: list[DeveloperField],
                   bytes_buffer: bytes, offset: int = 0):
        message = cls(definition_message=definition_message, developer_fields=developer_fields)
        message.read_from_bytes(bytes_buffer, offset)
        return message

    # timestamp : milliseconds from January 1st, 1970 at 00:00:00 UTC

    @property
    def timestamp(self) -> Optional[int]:
        field = self.get_field(TimestampField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    # timestamp : milliseconds from January 1st, 1970 at 00:00:00 UTC

    @timestamp.setter
    def timestamp(self, value: int):
        field = self.get_field(TimestampField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def sensor_type(self) -> Optional[SensorType]:
        field = self.get_field(OneDSensorCalibrationSensorTypeField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @sensor_type.setter
    def sensor_type(self, value: SensorType):
        field = self.get_field(OneDSensorCalibrationSensorTypeField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def calibration_factor(self) -> Optional[int]:
        field = self.get_field(OneDSensorCalibrationCalibrationFactorField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @calibration_factor.setter
    def calibration_factor(self, value: int):
        field = self.get_field(OneDSensorCalibrationCalibrationFactorField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def baro_cal_factor(self) -> Optional[int]:
        field = self.get_field(OneDSensorCalibrationCalibrationFactorField.ID)
        type_field = self.get_field(OneDSensorCalibrationSensorTypeField.ID)

        is_sub_field_valid = type_field and type_field.get_value() in [3]
        if field and field.is_valid() and is_sub_field_valid:
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @baro_cal_factor.setter
    def baro_cal_factor(self, value: int):
        field = self.get_field(OneDSensorCalibrationCalibrationFactorField.ID)
        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def calibration_divisor(self) -> Optional[int]:
        field = self.get_field(OneDSensorCalibrationCalibrationDivisorField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @calibration_divisor.setter
    def calibration_divisor(self, value: int):
        field = self.get_field(OneDSensorCalibrationCalibrationDivisorField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def level_shift(self) -> Optional[int]:
        field = self.get_field(OneDSensorCalibrationLevelShiftField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @level_shift.setter
    def level_shift(self, value: int):
        field = self.get_field(OneDSensorCalibrationLevelShiftField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)

    @property
    def offset_cal(self) -> Optional[int]:
        field = self.get_field(OneDSensorCalibrationOffsetCalField.ID)
        if field and field.is_valid():
            sub_field = field.get_valid_sub_field(self.fields)
            return field.get_value(sub_field=sub_field)
        else:
            return None

    @offset_cal.setter
    def offset_cal(self, value: int):
        field = self.get_field(OneDSensorCalibrationOffsetCalField.ID)

        if field:
            if value is None:
                field.clear()
            else:
                sub_field = field.get_valid_sub_field(self.fields)
                field.set_value(0, value, sub_field)


class TimestampField(Field):
    ID = 253

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='timestamp',
            field_id=self.ID,
            base_type=BaseType.UINT32,
            offset=-631065600000,
            scale=0.001,
            size=size,
            units='ms',
            type_name='date_time',
            growable=growable,
            sub_fields=[
            ]
        )


class OneDSensorCalibrationSensorTypeField(Field):
    ID = 0

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='sensor_type',
            field_id=self.ID,
            base_type=BaseType.ENUM,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class OneDSensorCalibrationCalibrationFactorField(Field):
    ID = 1

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='calibration_factor',
            field_id=self.ID,
            base_type=BaseType.UINT32,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
                SubField(
                    name='baro_cal_factor',
                    base_type=BaseType.UINT32,
                    scale=1,
                    offset=0,
                    units='Pa',
                    reference_map={
                        OneDSensorCalibrationSensorTypeField.ID: [3]
                    })
            ]
        )


class OneDSensorCalibrationCalibrationDivisorField(Field):
    ID = 2

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='calibration_divisor',
            field_id=self.ID,
            base_type=BaseType.UINT32,
            offset=0,
            scale=1,
            size=size,
            units='counts',
            type_name='',
            growable=growable,
            sub_fields=[
            ]
        )


class OneDSensorCalibrationLevelShiftField(Field):
    ID = 3

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='level_shift',
            field_id=self.ID,
            base_type=BaseType.UINT32,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )


class OneDSensorCalibrationOffsetCalField(Field):
    ID = 4

    def __init__(self, size: int = 0, growable: bool = True):
        super().__init__(
            name='offset_cal',
            field_id=self.ID,
            base_type=BaseType.SINT32,
            offset=0,
            scale=1,
            size=size,
            growable=growable,
            sub_fields=[
            ]
        )