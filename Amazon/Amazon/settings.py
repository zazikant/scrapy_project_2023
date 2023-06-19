# Scrapy settings for Amazon project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import scraper_helper as sh

BOT_NAME = "Amazon"

SPIDER_MODULES = ["Amazon.spiders"]
NEWSPIDER_MODULE = "Amazon.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "Amazon (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
AUTOTHROTTLE_SPEED = True

DEFAULT_REQUEST_HEADERS = sh.get_dict(
'''
Accept:
*/*
Accept-Encoding:
gzip, deflate, br
Accept-Language:
en-IN,en;q=0.9,mr-IN;q=0.8,mr;q=0.7,en-GB;q=0.6,en-US;q=0.5
Cookie:
DESIGNINGBUILDINGS=qal8qrfh0uiilv3pqoe7b2b6v4; __cf_bm=Cp1mK2J2_MO4xki23obTIZAtrzoJe02yLDtyhXYDflU-1687014155-0-AX4XIUnu9xTfariVUN8LysYXaL1CqayvQGMmbpW4ojFoaipk9zyVGP+n4oD5pdi/NA==; cc_cookie=%7B%22categories%22%3A%5B%22necessary%22%2C%22analytics%22%2C%22targeting%22%5D%2C%22level%22%3A%5B%22necessary%22%2C%22analytics%22%2C%22targeting%22%5D%2C%22revision%22%3A1%2C%22data%22%3Anull%2C%22rfc_cookie%22%3Atrue%2C%22consent_date%22%3A%222023-06-17T15%3A02%3A36.705Z%22%2C%22consent_uuid%22%3A%226862a419-6289-44a4-9e8a-7a92ddcffe6d%22%2C%22last_consent_update%22%3A%222023-06-17T15%3A02%3A36.705Z%22%7D; __gads=ID=9cc24426c38ab976-2236ec1e0a8000d1:T=1687014157:RT=1687014157:S=ALNI_MaMUPDo7G7j3uLI51JlNGzJM3mesA; __gpi=UID=00000c50c27a65db:T=1687014157:RT=1687014157:S=ALNI_MZXsFBes5xxVO45OvbeuzMxfEqQoA; _gid=GA1.3.1570572681.1687014160; _gat=1; _ga=GA1.1.1860930292.1687014160; _ga_GWDVC2DBNV=GS1.1.1687014161.1.1.1687014197.0.0.0
Referer:
https://www.designingbuildings.co.uk/wiki/Home
Sec-Ch-Ua:
"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"
Sec-Ch-Ua-Mobile:
?0
Sec-Ch-Ua-Platform:
"Windows"
Sec-Fetch-Dest:
empty
Sec-Fetch-Mode:
cors
Sec-Fetch-Site:
same-origin
User-Agent:
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
'''
)



# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "Amazon.middlewares.AmazonSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "Amazon.middlewares.AmazonDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "Amazon.pipelines.AmazonPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
