
import time

print("=" * 55)
print("             DONG HO HOC TAP POMODORO")
print("=" * 55)

# Nhap thong tin
mon_hoc = input("Hom nay ban muon hoc gi? ")

thoi_gian_hoc = int(input("Thoi gian hoc (phut): "))
thoi_gian_nghi = int(input("Thoi gian nghi (phut): "))

so_lan = 0

# Bat dau chuong trinh
while True:
    print("\n" + "=" * 55)
    print(f"BAT DAU PHIEN HOC SO {so_lan + 1}")
    print(f"Mon hoc: {mon_hoc}")
    input("Nhan Enter de bat dau...")

    tong_giay = thoi_gian_hoc * 60

    for i in range(tong_giay, 0, -1):
        phut = i // 60
        giay = i % 60

        tien_do = int((tong_giay - i) / tong_giay * 20)
        thanh = "#" * tien_do + "-" * (20 - tien_do)
        phan_tram = int((tong_giay - i) / tong_giay * 100)

        print(
            f"\rHoc: {phut:02d}:{giay:02d} "
            f"[{thanh}] {phan_tram}%",
            end=""
        )

        time.sleep(1)

    so_lan += 1

    print("\n\nHET GIO HOC!")
    print(f"Ban da hoan thanh {so_lan} lan Pomodoro!")
    print("Rat tot! Hay tiep tuc phat huy!")

    print(f"\nBat dau nghi ngoi {thoi_gian_nghi} phut...")

    tong_giay = thoi_gian_nghi * 60

    for i in range(tong_giay, 0, -1):
        phut = i // 60
        giay = i % 60

        print(f"\rThoi gian nghi: {phut:02d}:{giay:02d}", end="")
        time.sleep(1)

    print("\nDa het thoi gian nghi!")

    tiep_tuc = input("\nBan co muon hoc tiep khong (c/k)? ")

    if tiep_tuc.lower() != "c":
        break

print("\n" + "=" * 55)
print("TONG SO PHIEN POMODORO:", so_lan)
print("CHUC BAN HOC TAP THAT HIEU QUA!")
print("=" * 55)
