import unittest
from website_database import WebsiteDB
from server_module import parse_browser, parse_platform


class TestAPI(unittest.TestCase):
    def test_result(self):
        from main import get_result
        self.assertTrue(get_result() is None)

    def test_commands_are_valid(self):
        from main import COMMANDS
        for key, value in COMMANDS.items():
            self.assertTrue(len(key) == 1)
            self.assertTrue(value < 10)

    def test_format_data(self):
        from main import format_data
        self.assertEqual(
            'Visits count: 0\nTotal users: 0\n', format_data([]))
        data = format_data([['id0', '-', '+', '=', 'x']])
        self.assertEqual(
            'Visits count: 1\nTotal users: 1\nid0\t-\t+\t=\tx\n', data)

    def test_get_statistics(self):
        from main import get_statistics
        self.assertTrue(get_statistics(0).__contains__('\n'))
        self.assertRaises(IndexError, get_statistics, 5)

    def test_get_info(self):
        from main import get_info
        self.assertRaises(AttributeError, get_info, '-xxx')
        self.assertRaises(AttributeError, get_info, 't')

    def test_get_new_date(self):
        from main import get_new_date
        date = [1, 1, 1]
        self.assertEqual(0, get_new_date(date, 1, 1, 1,))


class TestServer(unittest.TestCase):
    def test_filling_db(self):
        from server import fill_db_values
        self.assertRaises(AttributeError, fill_db_values, 0, None)

    def test_setup_referrer(self):
        from server import setup_referrer
        self.assertRaises(AttributeError, setup_referrer, None)

    def test_setup_response(self):
        from server import setup_response
        self.assertRaises(RuntimeError, setup_response, "1")

    def test_client_id(self):
        from server import get_user_id
        self.assertEqual(get_user_id('5'), '5')
        self.assertTrue(int(get_user_id('0')) > 0)

    def test_server(self):
        from server import app
        self.assertTrue(app is not None)

    def test_browser_parser(self):
        firefox = 'Mozilla/5.0 Gecko/20100101 Firefox/47.0'
        edge = 'Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
        safari = 'Version/13.1.1 Mobile/15E148 Safari/604.1'
        self.assertEqual(parse_browser(firefox), 'Firefox')
        self.assertEqual(parse_browser(edge), 'Edge')
        self.assertEqual(parse_browser(safari), 'Safari')

    def test_platform(self):
        linux = '(X11; Linux x86_64)'
        mac = '(Macintosh; Intel Mac OS X; U; en)'
        win = '(Windows NT 10.0; Win64; x64)'
        ios = '(iPhone; CPU iPhone OS 13_5_1 like Mac OS X)'
        self.assertEqual(parse_platform(linux), 'Linux')
        self.assertEqual(parse_platform(mac), 'Macintosh')
        self.assertEqual(parse_platform(win), 'Windows')
        self.assertEqual(parse_platform(ios), 'iOS')


class TestDB(unittest.TestCase):
    def test_db_init(self):
        self.assertTrue(WebsiteDB())

    def test_db_close(self):
        self.assertTrue(WebsiteDB().close())

    def test_can_get_values(self):
        self.assertTrue(len(WebsiteDB()
                            .get_values()) >= 0)

    def test_set_values(self):
        self.assertRaises(TypeError, WebsiteDB().set_value, None, None, None)


if __name__ == '__main__':
    unittest.main()
