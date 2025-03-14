from pytest import approx
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe

def test_water_column_height():
    """Verify that the water_column_height
    function returns correct results.

    Parameters: none
    Return: nothing
    """
    assert water_column_height(0, 0) == 0
    assert water_column_height(0, 10) == 7.5
    assert water_column_height(25, 0) == 25
    assert water_column_height(48.3, 12.8) == 57.9

def test_pressure_gain_from_water_height():
    """Verify that the pressure_gain_from_water_height
    function returns correct results.

    Parameters: none
    Return: nothing
    """
    assert pressure_gain_from_water_height(0) == approx(0, 0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, 0.001)
    assert pressure_gain_from_water_height(50) == approx(489.450, 0.001)

def test_pressure_loss_from_pipe():
    """Verify that the pressure_loss_from_pipe
    function returns correct results.

    Parameters: none
    Return: nothing
    """
    assert pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == approx(0, 0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0, 1.75) == approx(0, 0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == approx(0, 0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == approx(-113.008, 0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == approx(-100.462, 0.001)
    assert pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == approx(-61.576, 0.001)
    assert pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == approx(-110.884, 0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])




