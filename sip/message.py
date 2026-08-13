


class SIPMessage:

    def __init__(self, start_line, headers, body):
        self.start_line = start_line
        self.headers = headers
        self.body = body


    def __repr__(self):
        return (
            f"SIPMessage("
            f"start_line={self.start_line!r}"
            f"headers={self.headers!r}"
            f"body={self.body!r})"
        )

    @property
    def method(self):
        return self.start_line.split()[0]

    @property
    def request_uri(self):
        return self.start_line.split()[1]

    @property
    def version(self):
        return self.start_line.split()[2]

def parse_raw_sip_message(raw_message: str) -> SIPMessage:
    header_section, body = raw_message.split("\n\n", 1)
    start_line, headers = header_section.split("\n", 1)
    headers = headers.split("\n")
    parsed_headers = {}

    for line in headers:
        name, value = line.split(":", 1)
        parsed_headers[name] = value.strip()

    return SIPMessage(start_line, parsed_headers, body)


def serialize_sip_message(message: SIPMessage) -> str:
    lines = []
    lines.append(message.start_line)
    for name, value in message.headers.items():
        lines.append(f"{name}: {value}")
    lines.append("")
    lines.append(message.body)
    print(lines)
    return "\r\n".join(lines)

SIP_MESSAGE = """INVITE sip:bob@biloxi.com SIP/2.0
Via: SIP/2.0/UDP ://atlanta.com;branch=z9hG4bK776asdhds
Max-Forwards: 70
To: Bob <sip:bob@biloxi.com>
From: Alice <sip:alice@atlanta.com>;tag=1928301774
Call-ID: a84b4c76e66710@://atlanta.com
CSeq: 314159 INVITE
Contact: <sip:alice@://atlanta.com>
Content-Type: application/sdp
Content-Length: 142

v=0
o=alice 2890844526 2890844526 IN IP4 ://atlanta.com
s=-
c=IN IP4 ://atlanta.com
t=0 0
m=audio 49170 RTP/AVP 0
a=rtpmap:0 PCMU/8000"""
message = parse_raw_sip_message(SIP_MESSAGE)
print(serialize_sip_message(message))


