from litespi.spi_nor_flash_module import SpiNorFlashModule
from litespi.opcodes import SpiNorFlashOpCodes
from litespi.ids import SpiNorFlashManufacturerIDs

# Define non-generated SPI NOR chips here

class MX25L12833F(SpiNorFlashModule):
    """MX25L12833F

    Datasheet: https://www.macronix.com/Lists/Datasheet/Attachments/7447/MX25L12833F,%203V,%20128Mb,%20v1.0.pdf
    """

    manufacturer_id = SpiNorFlashManufacturerIDs.MACRONIX
    device_id = 0x2018
    name = "mx25l12833f"

    total_size  =   16777216   # bytes
    page_size   =        256   # bytes
    total_pages =      65536

    supported_opcodes = [
        SpiNorFlashOpCodes.READ_1_1_1,
        SpiNorFlashOpCodes.READ_1_1_1_FAST,
        SpiNorFlashOpCodes.READ_1_1_2,
        SpiNorFlashOpCodes.READ_1_2_2,
        SpiNorFlashOpCodes.READ_1_1_4,
        SpiNorFlashOpCodes.READ_1_4_4,
        SpiNorFlashOpCodes.READ_4_4_4,
        SpiNorFlashOpCodes.PP_1_1_1,
        SpiNorFlashOpCodes.PP_1_4_4,
    ]
    dummy_bits = 8


class MX25L6406E(SpiNorFlashModule):
    """MX25L6406E

    Datasheet: https://www.macronix.com/Lists/Datasheet/Attachments/7370/MX25L6406E,%203V,%2064Mb,%20v1.9.pdf
    """

    manufacturer_id = SpiNorFlashManufacturerIDs.MACRONIX
    device_id = 0x2017
    name = "mx25l6406e"

    total_size  =    8388608   # bytes
    page_size   =        256   # bytes
    total_pages =      32768

    supported_opcodes = [
        SpiNorFlashOpCodes.READ_1_1_1,
        SpiNorFlashOpCodes.READ_1_1_1_FAST,
        SpiNorFlashOpCodes.READ_1_1_2,
        SpiNorFlashOpCodes.PP_1_1_1,
    ]
    dummy_bits = 8


class W25Q512JV(SpiNorFlashModule):
    """W25Q512JV

    Datasheet: https://www.winbond.com/resource-files/W25Q512JV%20SPI%20RevB%2006252019%20KMS.pdf
    """

    manufacturer_id = SpiNorFlashManufacturerIDs.WINBOND
    device_id = 0x4021
    name = "w25q512jv"

    total_size  =   67108864   # bytes
    page_size   =        256   # bytes
    total_pages =     262144

    supported_opcodes = [
        SpiNorFlashOpCodes.READ_1_1_1,
        SpiNorFlashOpCodes.READ_1_1_1_4B,
        SpiNorFlashOpCodes.READ_1_1_1_FAST,
        SpiNorFlashOpCodes.READ_1_1_1_FAST_4B,
        SpiNorFlashOpCodes.READ_1_1_2,
        SpiNorFlashOpCodes.READ_1_1_2_4B,
        SpiNorFlashOpCodes.READ_1_2_2,
        SpiNorFlashOpCodes.READ_1_2_2_4B,
        SpiNorFlashOpCodes.READ_1_1_4,
        SpiNorFlashOpCodes.READ_1_1_4_4B,
        SpiNorFlashOpCodes.READ_1_4_4,
        SpiNorFlashOpCodes.READ_1_4_4_4B,
        SpiNorFlashOpCodes.PP_1_1_1,
        SpiNorFlashOpCodes.PP_1_1_1_4B,
        SpiNorFlashOpCodes.PP_1_1_4,
        SpiNorFlashOpCodes.PP_1_1_4_4B,
    ]
    dummy_bits = 8

class W25Q16JV(SpiNorFlashModule):
    """W25Q16JV

    Datasheet: https://www.winbond.com/resource-files/w25q16jv%20spi%20revh%2004082019%20plus.pdf
    """

    manufacturer_id = SpiNorFlashManufacturerIDs.WINBOND
    device_id = 0x4015
    name = "w25q16jv"

    total_size  =   2097152   # bytes
    page_size   =       256   # bytes
    total_pages =      8192

    supported_opcodes = [
        SpiNorFlashOpCodes.READ_1_1_1,
        SpiNorFlashOpCodes.READ_1_1_1_4B,
        SpiNorFlashOpCodes.READ_1_1_1_FAST,
        SpiNorFlashOpCodes.READ_1_1_1_FAST_4B,
        SpiNorFlashOpCodes.READ_1_1_2,
        SpiNorFlashOpCodes.READ_1_1_2_4B,
        SpiNorFlashOpCodes.READ_1_2_2,
        SpiNorFlashOpCodes.READ_1_2_2_4B,
        SpiNorFlashOpCodes.READ_1_1_4,
        SpiNorFlashOpCodes.READ_1_1_4_4B,
        SpiNorFlashOpCodes.READ_1_4_4,
        SpiNorFlashOpCodes.READ_1_4_4_4B,
        SpiNorFlashOpCodes.PP_1_1_1,
        SpiNorFlashOpCodes.PP_1_1_1_4B,
        SpiNorFlashOpCodes.PP_1_1_4,
        SpiNorFlashOpCodes.PP_1_1_4_4B,
    ]
    dummy_bits = 8



class W74M64FV(SpiNorFlashModule):
    """W74M64FV

    Datasheet: https://www.winbond.com/resource-files/w74m64fv%20revb.pdf
    """

    manufacturer_id = SpiNorFlashManufacturerIDs.WINBOND
    device_id = 0x0000 # FIXME
    name = "w74m64fv"

    total_size  =    8388608   # bytes
    page_size   =        256   # bytes
    total_pages =      32768

    supported_opcodes = [
        SpiNorFlashOpCodes.READ_1_1_1,
        SpiNorFlashOpCodes.READ_1_1_4,
        SpiNorFlashOpCodes.PP_1_1_1,
    ]
    dummy_bits = 8
