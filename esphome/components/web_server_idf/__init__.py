from esphome.components.esp32 import add_idf_sdkconfig_option
import esphome.config_validation as cv

CODEOWNERS = ["@dentra"]

CONFIG_SCHEMA = cv.All(
    cv.Schema({}),
    cv.only_with_esp_idf,
)


async def to_code(config):
    # HTTP server memory optimizations for ESP-IDF
    # Maximum supported size of headers section in HTTP request packet
    add_idf_sdkconfig_option("CONFIG_HTTPD_MAX_REQ_HDR_LEN", 512)  # Reduced from 1024

    # Maximum supported size of URI in HTTP request
    add_idf_sdkconfig_option("CONFIG_HTTPD_MAX_URI_LEN", 256)  # Default is 512

    # Size of buffer to allocate for purge function
    add_idf_sdkconfig_option("CONFIG_HTTPD_PURGE_BUF_LEN", 16)  # Default is 32

    # Disable WebSocket support if not needed
    add_idf_sdkconfig_option("CONFIG_HTTPD_WS_SUPPORT", False)
