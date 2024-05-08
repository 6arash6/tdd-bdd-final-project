"""
CLI Command Extensions for Flask
"""
import os
from unittest import TestCase
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from service.common.cli_commands import db_create
#from service import __init__ as service_init



class TestFlaskCLI(TestCase):
    """Test Flask CLI Commands"""

    def setUp(self):
        self.runner = CliRunner()

    @patch('service.common.cli_commands.db')
    def test_db_create(self, db_mock):
        """It should call the db-create command"""
        db_mock.return_value = MagicMock()
        with patch.dict(os.environ, {"FLASK_APP": "service:app"}, clear=True):
            result = self.runner.invoke(db_create)
            self.assertEqual(result.exit_code, 0)
#ari
#   @patch('service.models.init_db')
#   def test_exception_handling(self, mock_init_db):
#     # Simulate an exception
#     mock_init_db.side_effect = Exception("Test Exception")

#     # Call the app initialization (assuming it's called from your main app file)
#     service_init.app = Flask(__name__)
#     with self.assertRaises(SystemExit):
#       service_init.app  # You might need to adjust the function name
#       #models.init_db(app)

#     # Assert expected behavior
#     service_init.app.logger.critical.assert_called_once_with(
#         "Test Exception: Cannot continue"
#     )

#if __name__ == '__main__':
#  unittest.main()