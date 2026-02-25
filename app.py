def tinh_giam_gia(gia_goc, phan_tram):
    if phan_tram > 100: return 0
    return gia_goc * (1 - phan_tram/100)

# Chạy thử
print(f"Giá sau giảm 20% của 100k là: {tinh_giam_gia(100, 20)}k")