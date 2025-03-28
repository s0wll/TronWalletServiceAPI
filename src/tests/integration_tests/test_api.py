import pytest


@pytest.mark.parametrize(
    "address",
    [
        ("TGJBjL8wmRVyRStkghnhcVNYYgn6Yjno6X"),
        ("TSMC4YzUSfySfqKuFnJbYyU3W6PBebBk2E"),
    ],
)
async def test_create_wallet_info(address: str, ac):
    response = await ac.post("/wallet_info", json={"address": address})
    assert response.status_code == 200
    assert "data" in response.json()


async def test_get_wallet_info_list(ac):
    response = await ac.get("/wallet_info")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
