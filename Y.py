import zlib,base64
exec(zlib.decompress(base64.b64decode("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")))