import pyshorteners


class Codec:
    """
    Codec class for encoding and decoding URLs using TinyURL service.

    The Codec class provides methods to encode a long URL into a shortened TinyURL
    format, and to decode a shortened TinyURL back to its original URL.

    Usage:
        codec = Codec()
        short_url = codec.encode(long_url)
        original_url = codec.decode(short_url)

    Methods:
        encode(longUrl: str) -> str:
            Encodes a given long URL into a shortened TinyURL.

        decode(shortUrl: str) -> str:
            Decodes the given TinyURL back to its original long URL.

    LeetCode: Beats 97.24% of submissions
    """

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        s = pyshorteners.Shortener()
        return s.tinyurl.short(longUrl)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        s = pyshorteners.Shortener()
        return s.tinyurl.expand(shortUrl)
