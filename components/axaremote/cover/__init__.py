import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.components import cover
from esphome.const import CONF_ID, CONF_CLOSE_DURATION

CODEOWNERS = ["@rrooggiieerr"]
DEPENDENCIES = ['cover', 'uart']

axaremote_ns = cg.esphome_ns.namespace('axaremote')
AXARemoteCover = axaremote_ns.class_('AXARemoteCover', cg.Component, cover.Cover, uart.UARTDevice)

CONF_AUTO_CALIBRATE = "auto_calibrate"
CONF_SERIAL_STATUS = "serial_status_leading"



CONFIG_SCHEMA = cover.cover_schema(AXARemoteCover).extend(
    {
        cv.GenerateID(): cv.declare_id(AXARemoteCover),
        cv.Optional(CONF_CLOSE_DURATION, default="50s"): cv.positive_time_period_milliseconds,
        cv.Optional(CONF_AUTO_CALIBRATE, default=False): bool,
        cv.Optional(CONF_SERIAL_STATUS, default=True): bool,
    }
).extend(uart.UART_DEVICE_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await cover.register_cover(var, config)
    await uart.register_uart_device(var, config)

    cg.add(var.set_close_duration(config[CONF_CLOSE_DURATION]))
    cg.add(var.set_auto_calibrate(config[CONF_AUTO_CALIBRATE]))
    cg.add(var.set_serial_status_leading(config[CONF_SERIAL_STATUS]))
