


class SIPMessage:

    def __init__(self, header, body):
        self.header = header
        self.body = body

def parse_raw_sip_message(message: str) -> SIPMessage:
    message = message.splitlines()
    start_line = message[0]
    headers = []
    for lines in message[1:]:
        if ":" in lines:
            headers.append(lines)
    body = []
    print(start_line)
    print(headers)
    return None
    # return SIPMessage(header, body)


SIP_MESSAGE = """INVITE sip:bob@biloxi.com SIP/2.0
Via: SIP/2.0/UDP ://atlanta.com;branch=z9hG4bK776asdhds
Max-Forwards: 70
To: Bob <sip:bob@biloxi.com>
From: Alice <sip:alice@atlanta.com>;tag=1928301774
Call-ID: a84b4c76e66710@://atlanta.com
CSeq: 314159 INVITE
Contact: <sip:alice@://atlanta.com>
Content-Type: application/sdp
Content-Length: 142"""
parse_raw_sip_message(SIP_MESSAGE)

