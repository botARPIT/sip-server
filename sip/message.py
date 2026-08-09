


class SIPMessage:

    def __init__(self, start_line, header, body):
        self.start_line = start_line
        self.header = header
        self.body = body

def parse_raw_sip_message(raw_message: str) -> SIPMessage:
    message = raw_message.split("\n")
    start_line = ""
    headers = {}
    body = ""
    for index, line in enumerate(message):
        if index == 0:
            start_line = line
            continue

        if line == '' :   
            body = str(message[index + 1:])
            break
        else :
            value = line.split(":", 1)
            headers[value[0]] = value[1].strip()
            
    
    return SIPMessage(start_line, headers, body)


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
parse_raw_sip_message(SIP_MESSAGE)

