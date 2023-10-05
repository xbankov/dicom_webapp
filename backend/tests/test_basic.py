# backend/tests/test_authentication.py

from fastapi.testclient import TestClient
from idna import valid_contextj
import numpy as np
from pydicom import dcmread
from src.volume_computation import calculate_volume

valid_dicom = dcmread("backend/tests/1-101.dcm")


def test_calculate_volume():
    assert calculate_volume(valid_dicom, threshold=0.5) == 143280.03
