"""upload_assets.put() sends the decision-36 Cache-Control for Words/Thumbnails (no network).
Run: python3 test_upload_cache_control.py"""
import os, sys, tempfile, unittest
from unittest import mock
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import upload_assets as U


class Resp:
    status = 200
    def __enter__(self): return self
    def __exit__(self, *a): return False


class PutCacheControl(unittest.TestCase):
    def sent(self, bucket, name):
        with tempfile.NamedTemporaryFile(suffix=os.path.splitext(name)[1], delete=False) as f:
            f.write(b'x')
        seen = []
        with mock.patch.object(U.urllib.request, 'urlopen', lambda req, timeout=0: (seen.append(req), Resp())[1]):
            self.assertEqual(U.put('https://example.invalid', 'k', bucket, name, f.name, True), 'ok')
        os.unlink(f.name)
        return {k.lower(): v for k, v in seen[0].header_items()}

    def test_words(self):
        h = self.sent('Words', 'cat_1.mp4')
        self.assertEqual(h['cache-control'], 'public, max-age=31536000, immutable')
        self.assertEqual(h['content-type'], 'video/mp4')

    def test_thumbnails(self):
        self.assertEqual(self.sent('Thumbnails', 'cat_1.webp')['cache-control'], 'public, max-age=31536000, immutable')

    def test_other_bucket_untouched(self):
        self.assertNotIn('cache-control', self.sent('avatars', 'a.png'))


if __name__ == '__main__':
    unittest.main()
