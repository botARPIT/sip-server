


class SIPMessage:

    def __init__(self, header, body):
        self.header = header
        self.body = body
        
def parseRawSIPMessage(message: RawSIPMessage) -> SIPMessage:
    split_message = message.split( )
    header = split_message[0]
    body = split_message[1]

    return SIPMessage(header, body)