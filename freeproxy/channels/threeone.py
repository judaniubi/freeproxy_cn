from freeproxy.channels import Channel
from freeproxy.util.pipe import to_doc, extra_xpath, safe_extra


class ThreeOneF(Channel):
    start_urls = [
        'https://31f.cn/https-proxy/'
    ]

    def next_page(self, url):
        yield url

    async def parse_page(self, session, url):
        proxys = await self.get(session, url) >> to_doc >> extra_xpath("//table[position()=1]//tr[position()>1]")
        rst = []
        for proxy in proxys:
            host = proxy >> extra_xpath(
                './td[position()=2]/text()') >> safe_extra
            port = proxy >> extra_xpath(
                './td[position()=3]/text()') >> safe_extra
            rst.append((host, port))
        return rst
