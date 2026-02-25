from app import tinh_giam_gia
def test_logic_giam_gia():
    # Kiểm tra xem 100k giảm 20% có đúng là 80k không
    assert tinh_giam_gia(100, 20) == 80

def test_giam_gia_qua_da():
    # Nếu giảm > 100% thì giá phải bằng 0
    assert tinh_giam_gia(100, 110) == 0