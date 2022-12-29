import pytest
from neural_networks_for_csp.__main__ import parse_args_and_run


def test_help_message(capsys):
    with pytest.raises(SystemExit) as system_exit:
        parse_args_and_run(["neural_networks_for_csp", "-h"])
        assert system_exit.code == 0
    assert "neural_networks_for_csp" in capsys.readouterr().out
