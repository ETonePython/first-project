from faker import Faker
import mobile
import pytest

fake = Faker()

skytel_prefix = ["91", "96", "90"]
unitel_prefix = ["88", "86", "89", "80"]


def test_unitel_88():
    assert mobile.is_unitel("88112233")

@pytest.mark.parametrize("phone_number", [
    "88112233",
    "86112233",
])
def test_unitel(phone_number):
    assert mobile.is_unitel(phone_number)

@pytest.mark.parametrize("prefix", unitel_prefix)
def test_unitel_prefix(prefix):
    assert mobile.is_unitel(fake.numerify(text=f"{prefix}######"))

@pytest.mark.parametrize("prefix", skytel_prefix + unitel_prefix)
def test_mobicom_prefix_invalid(prefix):
    assert not mobile.is_mobicom(fake.numerify(text=f"{prefix}######"))
