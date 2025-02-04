from typing import Optional, Union, Literal

from pydantic import BaseModel

from anova_wifi.device import DeviceState
from anova_wifi.event import AnovaEvent
from commands import TemperatureUnit

OkResponse = Literal['ok']


class SSEEvent(BaseModel):
    event_type: str
    device_id: Optional[str] = None
    payload: Optional[Union[AnovaEvent, DeviceState]] = None


class DeviceInfo(BaseModel):
    id: str
    version: Optional[str]
    device_number: Optional[str]


class TemperatureResponse(BaseModel):
    temperature: float


class SetTemperatureResponse(BaseModel):
    changed_to: float


class GetTargetTemperatureResponse(BaseModel):
    temperature: float


class SetTimerResponse(BaseModel):
    message: str
    minutes: int


class UnitResponse(BaseModel):
    unit: Optional[TemperatureUnit]


class SpeakerStatusResponse(BaseModel):
    speaker_status: bool


class TimerResponse(BaseModel):
    timer: int


class BLEDevice(BaseModel):
    address: str
    name: str


class NewSecretResponse(BaseModel):
    secret_key: str


class BLEDeviceInfo(BaseModel):
    ble_address: str
    ble_name: str
    version: str
    id_card: str
    temperature_unit: TemperatureUnit
    speaker_status: bool
