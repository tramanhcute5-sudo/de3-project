
import time

print("=" * 55)
print("             DONG HO HOC TAP POMODORO")
print("=" * 55)

#nhapmonhoc
monhoc = input("Hom nay ban muon hoc gi? ")

thoigianhoc = int(input("Thoi gian hoc (phut): "))
thoigiannghi = int(input("Thoi gian nghi (phut): "))

solan = 0

#batdauchay
while True:
    print("\n" + "=" * 55)
    print(f"BAT DAU PHIEN HOC SO {solan + 1}")
    print(f"Mon hoc: {monhoc}")
    input("Nhan Enter de bat dau...")

    #demtg
    tonggiay = thoigianhoc * 60

    for i in range(tonggiay, 0, -1):
        phut = i // 60
        giay = i % 60

        tiendo = int((tonggiay - i) / tonggiay * 20)
        thanh = "#" * tiendo + "-" * (20 - tiendo)
        phantram = int((tonggiay - i) / tonggiay * 100)

        print(
            f"\rHoc: {phut:02d}:{giay:02d} "
            f"[{thanh}] {phantram}%",
            end=""
        )

        time.sleep(1)

    #xog1lanhoc
    solan += 1

    print("\n\nHET GIO HOC!")
    print(f"Ban da hoan thanh {solan} lan Pomodoro!")
    print("Rat tot! Hay tiep tuc phat huy!")

    # Dem nguoc thoi gian nghi
    print(f"\nBat dau nghi ngoi {thoigiannghi} phut...")

    tonggiay = thoigiannghi * 60

    for i in range(tonggiay, 0, -1):
        phut = i // 60
        giay = i % 60

        print(f"\rThoi gian nghi: {phut:02d}:{giay:02d}", end="")
        time.sleep(1)

    print("\nDa het thoi gian nghi!")

    #hoingdung
    tieptuc = input("\nBan co muon hoc tiep khong (c/k)? ")

    if tieptuc.lower() != "c":
        break

print("\n" + "=" * 55)
print("TONG SO PHIEN POMODORO:", solan)
print("CHUC BAN HOC TAP THAT HIEU QUA!")
print("=" * 55)
