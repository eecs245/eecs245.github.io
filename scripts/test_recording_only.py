import unittest
from unittest.mock import Mock, MagicMock, patch

import update_recording as recording


class RecordingOnlyTests(unittest.TestCase):
    def test_default_and_explicit_recording_modes_ignore_caption_failures(self):
        for flags in ([], ['--recording-only']):
            with self.subTest(flags=flags):
                browser, context = Mock(), Mock()
                target = dict(module_path='/schedule', date_str='2026-10-13',
                              date_obj=None, recording_url='https://example.com/recording',
                              lecture_number='12', lecture_name='LEC 12',
                              lecture_title='Rank', recording_title='Lecture 12')
                with patch('sys.argv', ['update_recording.py', '--interactive-login', *flags]), \
                        patch('playwright.sync_api.sync_playwright', return_value=MagicMock()), \
                        patch.object(recording, '_launch_browser', return_value=browser), \
                        patch.object(recording, '_create_context', return_value=context), \
                        patch.object(recording, '_fetch_leccap_recordings_with_context', return_value=[{}]), \
                        patch.object(recording, 'build_recording_target', return_value=target), \
                        patch.object(recording, 'select_recent_recordings', return_value=[{}]), \
                        patch.object(recording, 'update_recording'), \
                        patch.object(recording, 'update_recording_title'), \
                        patch.object(recording, 'run_git_commands') as publish, \
                        patch('recording_captions.refresh_captions', side_effect=RuntimeError('caption server failed')) as captions:
                    recording.main()
                captions.assert_not_called()
                publish.assert_called_once_with('/schedule', 'LEC 12', 'https://example.com/recording')
                browser.close.assert_called_once()


if __name__ == '__main__':
    unittest.main()
