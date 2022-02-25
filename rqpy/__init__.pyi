from typing import Optional, List


class Packet:
    @property
    def seq_id(self) -> int: ...

    @property
    def command_name(self) -> str: ...

    @property
    def message(self) -> str: ...

    @property
    def body(self) -> bytes: ...

    @property
    def uin(self) -> int: ...


class OSVersion:
    @property
    def incremental(self) -> str: ...

    @property
    def release(self) -> str: ...

    @property
    def codename(self) -> str: ...

    @property
    def sdk(self) -> int: ...


class Device:
    @staticmethod
    def __init__() -> Device: ...

    @staticmethod
    def random() -> Device: ...

    @staticmethod
    def from_str(str) -> Device: ...

    def to_str(self) -> str: ...

    @property
    def display(self) -> str: ...

    @property
    def product(self) -> str: ...

    @property
    def device(self) -> str: ...

    @property
    def board(self) -> str: ...

    @property
    def model(self) -> str: ...

    @property
    def finger_print(self) -> str: ...

    @property
    def boot_id(self) -> str: ...

    @property
    def proc_version(self) -> str: ...

    @property
    def imei(self) -> str: ...

    @property
    def brand(self) -> str: ...

    @property
    def bootloader(self) -> str: ...

    @property
    def base_band(self) -> str: ...

    @property
    def version(self) -> OSVersion: ...

    @property
    def sim_info(self) -> str: ...

    @property
    def os_type(self) -> str: ...

    @property
    def mac_address(self) -> str: ...

    @property
    def ip_address(self) -> List[int]: ...

    @property
    def wifi_bssid(self) -> str: ...

    @property
    def wifi_ssid(self) -> str: ...

    @property
    def imsi_md5(self) -> bytes: ...

    @property
    def android_id(self) -> bytes: ...

    @property
    def apn(self) -> bytes: ...

    @property
    def vendor_name(self) -> bytes: ...

    @property
    def vendor_os_name(self) -> bytes: ...


class Engine:
    def __init__(self, device: Device, protocol: int): ...

    @property
    def uin(self) -> int: ...

    @uin.setter
    def uin(self, value: int): ...

    def encode_packet(self, pkt: Packet) -> bytes: ...

    def decode_packet(self, payload: bytes) -> Packet: ...

    def build_qrcode_fetch_request_packet(self) -> Packet: ...

    def build_qrcode_result_query_request_packet(self, sig: bytes) -> Packet: ...

    def decode_trans_emp_response(self, payload: bytes) -> QRCodeState: ...

    def build_qrcode_login_packet(self, t106: bytes, t16a: bytes, t318: bytes) -> Packet: ...

    def build_device_lock_login_packet(self) -> Packet: ...

    def build_login_packet(self, password_md5: bytes) -> Packet: ...

    def build_sms_request_packet(self) -> Packet: ...

    def build_sms_code_submit_packet(self, code: str) -> Packet: ...

    def build_ticket_submit_packet(self, ticket: str) -> Packet: ...

    def decode_login_response(self, payload: bytes) -> LoginResponse: ...

    def build_client_register_packet(self) -> Packet: ...

    def build_heartbeat_packet(self) -> Packet: ...

    def build_update_signature_packet(self, signature: str) -> Packet: ...

    def uni_packet(self, command_name: str, body: bytes) -> Packet: ...


class QRCodeState:
    @property
    def image_fetch(self) -> Optional[QRCodeImageFetch]: ...

    @property
    def confirmed(self) -> Optional[QRCodeConfirmed]: ...

    @property
    def waiting_for_scan(self) -> Optional[bool]: ...

    @property
    def waiting_for_confirm(self) -> Optional[bool]: ...

    @property
    def timeout(self) -> Optional[bool]: ...

    @property
    def canceled(self) -> Optional[bool]: ...


class QRCodeImageFetch:
    @property
    def sig(self) -> bytes: ...

    @property
    def image(self) -> bytes: ...


class QRCodeConfirmed:
    @property
    def uin(self) -> int: ...

    @property
    def tmp_pwd(self) -> bytes: ...

    @property
    def tmp_no_pic_sig(self) -> bytes: ...

    @property
    def tgt_qr(self) -> bytes: ...


class LoginResponse:
    @property
    def success(self) -> Optional[LoginSuccess]: ...

    @property
    def device_lock_login(self) -> Optional[bool]: ...

    @property
    def account_frozen(self) -> Optional[bool]: ...

    @property
    def too_many_sms_request(self) -> Optional[bool]: ...

    @property
    def device_locked(self) -> Optional[LoginDeviceLocked]: ...

    @property
    def need_captcha(self) -> Optional[LoginNeedCaptcha]: ...


class LoginSuccess:
    @property
    def account_info(self) -> Optional[AccountInfo]: ...


class LoginDeviceLocked:
    @property
    def sms_phone(self) -> Optional[str]: ...

    @property
    def verify_url(self) -> Optional[str]: ...

    @property
    def message(self) -> Optional[str]: ...


class LoginNeedCaptcha:
    @property
    def verify_url(self) -> Optional[str]: ...


class AccountInfo:
    @property
    def nick(self) -> str: ...

    @property
    def age(self) -> int: ...

    @property
    def gender(self) -> int: ...
