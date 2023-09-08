from abc223.D.main import solve

import pytest

@pytest.mark.parametrize("N,M,A,B, expected", [
    (4,1,[1],[2], [1,2,3,4]),
    (4,2,[1,3],[2,4], [1,2,3,4]),
    (4,3,[1,1,3],[2,3,2], [1,3,2,4]),

])
def test_solve(capsys,N,M,A,B, expected):
    solve(N,M,A,B)
    out, _ = capsys.readouterr()
    assert list(map(int, out.split()))==expected

