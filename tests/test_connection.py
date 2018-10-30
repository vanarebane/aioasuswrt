#    @mock.patch(
#        'homeassistant.components.device_tracker.asuswrt.AsusWrtDeviceScanner',
#        return_value=mock.MagicMock())
#    def test_get_scanner_with_pubkey_no_password(self, asuswrt_mock):
#        """Test creating an AsusWRT scanner with a pubkey and no password."""
#        conf_dict = {
#            device_tracker.DOMAIN: {
#                CONF_PLATFORM: 'asuswrt',
#                CONF_HOST: 'fake_host',
#                CONF_USERNAME: 'fake_user',
#                CONF_PUB_KEY: FAKEFILE,
#                CONF_TRACK_NEW: True,
#                CONF_CONSIDER_HOME: timedelta(seconds=180),
#                CONF_NEW_DEVICE_DEFAULTS: {
#                    CONF_TRACK_NEW: True,
#                    CONF_AWAY_HIDE: False
#                }
#            }
#        }
#
#        with assert_setup_component(1, DOMAIN):
#            assert setup_component(self.hass, DOMAIN, conf_dict)
#
#        conf_dict[DOMAIN][CONF_MODE] = 'router'
#        conf_dict[DOMAIN][CONF_PROTOCOL] = 'ssh'
#        conf_dict[DOMAIN][CONF_PORT] = 22
#        self.assertEqual(asuswrt_mock.call_count, 1)
#        self.assertEqual(asuswrt_mock.call_args, mock.call(conf_dict[DOMAIN]))
#
#    def test_ssh_login_with_pub_key(self):
#        """Test that login is done with pub_key when configured to."""
#        ssh = mock.MagicMock()
#        ssh_mock = mock.patch('pexpect.pxssh.pxssh', return_value=ssh)
#        ssh_mock.start()
#        self.addCleanup(ssh_mock.stop)
#        conf_dict = PLATFORM_SCHEMA({
#            CONF_PLATFORM: 'asuswrt',
#            CONF_HOST: 'fake_host',
#            CONF_USERNAME: 'fake_user',
#            CONF_PUB_KEY: FAKEFILE
#        })
#        update_mock = mock.patch(
#            'homeassistant.components.device_tracker.asuswrt.'
#            'AsusWrtDeviceScanner.get_asuswrt_data')
#        update_mock.start()
#        self.addCleanup(update_mock.stop)
#        asuswrt = device_tracker.asuswrt.AsusWrtDeviceScanner(conf_dict)
#        asuswrt.connection.run_command('ls')
#        self.assertEqual(ssh.login.call_count, 1)
#        self.assertEqual(
#            ssh.login.call_args,
#            mock.call('fake_host', 'fake_user', quiet=False,
#                      ssh_key=FAKEFILE, port=22)
#        )
#
#    def test_ssh_login_with_password(self):
#        """Test that login is done with password when configured to."""
#        ssh = mock.MagicMock()
#        ssh_mock = mock.patch('pexpect.pxssh.pxssh', return_value=ssh)
#        ssh_mock.start()
#        self.addCleanup(ssh_mock.stop)
#        conf_dict = PLATFORM_SCHEMA({
#            CONF_PLATFORM: 'asuswrt',
#            CONF_HOST: 'fake_host',
#            CONF_USERNAME: 'fake_user',
#            CONF_PASSWORD: 'fake_pass'
#        })
#        update_mock = mock.patch(
#            'homeassistant.components.device_tracker.asuswrt.'
#            'AsusWrtDeviceScanner.get_asuswrt_data')
#        update_mock.start()
#        self.addCleanup(update_mock.stop)
#        asuswrt = device_tracker.asuswrt.AsusWrtDeviceScanner(conf_dict)
#        asuswrt.connection.run_command('ls')
#        self.assertEqual(ssh.login.call_count, 1)
#        self.assertEqual(
#            ssh.login.call_args,
#            mock.call('fake_host', 'fake_user', quiet=False,
#                      password='fake_pass', port=22)
#        )
#
#    def test_ssh_login_without_password_or_pubkey(self):
#        """Test that login is not called without password or pub_key."""
#        ssh = mock.MagicMock()
#        ssh_mock = mock.patch('pexpect.pxssh.pxssh', return_value=ssh)
#        ssh_mock.start()
#        self.addCleanup(ssh_mock.stop)
#
#        conf_dict = {
#            CONF_PLATFORM: 'asuswrt',
#            CONF_HOST: 'fake_host',
#            CONF_USERNAME: 'fake_user',
#        }
#
#        with self.assertRaises(vol.Invalid):
#            conf_dict = PLATFORM_SCHEMA(conf_dict)
#
#        update_mock = mock.patch(
#            'homeassistant.components.device_tracker.asuswrt.'
#            'AsusWrtDeviceScanner.get_asuswrt_data')
#        update_mock.start()
#        self.addCleanup(update_mock.stop)
#
#        with assert_setup_component(0, DOMAIN):
#            assert setup_component(self.hass, DOMAIN,
#                                   {DOMAIN: conf_dict})
#        ssh.login.assert_not_called()

#    def test_telnet_login_with_password(self):
#        """Test that login is done with password when configured to."""
#        telnet = mock.MagicMock()
#        telnet_mock = mock.patch('telnetlib.Telnet', return_value=telnet)
#        telnet_mock.start()
#        self.addCleanup(telnet_mock.stop)
#        conf_dict = PLATFORM_SCHEMA({
#            CONF_PLATFORM: 'asuswrt',
#            CONF_PROTOCOL: 'telnet',
#            CONF_HOST: 'fake_host',
#            CONF_USERNAME: 'fake_user',
#            CONF_PASSWORD: 'fake_pass'
#        })
#        update_mock = mock.patch(
#            'homeassistant.components.device_tracker.asuswrt.'
#            'AsusWrtDeviceScanner.get_asuswrt_data')
#        update_mock.start()
#        self.addCleanup(update_mock.stop)
#        asuswrt = device_tracker.asuswrt.AsusWrtDeviceScanner(conf_dict)
#        asuswrt.connection.run_command('ls')
#        self.assertEqual(telnet.read_until.call_count, 4)
#        self.assertEqual(telnet.write.call_count, 3)
#        self.assertEqual(
#            telnet.read_until.call_args_list[0],
#            mock.call(b'login: ')
#        )
#        self.assertEqual(
#            telnet.write.call_args_list[0],
#            mock.call(b'fake_user\n')
#        )
#        self.assertEqual(
#            telnet.read_until.call_args_list[1],
#            mock.call(b'Password: ')
#        )
#        self.assertEqual(
#            telnet.write.call_args_list[1],
#            mock.call(b'fake_pass\n')
#        )
#        self.assertEqual(
#            telnet.read_until.call_args_list[2],
#            mock.call(b'#')
#        )
#
#    def test_telnet_login_without_password(self):
#        """Test that login is not called without password or pub_key."""
#        telnet = mock.MagicMock()
#        telnet_mock = mock.patch('telnetlib.Telnet', return_value=telnet)
#        telnet_mock.start()
#        self.addCleanup(telnet_mock.stop)
#
#        conf_dict = {
#            CONF_PLATFORM: 'asuswrt',
#            CONF_PROTOCOL: 'telnet',
#            CONF_HOST: 'fake_host',
#            CONF_USERNAME: 'fake_user',
#        }
#
#        with self.assertRaises(vol.Invalid):
#            conf_dict = PLATFORM_SCHEMA(conf_dict)
#
#        update_mock = mock.patch(
#            'homeassistant.components.device_tracker.asuswrt.'
#            'AsusWrtDeviceScanner.get_asuswrt_data')
#        update_mock.start()
#        self.addCleanup(update_mock.stop)
#
#        with assert_setup_component(0, DOMAIN):
#            assert setup_component(self.hass, DOMAIN,
#                                   {DOMAIN: conf_dict})
#        telnet.login.assert_not_called()
#
#
# @pytest.mark.skip(
#    reason="These tests are performing actual failing network calls. They "
#    "need to be cleaned up before they are re-enabled. They're frequently "
#    "failing in Travis.")
# class TestSshConnection(TestCase):
#    """Testing SshConnection."""
#
#    def setUp(self):
#        """Set up test env."""
#        self.connection = SshConnection(
#            'fake', 'fake', 'fake', 'fake', 'fake')
#        self.connection._connected = True
#
#    def test_run_command_exception_eof(self):
#        """Testing exception in run_command."""
#        from pexpect import exceptions
#        self.connection._ssh = mock.Mock()
#        self.connection._ssh.sendline = mock.Mock()
#        self.connection._ssh.sendline.side_effect = exceptions.EOF('except')
#        self.connection.run_command('test')
#        self.assertFalse(self.connection._connected)
#        self.assertIsNone(self.connection._ssh)
#
#    def test_run_command_exception_pxssh(self):
#        """Testing exception in run_command."""
#        from pexpect import pxssh
#        self.connection._ssh = mock.Mock()
#        self.connection._ssh.sendline = mock.Mock()
#        self.connection._ssh.sendline.side_effect = pxssh.ExceptionPxssh(
#            'except')
#        self.connection.run_command('test')
#        self.assertFalse(self.connection._connected)
#        self.assertIsNone(self.connection._ssh)
#
#    def test_run_command_assertion_error(self):
#        """Testing exception in run_command."""
#        self.connection._ssh = mock.Mock()
#        self.connection._ssh.sendline = mock.Mock()
#        self.connection._ssh.sendline.side_effect = AssertionError('except')
#        self.connection.run_command('test')
#        self.assertFalse(self.connection._connected)
#        self.assertIsNone(self.connection._ssh)
#
#
# @pytest.mark.skip(
#    reason="These tests are performing actual failing network calls. They "
#    "need to be cleaned up before they are re-enabled. They're frequently "
#    "failing in Travis.")
# class TestTelnetConnection(TestCase):
#    """Testing TelnetConnection."""
#
#    def setUp(self):
#        """Set up test env."""
#        self.connection = TelnetConnection(
#            'fake', 'fake', 'fake', 'fake')
#        self.connection._connected = True
#
#    def test_run_command_exception_eof(self):
#        """Testing EOFException in run_command."""
#        self.connection._telnet = mock.Mock()
#        self.connection._telnet.write = mock.Mock()
#        self.connection._telnet.write.side_effect = EOFError('except')
#        self.connection.run_command('test')
#        self.assertFalse(self.connection._connected)
#
#    def test_run_command_exception_connection_refused(self):
#        """Testing ConnectionRefusedError in run_command."""
#        self.connection._telnet = mock.Mock()
#        self.connection._telnet.write = mock.Mock()
#        self.connection._telnet.write.side_effect = ConnectionRefusedError(
#            'except')
#        self.connection.run_command('test')
#        self.assertFalse(self.connection._connected)
#
#    def test_run_command_exception_gaierror(self):
#        """Testing socket.gaierror in run_command."""
#        self.connection._telnet = mock.Mock()
#        self.connection._telnet.write = mock.Mock()
#        self.connection._telnet.write.side_effect = socket.gaierror('except')
#        self.connection.run_command('test')
#        self.assertFalse(self.connection._connected)
#
#    def test_run_command_exception_oserror(self):
#        """Testing OSError in run_command."""
#        self.connection._telnet = mock.Mock()
#        self.connection._telnet.write = mock.Mock()
#        self.connection._telnet.write.side_effect = OSError('except')
#        self.connection.run_command('test')
#        self.assertFalse(self.connection._connected)